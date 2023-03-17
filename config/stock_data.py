from pydantic import BaseModel


class SMACall(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    stock_interval: str
    sma_interval: int
    price_type: str


class MACDCall(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    stock_interval: str
    macd_fast: int
    macd_slow: int
    macd_smooth: int
    price_type: str


class RSICall(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    stock_interval: str
    rsi_interval: int
    price_type: str
