import pandas as pd

old_file_path = '../../files/excel-files/read.xlsx'
file_path = '../../files/excel-files/edit.xlsx'

# 根据行索引修改指定列数据
excel_data = pd.read_excel(old_file_path, sheet_name='Fruits')
excel_data.at[0, 'Fruit'] = 'Apples'  # 替换第一行Fruit列的值
excel_data.at[2, 'Numbers'] = '22'  # 替换第三行Numbers列的值

excel_data.to_excel(file_path, sheet_name='Fruits', index=False)  # 将修改后的数据重新写入新的Excel文件

# 根据列索引修改所有行数据的值
excel_data = pd.read_excel(old_file_path, sheet_name='Fruits')
excel_data[3] = '1.6kg'

excel_data.to_excel(file_path, sheet_name='Fruits', index=False)

# 根据行列索引修改指定单元格数据
excel_data = pd.read_excel(old_file_path, sheet_name='Fruits')
excel_data.loc[2, excel_data.columns[1]] = '23'  # 替换第三行第二列单元格的值

excel_data.to_excel(file_path, sheet_name='Fruits', index=False)  # 将修改后的数据重新写入新的Excel文件
