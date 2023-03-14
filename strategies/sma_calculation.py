import pandas as pd
import json


class SMA_Calcuation:
    def __init__(
        self, ticker: str, sma_interval: int, price_type: str, data: list[dict]
    ):
        self.ticker = ticker
        self.sma_interval = sma_interval
        self.price_type = price_type
        self.data = data
        self.sma_data_df = None

    def calculate_sma(self):
        try:
            data_df = pd.DataFrame(self.data)
        except:
            return {"Error_Message": "Unable to convert json data to DataFrame"}

        try:
            self.sma_data_df = data_df["date"].to_frame()
            self.sma_data_df[f"sma_{self.sma_interval}"] = (
                data_df[f"{self.price_type}"].rolling(self.sma_interval).mean()
            )
        except:
            return {"Error_Message": "Unable to Calculate SMA due to price error"}

        return json.loads(self.sma_data_df.to_json(orient="records"))
