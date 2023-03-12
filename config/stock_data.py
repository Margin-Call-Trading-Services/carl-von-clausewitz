from pydantic import BaseModel


class SMAData(BaseModel):
    ticker: str
    sma_value: int
    price_type: str
    data: list[dict]


class MACDData(BaseModel):
    ticker: str
    macd_fast: int
    macd_slow: int
    macd_smooth: int
    price_type: str
    data: list[dict]
