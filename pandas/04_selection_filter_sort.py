"""Pandas 第 2 课：选择、筛选和排序日 K 数据。"""

import pandas as pd

# 创建示例 DataFrame
df = pd.DataFrame(
    {
        "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
        "年龄": [25, 30, 28, 35, 22],
        "城市": ["北京", "上海", "广州", "深圳", "杭州"],
    },
    index=[1, 3, 5, 7, 9],
)  # 注意：索引不是连续的

print("DataFrame：")
print(df)
print()

""" 位置切片 """

# loc: 使用标签索引（包含结束位置）
print("df.loc[1:5]（标签切片，包含5）：")
print(df.loc[1:5, ["姓名", "年龄"]])  # 选择行标签1到5，列标签为"姓名"和"年龄"
print()

# iloc: 使用位置索引（不包含结束位置）
print("df.iloc[0:2]（位置切片，不包含2）：")
print(df.iloc[0:2])
print()

""" 筛选行 """

print("筛选行：")

# 1 DataFrame

print(df["年龄"] > 30)  # 返回布尔 Series，表示每行的"年龄"是否大于30
print()
print(df[df["年龄"] > 30])  # 返回满足条件的行
print()

# 2 loc
print(df.loc[df["年龄"] > 30])
print()

# 3 iloc
print(df.iloc[df["年龄"] > 30])  # 注意：iloc 不能直接使用布尔 Series 进行筛选，会报错
print()


""" 同时筛选行和列 """
print("同时筛选行和列:")

# 1 DataFrame

print(df[df["年龄"] > 30][["姓名", "年龄"]])  # 返回满足条件的行和指定列
print()

# 2 loc
print(df.loc[df["年龄"] > 30, ["姓名", "年龄"]])
print()

# 3 iloc
print(df.iloc[df["年龄"] > 30, [0, 1]])  # 返回满足条件的行和指定列（使用位置索引）
print()
