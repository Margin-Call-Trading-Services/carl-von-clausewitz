import pandas as pd


class MACD_Calculation:
    def __init__(
        self,
        ticker: str,
        macd_fast: int,
        macd_slow: int,
        macd_smooth: int,
        price_type: str,
        data: list[dict],
    ):
        self.ticker = ticker
        self.macd_fast = macd_fast
        self.macd_slow = macd_slow
        self.macd_smooth = macd_smooth
        self.price_type = price_type
        self.data = data

    def calculate_macd(self):
        try:
            data_df = pd.DataFrame(self.data)
        except:
            return {"Error_Message": "Unable to convert json data to DataFrame"}

        try:
            self.macd_data_df = data_df["date"].to_frame()
            macd_fast = (
                data_df["close"]
                .ewm(span=self.macd_fast, adjust=False, min_periods=self.macd_fast)
                .mean()
            )
            macd_slow = (
                data_df["close"]
                .ewm(span=self.macd_slow, adjust=False, min_periods=self.macd_slow)
                .mean()
            )
            macd = macd_fast - macd_slow
            self.macd_data_df[
                f"macd_line_{self.macd_fast}_{self.macd_slow}"
            ] = self.macd_data_df.index.map(macd)

            macd_smooth = (
                self.macd_data_df[f"macd_line_{self.macd_fast}_{self.macd_slow}"]
                .ewm(span=self.macd_smooth, adjust=False, min_periods=self.macd_smooth)
                .mean()
            )

            self.macd_data_df[
                f"macd_smooth_{self.macd_smooth}"
            ] = self.macd_data_df.index.map(macd_smooth)

        except:
            return {"Error_Message": "Unable to calculate MACD from DataFame"}

        return self.macd_data_df.to_json(orient="records")
