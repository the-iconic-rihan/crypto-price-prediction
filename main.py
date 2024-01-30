# app.py

import streamlit as st
from datetime import date, timedelta
import time,os
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objs as go
from loguru import logger
import smtplib
from dotenv import load_dotenv  # Import the load_dotenv function
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Load environment variables from .env
load_dotenv()
# Configure Loguru
logger.add("crypto_price_prediction.log", rotation="500 MB", level="INFO")

email_address = os.environ['email_address']
email_password =os.environ["email_password"]
smtp_server = os.environ["smtp_server"]
smtp_port = os.environ["smtp_port"]

# Navigation header
st.set_page_config(layout="wide", page_title="Crypto Price Prediction App", page_icon="📈")
st.title('Crypto Price Prediction App')

# Set custom styles using HTML and CSS
st.markdown(
    """
    <style>
    .reportview-container .markdown-text-container {
        font-family: 'Nunito Sans', sans-serif;
    }
    .main-container {
        max-width: 1200px;
        padding-top: 2rem;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .stButton button {
        background-color: #007bff !important;
        border-radius: 4px !important;
        color: white !important;
    }
    .stButton button:hover {
        background-color: #0069d9 !important;
    }
    .stTextInput input {
        background-color: #f8f9fa !important;
        color: #495057 !important;
        border-radius: 4px !important;
    }
    .block-container {
        width: 80%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def load_data(ticker, start_date, end_date):
    """
    Load historical data for the selected cryptocurrency.

    Parameters:
        ticker (str): The symbol of the cryptocurrency.
        start_date (date): The start date for data retrieval.
        end_date (date): The end date for data retrieval.

    Returns:
        pd.DataFrame: Historical price data.
    """
    try:
        data = yf.download(ticker, start_date, end_date)
        data.reset_index(inplace=True)
        logger.info(f"Data loaded successfully for {ticker}")
        return data
    except Exception as e:
        logger.error(f"Error loading data for {ticker}: {str(e)}")
        st.error(f"Error loading data for {ticker}. Please check the cryptocurrency symbol.")
        st.stop()

def display_raw_data(data):
    """
    Display the raw data in the Streamlit app.

    Parameters:
        data (pd.DataFrame): The DataFrame containing raw data.
    """
    st.subheader('Raw data')
    st.dataframe(data.tail())
    logger.info("Raw data displayed")

def plot_time_series(data):
    """
    Plot the time series data in the Streamlit app.

    Parameters:
        data (pd.DataFrame): The DataFrame containing time series data.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Open Price', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Close Price', line=dict(color='blue')))
    fig.update_layout(title='Time Series Data', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    logger.info("Time series data plotted")

def predict_and_display_forecast(df_train, period):
    """
    Predict and display forecast in the Streamlit app.

    Parameters:
        df_train (pd.DataFrame): The DataFrame containing training data.
        period (int): The prediction period.

    Returns:
        Prophet: The trained Prophet model.
        pd.DataFrame: The forecast data.
    """
    try:
        m = Prophet(
            yearly_seasonality='auto',
            weekly_seasonality=False,
            daily_seasonality=False,
            seasonality_mode='multiplicative',
            changepoint_prior_scale=0.05
        )
        m.fit(df_train)

        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        # Display forecast data
        st.subheader('Forecast Data')
        st.dataframe(forecast.tail())
        logger.info("Forecast data displayed")

        # Display forecast chart
        st.subheader('Forecast Chart')
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)
        logger.info("Forecast chart displayed")

        # Display forecast components
        st.subheader('Forecast Components')
        fig2 = m.plot_components(forecast)
        st.write(fig2)
        logger.info("Forecast components displayed")

        return m, forecast
    except Exception as e:
        logger.error(f"Error predicting and displaying forecast: {str(e)}")
        st.error("An error occurred while generating the forecast. Please try again.")
        st.stop()

# def send_email_notification(user_email, subject, body):
#     """
#     Send email notification.

#     Parameters:
#         user_email (str): Email address of the user.
#         subject (str): Subject of the email.
#         body (str): Body of the email.
#     """
#     message = MIMEMultipart()
#     message['From'] = email_address
#     message['To'] = user_email
#     message['Subject'] = subject
#     message.attach(MIMEText(body, 'plain'))

#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()
#         server.login(email_address, email_password)
#         server.sendmail(email_address, user_email, message.as_string())
#         logger.info(f"Email notification sent to {user_email}")

# Main Streamlit app logic
if __name__ == "__main__":
    crypto_symbols = ['BTC', 'ETH-USD', 'USDT', 'DOGE-USD', 'XRP-USD', 'BCH', 'LTC', 'ADA-USD', 'DOT', 'LINK', 'BNB']
    selected_crypto = st.selectbox('Select dataset for prediction', crypto_symbols, key="selected_crypto")

    n_years = st.number_input('Years of prediction:', min_value=1, max_value=10, value=5, key="n_years")
    period = n_years * 365

    start_date = st.date_input("Start Date", value=date(2015, 1, 1), key="start_date")
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date = date.today().strftime("%Y-%m-%d")

    data_load_state = st.empty()
    data_load_state.text('Loading data...')
    data = load_data(selected_crypto, start_date_str, end_date)
    data_load_state.text('')

    display_raw_data(data)
    plot_time_series(data)

    # # Section for Email Notifications
    # st.sidebar.header("Email Notifications")
    # user_email = st.sidebar.text_input("Enter your email:", key="user_email_input")

    # if st.sidebar.button("Enable Email Notifications"):
    #     subject = "Crypto Price Alert"
    #     body = "The price has crossed your specified threshold."
    #     send_email_notification(user_email, subject, body)
    #     st.sidebar.success("Email notification enabled.")

    # Section for Advanced Analytics
    st.sidebar.header("Advanced Analytics")
    window = st.sidebar.slider("Select Moving Average Window", min_value=1, max_value=50, value=20, key="ma_window")
    data['MA'] = data['Close'].rolling(window=window).mean()

    # Update the chart with Moving Average
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Open Price', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Close Price', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['MA'], name=f'Moving Average ({window} days)', line=dict(color='green')))
    fig.update_layout(title='Time Series Data with Moving Average', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

    # Predict button functionality
    if st.button("Predict", key="predict_button"):
        element_to_hide = st.empty()
        element_to_hide.text("Please wait...")
        time.sleep(10)
        with st.spinner('Generating forecast...'):
            df_train = data[['Date', 'Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            # Check if df_train has enough non-NaN rows
            if df_train.dropna().shape[0] < 2:
                st.warning("Insufficient data for prediction. Please check your dataset.")
            else:
                m = Prophet(
                    yearly_seasonality='auto',
                    weekly_seasonality=False,
                    daily_seasonality=False,
                    seasonality_mode='multiplicative',
                    changepoint_prior_scale=0.05
                )
                m.fit(df_train)

                future = m.make_future_dataframe(periods=period)
                forecast = m.predict(future)

                st.subheader('Forecast Data')
                st.dataframe(forecast.tail())

                st.subheader('Forecast Chart')
                fig1 = plot_plotly(m, forecast)
                st.plotly_chart(fig1)

                st.subheader('Forecast Components')
                fig2 = m.plot_components(forecast)
                st.write(fig2)

                # Hide the "Please wait..." text and show the results
                st.success('Prediction generated successfully!')

        element_to_hide.text("")
