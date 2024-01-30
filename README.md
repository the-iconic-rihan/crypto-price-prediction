# Crypto Price Prediction App

This is a simple web application built with Streamlit that allows you to predict the future prices of cryptocurrencies using the Facebook Prophet library.

## Features

- Select from a list of available cryptocurrencies.
- Choose the number of years for prediction (1-10 years).
- Visualize the historical price data of the selected cryptocurrency.
- Generate price forecasts using the Facebook Prophet model.
- Display forecasted data and visualization of the predicted prices.
- Responsive and user-friendly interface.

## Installation

Follow the instructions below to set up the Crypto Price Prediction App on your local machine.

### Prerequisites

- Python 3.7 or higher installed on your system.
- Git installed on your system (optional, required only for cloning the repository).

### Step 1: Clone the repository (or download the code)

If you have Git installed, you can clone the repository using the following command:

```
git clone https://github.com/your-username/crypto-price-prediction.git
```

- Alternatively, you can download the code as a ZIP file by clicking on the "Code" button on the repository page and selecting "Download ZIP".

### Step 2: Create and activate a virtual environment (optional, but simple python virtual env is not recomendend for windows users)

It is recommended to create a conda virtual environment to keep the project dependencies isolated. Open your anaconda terminal or command prompt, navigate to the project directory, and run the following commands:

use conda virtual env for easy installtion. for below steps : 

```#
python -m venv myenv

# Activate the virtual environment
# For Windows
myenv\Scripts\activate

# For macOS/Linux
source myenv/bin/activate

# you need to downlaod the Anaconda if not downlaoded.

conda create --name your_env_name python=3.8
conda activate your_env_name

```

### Step 3: Install the dependencies

Navigate to the project directory and install the required Python dependencies by running the following command:

```
pip install -r requirements.txt
```

### Step 4: Run the application

To start the Crypto Price Prediction App, run the following command:

```
streamlit run app.py

```

This will start the application locally, and you can access it by opening the provided URL in your web browser.

# IDE-specific Instructions

### PyCharm

<ol><li>Open PyCharm and click on "Open" to select the project directory.</li>
<li>Configure the Python interpreter to use the virtual environment (if created).</li>
<li>Install the required packages by running pip install -r requirements.txt in the terminal.</li>
<li>Click on the "Run" button or use the keyboard shortcut to start the application.</li></ol>

### Spyder IDE

<ol><li>Open Spyder IDE and click on "Open Project" to select the project directory.</li>
<li>Create and activate a virtual environment (if desired).</li>
<li>Install the required packages by running pip install -r requirements.txt in the IPython console.</li>
<li>Run the application by executing the app.py file.</li>

# Supported Operating Systems

### The Crypto Price Prediction App is compatible with the following operating systems:

<ol>
<li>Windows</li>
<li>macOS</li>
<li>Linux</li></ol>

# Troubleshooting

### ModuleNotFoundError: No module named 'yfinance'

- If you encounter this error, it means the yfinance module is not installed. To resolve it, run the following command:

```
pip install yfinance
```

# ModuleNotFoundError: No module named 'prophet'

- If you face this error, it means the prophet library is missing. Follow the instructions below to install it:

### For Windows users:

<ul>
<li>
Install Microsoft Visual C++ Build Tools from this link: <br>https://visualstudio.microsoft.com/visual-cpp-build-tools/.</li>
<li>Restart your computer.</li>
<li>Retry the installation of prophet using the command: pip install prophet.</li></ul>

- For macOS and Linux users, please refer to the official documentation of fbprophet for installation instructions specific to your operating system.

# Contributing

Contributions to the Crypto Price Prediction App are welcome! If you find any issues or have suggestions for improvement, please feel free to submit a pull request.

# License

This project is licensed under the MIT License.

```
Please note that the instructions provided above are general guidelines, and you may need to adapt them based on your specific setup and requirements.
```

# Output

![Crypto Price Prediction App2_pages-to-jpg-0001](https://github.com/the-iconic-rihan/crypto-price-prediction/assets/68491627/d318d310-c2ae-4407-b090-e90b410327ec)
![Crypto Price Prediction App2_pages-to-jpg-0002](https://github.com/the-iconic-rihan/crypto-price-prediction/assets/68491627/1dfbbcac-b80a-4fd5-8ce1-cb07e55685d6)
![Crypto Price Prediction App2_pages-to-jpg-0003](https://github.com/the-iconic-rihan/crypto-price-prediction/assets/68491627/249815d4-5a7a-4ab9-ae48-3a58a240456d)
