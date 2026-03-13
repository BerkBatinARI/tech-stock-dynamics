from pathlib import Path

import matplotlib.pyplot as plt
import bar_chart_race as bcr
import pandas as pd


INPUT_FILE = "tech_prices_normalized.csv"
OUTPUT_FILE = "tech_stock_dynamics.gif"
RESAMPLE_RULE = "ME"
TOP_N = 7

COLORS = {
    "AAPL": "#B0B7C3",
    "MSFT": "#00A300",
    "NVDA": "#76B900",
    "GOOGL": "#1A73E8",
    "AMZN": "#FF9900",
    "META": "#0057FF",
    "TSLA": "#E31937",
}


def summary(values, ranks):
    return {
        "x": 0.01,
        "y": 0.02,
        "s": "Normalized price index (100 = start value in Jan 2018)",
        "ha": "left",
        "va": "bottom",
        "size": 11,
        "color": "black",
        "weight": "bold",
    }


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / INPUT_FILE
    output_path = project_root / "output" / OUTPUT_FILE

    df = pd.read_csv(data_path, index_col=0, parse_dates=True)
    df = df.resample(RESAMPLE_RULE).last().dropna(how="all")

    plt.rcParams["figure.facecolor"] = "white"
    plt.rcParams["axes.facecolor"] = "white"
    plt.rcParams["savefig.facecolor"] = "white"
    plt.rcParams["text.color"] = "black"
    plt.rcParams["axes.labelcolor"] = "black"
    plt.rcParams["xtick.color"] = "black"
    plt.rcParams["ytick.color"] = "black"

    bcr.bar_chart_race(
        df=df,
        filename=str(output_path),
        orientation="h",
        sort="desc",
        n_bars=TOP_N,
        fixed_order=False,
        fixed_max=False,
        steps_per_period=35,
        period_length=220,
        interpolate_period=True,
        label_bars=True,
        bar_size=0.9,
        period_fmt="%b %Y",
        period_label={"x": 0.98, "y": 0.12, "ha": "right", "va": "center", "size": 22},
        period_summary_func=summary,
        title="Tech Stock Dynamics",
        title_size=19,
        figsize=(12, 7),
        cmap=[COLORS.get(col, "#4C78A8") for col in df.columns],
        shared_fontdict={"color": "black", "weight": "normal"},
        filter_column_colors=True,
        bar_kwargs={"alpha": 1.0},
    )

    print(f"Animation saved to: {output_path}")
    print(f"Periods used: {len(df)}")
    print(f"Date range: {df.index.min().date()} to {df.index.max().date()}")
    print("X-axis meaning: normalized price index where 100 = starting value")


if __name__ == "__main__":
    main()