import pandas as pd

file_path = '../../files/excel-files/read.xlsx'

# 依次按顺序读取每个worksheet的内容
excel_data = pd.read_excel(file_path, sheet_name=None)
print(excel_data)  # 打印出来是{}
for sheet_name, sheet_data in excel_data.items():  # 按Excel格式打印
    print(f'工作表名称：{sheet_name}')
    print(sheet_data)  # 按Excel格式打印，默认带行索引
    print(sheet_data.to_string(index=False))  # 按Excel格式打印，不带行索引
    print('-----------------------')

# 读取指定worksheet的内容
excel_data = pd.read_excel(file_path, sheet_name='Person')
print(excel_data)  # 按Excel格式打印，默认带行索引
print(excel_data.to_string(index=False))  # 按Excel格式打印，不带行索引
print(excel_data.to_string(index=False, header=False))  # 按Excel格式打印，不带行索引，不带header
print(excel_data.values)  # 打印出来是[['Rong' 29 'Female']], ['Gang' 30 'Male'], ['Xue' 26 'Female'], [['Peng' 22 'Male']]

# 根据行索引读取特定行
excel_data = pd.read_excel(file_path, sheet_name='Person')
specific_row = excel_data.iloc[1]  # 读取第二行内容
row_data = specific_row.to_string(index=False)
print(specific_row)  # 按Excel格式打印，打印出来会列索引
print(row_data)  # 按Excel格式打印，打印出来不带列索引

# 根据行标签读取特定行
excel_data = pd.read_excel(file_path, sheet_name='Person', index_col=0)
specific_row = excel_data.loc['Rong']  # 读取行标签为Rong的这一行
print(specific_row)

# 根据列索引读取特定列
excel_data = pd.read_excel(file_path, sheet_name='Person')
specific_col = excel_data.iloc[:, 1]  # 读取第二列内容
col_data = specific_col.to_string(index=False)
print(specific_col)  # 按Excel格式打印，打印出来会带行号索引
print(col_data)  # 按Excel格式打印，打印出来不带行号索引

# 根据列标签读取特定列
excel_data = pd.read_excel(file_path, sheet_name='Person')
specific_col = excel_data.loc[:, 'Age']  # 读取列标签为Age的这一列
col_data = specific_col.to_string(index=False)
print(specific_col)  # 按Excel格式打印，打印出来会带行号索引
print(col_data)  # 按Excel格式打印，打印出来不带行号索引

# 根据行索引和列索引读取指定单元格
excel_data = pd.read_excel(file_path, sheet_name='Person')
specific_cell = excel_data.iloc[0, 1]  # 读取第一行第二列的单元格内容
print(specific_cell)

# 根据行标签和列标签读取指定单元格
excel_data = pd.read_excel(file_path, sheet_name='Person', index_col=0)
specific_cell = excel_data.loc['Gang', 'Gender']
print(specific_cell)

