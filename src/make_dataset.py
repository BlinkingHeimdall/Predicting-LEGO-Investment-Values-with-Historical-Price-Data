from __future__ import annotations

from pathlib import Path
from datetime import datetime
import pandas as pd

RAW_PATH = Path("data/raw/Kaggle_LEGO_DATASET.csv")
OUT_PATH = Path("data/processed/lego_model_ready.csv")

def main() -> None:
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            f"Raw LEGO dataset not found at: {RAW_PATH.resolve()}\n"
            "Place Kaggle_LEGO_DATASET.csv in data/raw/ and rerun."
        )
    
    df = pd.read_csv(RAW_PATH)

    numeric_cols = ["USD_MSRP", "Current_Price", "Pieces", "Minifigures", "Year"]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df["Minifigures"] = df["Minifigures"].fillna(0)

    before = len(df)
    df = df[
        (df["USD_MSRP"] > 0)
        & (df["Current_Price"] > 0)
        & (df["Pieces"] > 0)
        & (df["Year"] > 0)
    ].copy()
    after = len(df)

    df["aftermarket_value_ratio"] = df["Current_Price"] / df["USD_MSRP"]
    df["price_per_piece"] = df["USD_MSRP"] / df["Pieces"]
    current_year = datetime.now().year
    df["age_years"] = current_year - df["Year"]
    df = df[df["age_years"] >= 0].copy()

    model_cols = [
        "aftermarket_value_ratio",
        "Current_Price",
        "USD_MSRP",
        "price_per_piece",
        "Pieces",
        "Minifigures",
        "age_years",
        "Theme_Group",
        "Availability",
    ]

    required_cols = [
        "aftermarket_value_ratio",
        "Current_Price",
        "USD_MSRP",
        "price_per_piece",
        "Pieces",
        "age_years",
]

    df_model = df[model_cols].dropna(subset=required_cols).copy()

    df_model["Minifigures"] = df_model["Minifigures"].astype(int)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_model.to_csv(OUT_PATH, index=False)

    print("Step 1 complete.")
    print(f"Rows before filter: {before}")
    print(f"Rows after  filter: {after}")
    print(f"Rows model-ready : {len(df_model)}")
    print(f"Wrote: {OUT_PATH.resolve()}")
    print(df_model.isna().mean().sort_values(ascending=False).head(10))


if __name__ == "__main__":
    main()