#!/usr/bin/env python3
"""CSV/Excel 데이터를 분석하여 QBR 요약 통계를 JSON으로 출력."""

import argparse
import json
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("Error: pandas required. Install with: pip install pandas openpyxl", file=sys.stderr)
    sys.exit(1)


def load_data(filepath: str) -> pd.DataFrame:
    p = Path(filepath)
    ext = p.suffix.lower()
    if ext == ".csv":
        return pd.read_csv(filepath)
    elif ext == ".tsv":
        return pd.read_csv(filepath, sep="\t")
    elif ext in (".xlsx", ".xls"):
        return pd.read_excel(filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def analyze(df: pd.DataFrame, quarter: str | None = None, year: int | None = None) -> dict:
    result = {
        "file_info": {
            "rows": len(df),
            "columns": list(df.columns),
            "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        },
        "numeric_summary": {},
        "categorical_summary": {},
    }

    # Numeric columns
    num_cols = df.select_dtypes(include="number").columns
    for col in num_cols:
        series = df[col].dropna()
        summary = {
            "count": int(series.count()),
            "sum": round(float(series.sum()), 2),
            "mean": round(float(series.mean()), 2),
            "median": round(float(series.median()), 2),
            "min": round(float(series.min()), 2),
            "max": round(float(series.max()), 2),
            "std": round(float(series.std()), 2) if len(series) > 1 else 0,
        }
        # Top/bottom 5
        if len(series) >= 5:
            summary["top5_indices"] = series.nlargest(5).index.tolist()
            summary["bottom5_indices"] = series.nsmallest(5).index.tolist()
        result["numeric_summary"][col] = summary

    # Categorical columns
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    for col in cat_cols:
        vc = df[col].value_counts()
        result["categorical_summary"][col] = {
            "unique": int(df[col].nunique()),
            "top_values": {str(k): int(v) for k, v in vc.head(10).items()},
        }

    # Quarter/year filter info
    if quarter or year:
        result["filter"] = {"quarter": quarter, "year": year}

    # QoQ-style change rates if there are at least 2 period columns
    date_cols = df.select_dtypes(include=["datetime64"]).columns
    if len(date_cols) > 0:
        result["has_date_columns"] = list(date_cols)

    return result


def main():
    parser = argparse.ArgumentParser(description="Analyze data for QBR report")
    parser.add_argument("file", help="Path to CSV/Excel file")
    parser.add_argument("--quarter", choices=["Q1", "Q2", "Q3", "Q4"], help="Target quarter")
    parser.add_argument("--year", type=int, help="Target year")
    args = parser.parse_args()

    try:
        df = load_data(args.file)
        result = analyze(df, args.quarter, args.year)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
