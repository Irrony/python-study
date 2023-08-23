import pandas as pd

old_file_path = '../../files/csv-files/read.csv'
file_path = '../../files/csv-files/delete.csv'

csv_data = pd.read_csv(old_file_path)
df_csv = pd.DataFrame(csv_data)

#  根据行索引删除指定行数据
del_rows = [1, 3]  # 删除第二行和第四行数据
del_rows1 = range(1, 4)  # 删除第二行到第四行的行数据（左开右闭）
result = df_csv.drop(del_rows)
result.to_csv(file_path, index=False)

# 根据列索引删除指定列数据
del_cols = [0, 2]  # 删除第一列和第三列数据
result = df_csv.drop(df_csv.columns[del_cols], axis=1)
result.to_csv(file_path, index=False)

# 根据列标签删除列数据
result = df_csv.drop('Price', axis=1)
result.to_csv(file_path, index=False)

# 根据行列索引删除指定单元格数据
df_csv.loc[1, df_csv.columns[1]] = None  # 删除第二行第二列对应单元格的数据
df_csv.to_csv(file_path, index=False)
