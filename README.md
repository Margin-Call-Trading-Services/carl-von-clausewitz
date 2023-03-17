# Carl Von Clausewitz
The esteemed Prussian general and military strategiest stressed the importance of the political and psycholocial aspects of war. His theories and tactics have influenced many polical leaders through out history such as Lenin, Hitler, and Mao (obviously not a list of leaders you want appreciating your work and are complete POSs). Nevertheless, Von Clausewitz has conjured a couple of well-known quotes that epitomizes the ambition of this repository:
  - If the leader is filled with high ambition and if he pursues his aims with audacity and strength of will, he will reach them despite all obstacles.
  - It is even better to act quuickly and err, than to hesitate until the time for action is past


## Description
This repository includes all of the various indicators that can be used to analyze the value of a security. Currently, there are only two strategies: SMA and MACD. Depending on the strategy used, the curl post request will require different inputs. This will be outlined on the how to section. 


# Endpoints

Below is the list of endpoints for each of the various strategies currently in the repo. Note :the format of the json file/message can be seen in the test data folder for each of the indicators. 

## POST '/macd'

Expected input parameters:
  - ticker: str
  - start_date: str
  - end_date: str
  - stock_interval: str
  - macd_fast: int
  - macd_slow: int
  - macd_smooth: int
  - price_type: str


When the /macd post is invoked, it makes a call to the get-dat-money api endpoint 'GET /api/v1/prices'. Using the start_date, end_date, and stock_interval, the stock data is returned. The json file is then parsed for the price data and used to calculate the macd.

The macd fast and slow are used to calculate the macd line (fast should be a lower number than slow) the macd smooth will calculate the ema for the macd line based on the provided value. The price type either open, high, low, close, or adj_close. The data is provided from the get-dat-money api, this is the stock data for a given time interval.


## POST '/sma'

Expected input parameters:
  - ticker: str
  - start_date: str
  - end_date: str
  - stock_interval: str
  - sma_interval: int
  - price_type: str

When the /sma post is invoked, it makes a call to the get-dat-money api endpoint 'GET /api/v1/prices'. Using the start_date, end_date, and stock_interval, the stock data is returned. The json file is then parsed for the price data and used to calculate the sma.

The sma_interval is the simple moving average period (EX: 5 period, 7 period, 14 period, etc). The price_type can be either open, high, low, close, or adj_close. The data is provided from the get-dat-money api, this is the stock data for a given time interval.

## POST '/rsi'

Expected input parameters:
  - ticker: str
  - start_date: str
  - end_date: str
  - stock_interval: str
  - rsi_interval: int
  - price_type: str

When the /rsi post is invoked, it makes a call to the get-dat-money api endpoint 'GET /api/v1/prices'. Using the start_date, end_date, and stock_interval, the stock data is returned. The json file is then parsed for the price data and used to calculate the rsi.

The rsi_interval is the number of price data points that are used to calculate a single rsi data point. The price_type can be either open, high, low, close, or adj_close. The data is provided from the get-dat-money api, this is the stock data for a given time interval.


# Running Locally

There are two make commands: 'make start' and 'make kill'

After the command is called, the following curl commands can be used to test out the api:

'curl -X POST -H "Content-Type: application/json" -d @test_data/<filename.json> http://localhost:8001/<endpoint>'

Example for macd_request:

'curl -X POST -H "Content-Type: application/json" -d @test_data/macd_request.json http://localhost:8001/macd'



# TODO and Notes for myself

## TODO List
  - Need to adjust indicators to digest different interval data (min, hrs, days, weeks, etc)
  - Need to write unit tests
  - Need to add bollinger bands
  - Look into other indicators, check this website: https://www.investopedia.com/top-7-technical-analysis-tools-4773275

### How to start up virtual environment
Type this in terminal: source venv/bin/activate
This will switch the terminal to the virtual environment

### To start up API
uvicorn main:app
to open it in developer mode -> uvicorn main:app --reload

### To Spin up Docker Container
docker-compose up -d



