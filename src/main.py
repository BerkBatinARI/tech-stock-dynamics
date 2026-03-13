from pathlib import Path

import pandas as pd
import yfinance as yf


TICKERS = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA"]
START_DATE = "2018-01-01"
END_DATE = None


def download_prices() -> pd.DataFrame:
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
    return close_df


def normalize_prices(close_df: pd.DataFrame) -> pd.DataFrame:
    normalized_df = close_df.copy()
    normalized_df = normalized_df.dropna()
    normalized_df = normalized_df / normalized_df.iloc[0] * 100
    return normalized_df


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"

    data_dir.mkdir(exist_ok=True)

    close_df = download_prices()
    close_df.to_csv(data_dir / "tech_prices.csv")

    normalized_df = normalize_prices(close_df)
    normalized_df.to_csv(data_dir / "tech_prices_normalized.csv")

    print("Download and normalization complete.")
    print(f"Saved raw prices: {data_dir / 'tech_prices.csv'}")
    print(f"Saved normalized prices: {data_dir / 'tech_prices_normalized.csv'}")


if __name__ == "__main__":
    main()