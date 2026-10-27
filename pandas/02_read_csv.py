"""读取 CSV"""

from pathlib import Path

import pandas as pd

# CSV文件所在路径
csv_path = Path(__file__).parent / "data" / "daily_bars.csv"


bars = pd.read_csv(
    csv_path,
    # 约定每列的数据类型
    dtype={
        "symbol": str,
        "name": str,
        "volume": float,
    },
    # 读取时直接把日期转为日期类型
    parse_dates=["date"],
)


print("=== 前 5 行 ===")
print(bars.head())

print("\n=== 表的大小 ===")
print(f"共有 {bars.shape[0]} 行、{bars.shape[1]} 列")

print("\n=== 每列类型和空值情况 ===")
bars.info()

print("\n=== 数值列统计 ===")
print(bars[["open", "high", "low", "close", "volume"]].describe().round(2))

print("\n日期范围：", bars["date"].min().date(), "至", bars["date"].max().date())
