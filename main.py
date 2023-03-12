from fastapi import Body, FastAPI

from config.stock_data import SMAData, MACDData
from strategies.macd_calculation import MACD_Calculation
from strategies.sma_calculation import SMA_Calcuation


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "See README.md to learn how to use the API"}


@app.post("/sma")
def calculate_sma(stock_data: SMAData):
    try:
        SMA_Class = SMA_Calcuation(
            stock_data.ticker,
            stock_data.sma_value,
            stock_data.price_type,
            stock_data.data,
        )
    except:
        return {
            "Error_Message": "Unable to calculate SMA due to incorrect json data format"
        }
    return SMA_Class.calculate_sma()


@app.post("/macd")
def calculate_macd(stock_data: MACDData):
    try:
        MACD_Class = MACD_Calculation(
            stock_data.ticker,
            stock_data.macd_fast,
            stock_data.macd_slow,
            stock_data.macd_smooth,
            stock_data.price_type,
            stock_data.data,
        )
    except:
        return {
            "Error_Message": "Unable to calculate MACD due to incorrect json data format"
        }
    return MACD_Class.calculate_macd()
