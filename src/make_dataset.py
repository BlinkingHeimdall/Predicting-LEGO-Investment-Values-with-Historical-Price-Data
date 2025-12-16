from __future__ import annotations

from pathlib import Path
from datetime import datetime
import pandas as pd

# Here the file paths are set for the kaggle dataset both before and after transformation
RAW_PATH = Path("data/raw/Kaggle_LEGO_DATASET.csv")
OUT_PATH = Path("data/processed/lego_model_ready.csv")

def main() -> None:
    if not RAW_PATH.exists():
        raise FileNotFoundError(
            f"Raw LEGO dataset not found at: {RAW_PATH.resolve()}\n"
            "Place Kaggle_LEGO_DATASET.csv in data/raw/ and rerun."
        )
    
    #This reads the raw kaggle dataset
    df = pd.read_csv(RAW_PATH)

    #This will set the columns to numeric
    numeric_cols = ["USD_MSRP", "Current_Price", "Pieces", "Minifigures", "Year"]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    #This sets the minifigure count to zero if it is empty so the row doe not get dropped
    df["Minifigures"] = df["Minifigures"].fillna(0)

    before = len(df)
    df = df[
        (df["USD_MSRP"] > 0)
        & (df["Current_Price"] > 0)
        & (df["Pieces"] > 0)
        & (df["Year"] > 0)
    ].copy()
    after = len(df)

    #This is where feature engineering happens
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

    # This saves the cleaned dataset
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_model.to_csv(OUT_PATH, index=False)

    print("Step 1 complete.")
    print(f"Rows before filter: {before}")
    print(f"Rows after  filter: {after}")
    print(f"Rows model-ready : {len(df_model)}")
    print(f"Wrote: {OUT_PATH.resolve()}")

    #this is printing the missingness for verification
    print(df_model.isna().mean().sort_values(ascending=False).head(10))


if __name__ == "__main__":
    main()