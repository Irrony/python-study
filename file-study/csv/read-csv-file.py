import pandas as pd

file_path = '../../files/csv-files/read.csv'

# 读取csv文件
# csv_data = pd.read_csv(file_path)
# print(csv_data)

# 读取特定行的数据
row = [1, 3]  # 读取第二行和第四行的数据
csv_data = pd.read_csv(file_path)
specific_rows = csv_data.iloc[row]
print(specific_rows.to_string(index=False, header=None))  # 不带索引，不带列名

# 读取特定行范围内的数据
start_row = 2
end_row = 5
specific_rows = pd.read_csv(file_path, skiprows=range(1,start_row), nrows=end_row - start_row + 1)  # 读第二行到第五行的数据
print(specific_rows)

# 读取特定列的数据
col = [1, 2]  # 读取第二列和第三列数据
specific_cols = pd.read_csv(file_path, usecols=col)
print(specific_cols)

# 读取特定列范围内的数据
start_col = 1
end_col = 3
specific_cols = pd.read_csv(file_path, usecols=range(start_col, end_col+1))  # 读取第二列到第四列数据
print(specific_cols)

# 读取特定单元格
row_index = 1
col_index = 2
csv_data = pd.read_csv(file_path)
specific_cell = csv_data.iloc[row_index, col_index]  # 读取第二行第三列的单元格数据
print(specific_cell)
