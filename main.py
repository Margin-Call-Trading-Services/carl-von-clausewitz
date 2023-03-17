from fastapi import Body, FastAPI
import requests

from config.stock_data import SMACall, MACDCall, RSICall
from strategies.macd_calculation import MACD_Calculation
from strategies.sma_calculation import SMA_Calcuation
from strategies.rsi_calculation import RSI_Calculation

app = FastAPI()


@app.post("/sma")
def calculate_sma(stock_info: SMACall):
    try:
        stock_data_req = requests.get(
            f"http://host.docker.internal:8080/api/v1/prices?ticker={stock_info.ticker}&start_date={stock_info.start_date}&end_date={stock_info.end_date}"
        )
        # Assume stock_data_req needs to get processed to turn into a json file, if that is case, use stock_data_json = stock_data_req
        stock_data_json = stock_data_req.json()
        stock_data = stock_data_json["data"]["price_data"]
    except:
        return {
            "Error: Unable to get data from get-dat-money api or cannot retrieve stock data from request"
        }

    try:
        SMA_Class = SMA_Calcuation(
            stock_info.ticker,
            stock_info.sma_interval,
            stock_info.price_type,
            stock_data,
        )

    except:
        return {"Unable to calculate SMA due to json input format error"}

    return SMA_Class.calculate_sma()


@app.post("/macd")
def calculate_macd(stock_info: MACDCall):
    try:
        stock_data_req = requests.get(
            f"http://host.docker.internal:8080/api/v1/prices?ticker={stock_info.ticker}&start_date={stock_info.start_date}&end_date={stock_info.end_date}"
        )
        # Assume stock_data_req needs to get processed to turn into a json file, if that is case, use stock_data_json = stock_data_req
        stock_data_json = stock_data_req.json()
        stock_data = stock_data_json["data"]["price_data"]
    except:
        return {
            "Error: Unable to get data from get-dat-money api or cannot retrieve stock data from request"
        }

    try:
        MACD_Class = MACD_Calculation(
            stock_info.ticker,
            stock_info.macd_fast,
            stock_info.macd_slow,
            stock_info.macd_smooth,
            stock_info.price_type,
            stock_data,
        )

    except:
        return {"Unable to calculate SMA due to json input format error"}

    return MACD_Class.calculate_macd()


@app.post("/rsi")
def calculate_rsi(stock_info: RSICall):
    try:
        stock_data_req = requests.get(
            f"http://host.docker.internal:8080/api/v1/prices?ticker={stock_info.ticker}&start_date={stock_info.start_date}&end_date={stock_info.end_date}"
        )
        # Assume stock_data_req needs to get processed to turn into a json file, if that is case, use stock_data_json = stock_data_req
        stock_data_json = stock_data_req.json()
        stock_data = stock_data_json["data"]["price_data"]
    except:
        return {
            "Error: Unable to get data from get-dat-money api or cannot retrieve stock data from request"
        }

    try:
        RSI_Class = RSI_Calculation(
            stock_info.ticker,
            stock_info.rsi_interval,
            stock_info.price_type,
            stock_data,
        )

    except:
        return {"Unable to calculate SMA due to json input format error"}

    return RSI_Class.calculate_rsi()
