from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "tech_rankings.csv"
    output_path = project_root / "output" / "tech_stock_rankings.png"

    df = pd.read_csv(data_path, index_col=0, parse_dates=True)

    plt.figure(figsize=(12, 7))

    for ticker in df.columns:
        plt.plot(df.index, df[ticker], label=ticker)

    plt.gca().invert_yaxis()
    plt.title("Daily Ranking of Tech Stocks")
    plt.xlabel("Date")
    plt.ylabel("Rank (1 = highest performer)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Chart saved to: {output_path}")


if __name__ == "__main__":
    main()