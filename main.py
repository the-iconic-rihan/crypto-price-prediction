# import streamlit as st
# from datetime import date, timedelta
# import time
# import yfinance as yf

# from prophet import Prophet
# from prophet.plot import plot_plotly
# import plotly.graph_objs as go
# import pandas as pd

# # Set the Nunito Sans font
# st.set_page_config(layout="wide", page_title="Crypto Price Prediction App", page_icon="📈")
# st.markdown(
#     """
#     <style>
#     .reportview-container .markdown-text-container {
#         font-family: 'Nunito Sans', sans-serif;
#     }
#     .main-container {
#         max-width: 1200px;
#         padding-top: 2rem;
#     }
#     .sidebar .sidebar-content {
#         background-color: #f8f9fa;
#     }
#     .stButton button {
#         background-color: #007bff !important;
#         border-radius: 4px !important;
#         color: white !important;
#     }
#     .stButton button:hover {
#         background-color: #0069d9 !important;
#     }
#     .stTextInput input {
#         background-color: #f8f9fa !important;
#         color: #495057 !important;
#         border-radius: 4px !important;
#     }
#     .block-container {
#         width: 80%;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Navigation header
# st.title('Crypto Price Prediction App')

# crypto_symbols = ['BTC', 'ETH-USD', 'USDT', 'DOGE-USD', 'XRP-USD', 'BCH', 'LTC', 'ADA-USD', 'DOT', 'LINK', 'BNB']

# selected_crypto = st.selectbox('Select dataset for prediction', crypto_symbols)

# n_years = st.number_input('Years of prediction:', min_value=1, max_value=10, value=5)
# period = n_years * 365

# # Start date
# start_date = st.date_input("Start Date", value=date(2015, 1, 1))
# start_date_str = start_date.strftime("%Y-%m-%d")

# # End date
# end_date = date.today().strftime("%Y-%m-%d")

# @st.cache_data
# def load_data(ticker):
#     data = yf.download(ticker, start_date_str, end_date)
#     data.reset_index(inplace=True)
#     return data

# data_load_state = st.empty()
# data_load_state.text('Loading data...')
# data = load_data(selected_crypto)
# data_load_state.text('')

# st.subheader('Raw data')
# st.dataframe(data.tail())

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Open Price'))
# fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Close Price'))
# fig.update_layout(title='Time Series Data', xaxis_rangeslider_visible=True)
# st.plotly_chart(fig)

# if st.button("Predict", key="predict_button"):
#     element_to_hide = st.empty()
#     element_to_hide.text("PLease wait...")
#     time.sleep(10)
#     with st.spinner('Generating forecast...'):
#         df_train = data[['Date', 'Close']]
#         df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
#         m = Prophet(
#             yearly_seasonality='auto',
#             weekly_seasonality=False,
#             daily_seasonality=False,
#             seasonality_mode='multiplicative',
#             changepoint_prior_scale=0.05
#         )
#         m.fit(df_train)

#         future = m.make_future_dataframe(periods=period)
#         forecast = m.predict(future)

#         st.subheader('Forecast Data')
#         st.dataframe(forecast.tail())

#         st.subheader('Forecast Chart')
#         fig1 = plot_plotly(m, forecast)
#         st.plotly_chart(fig1)

#         st.subheader('Forecast Components')
#         fig2 = m.plot_components(forecast)
#         st.write(fig2)

#         # Hide the "Please wait..." text and show the results
#         st.success('Prediction generated successfully!')
#     element_to_hide.text("")



import streamlit as st
from datetime import date, timedelta
import time
import yfinance as yf

from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objs as go
import pandas as pd

# Set the Nunito Sans font
st.set_page_config(layout="wide", page_title="Crypto Price Prediction App", page_icon="📈")
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

# Navigation header
st.title('Crypto Price Prediction App')

crypto_symbols = ['BTC', 'ETH-USD', 'USDT', 'DOGE-USD', 'XRP-USD', 'BCH', 'LTC', 'ADA-USD', 'DOT', 'LINK', 'BNB']

selected_crypto = st.selectbox('Select dataset for prediction', crypto_symbols)

n_years = st.number_input('Years of prediction:', min_value=1, max_value=10, value=5)
period = n_years * 365

# Start date
start_date = st.date_input("Start Date", value=date(2015, 1, 1))
start_date_str = start_date.strftime("%Y-%m-%d")

# End date
end_date = date.today().strftime("%Y-%m-%d")

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start_date_str, end_date)
    data.reset_index(inplace=True)
    return data

data_load_state = st.empty()
data_load_state.text('Loading data...')
data = load_data(selected_crypto)
data_load_state.text('')

st.subheader('Raw data')
st.dataframe(data.tail())

fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Open Price'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Close Price'))
fig.update_layout(title='Time Series Data', xaxis_rangeslider_visible=True)
st.plotly_chart(fig)

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
