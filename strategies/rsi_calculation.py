import pandas as pd
import pandas_ta as ta

import json


class RSI_Calculation:
    def __init__(
        self, ticker: str, rsi_interval: int, price_type: str, data: list[dict]
    ) -> None:
        self.ticker = ticker
        self.rsi_interval = rsi_interval
        self.price_type = price_type
        self.data = data

    def calculate_rsi(self):
        data_df = pd.DataFrame(self.data)
        self.rsi_df = data_df["date"].to_frame()

        self.rsi_df[f"rsi_{self.rsi_interval}"] = data_df.ta.rsi(
            close="close", length=self.rsi_interval, append=True
        )

        return json.loads(self.rsi_df.to_json(orient="records"))
