"""导出 CSV"""

import pandas as pd

from pathlib import Path

# CSV想要存的路径
output_csv_path = Path(__file__).parent / "data" / "output" / "output.csv"

# 准备测试数据
df = pd.DataFrame(
    {
        "姓名": ["张三", "李四", "王五", "赵六"],
        "年龄": [25, 30, 28, 35],
        "城市": ["北京", "上海", "广州", "深圳"],
        "薪资": [12000, 15000, 11000, 18000],
    }
)

# 最基本的导出（包含索引）
# df.to_csv(
#     output_csv_path,
# )

# 不包含索引
# df.to_csv(output_csv_path, index=False)


# 不写入表头
df.to_csv(output_csv_path, header=False)


print("导出CSV文件")
