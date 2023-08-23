import pandas as pd

old_file_path = '../../files/excel-files/read.xlsx'
file_path = '../../files/excel-files/delete.xlsx'

excel_data = pd.read_excel(old_file_path, sheet_name='Person')
data = pd.DataFrame(excel_data)

# 根据行索引删除数据
result = data.drop(1)  # 删除第二行数据
result.to_excel(file_path, sheet_name='Person', index=False)

# 根据列索引删除数据
result = data.drop(excel_data.columns[2], axis=1)  # 删除第三列数据
result.to_excel(file_path, sheet_name='Person', index=False)

# 根据列标签删除数据
result = data.drop('Gender', axis=1)  # 删除Gender列数据
result.to_excel(file_path, sheet_name='Person', index=False)

# 根据行列索引删除指定单元格数据
excel_data.loc[1, excel_data.columns[2]] = None  # 删除第二行第三列的单元格数据
excel_data.to_excel(file_path, sheet_name='Person', index=False)

