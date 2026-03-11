from pathlib import Path

import pandas as pd
import yfinance as yf


TICKERS = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA"]
START_DATE = "2018-01-01"
END_DATE = None


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"
    output_dir = project_root / "output"

    data_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    print("Downloading tech stock data...")
    df = yf.download(
        TICKERS,
        start=START_DATE,
        end=END_DATE,
        auto_adjust=True,
        progress=False,
    )

    close_df = df["Close"].copy()
    close_df = close_df.dropna(how="all")
    close_df.to_csv(data_dir / "tech_prices.csv")

    print("Download complete.")
    print(f"Saved file: {data_dir / 'tech_prices.csv'}")
    print(f"Shape: {close_df.shape}")
    print(close_df.tail())


if __name__ == "__main__":
    main()