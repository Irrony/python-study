import pandas as pd

old_file_path = '../../files/csv-files/read.csv'
file_path = '../../files/csv-files/edit.csv'

# 根据行索引修改列名对应单元格的值
csv = pd.read_csv(old_file_path)
csv.at[2, 'Weight'] = '1.5kg'  # 修改第三行Weight列的单元格值
csv.at[4, 'Numbers'] = '21'  # 修改第五行Numbers列的单元格值
csv.to_csv(file_path, index=False)

# 根据列索引修改所有行数据的值
csv = pd.read_csv(old_file_path)
csv[csv.columns[3]] = '1.6kg'  # 将所有行的第四列的值均改为1.6kg

# 根据行列索引修改指定单元格数据
csv = pd.read_csv(old_file_path)
csv.at[2, csv.columns[3]] = '1.6kg'  # 只将第三行第四列的值改为1.6kg
csv.to_csv(file_path, index=False)
