import pandas as pd

file_path = '../../files/excel-files/write.xlsx'
# 覆盖写入，仅有一个worksheet时
data = {
    'Name': ['Rong', 'Gang', 'Xue', 'Peng'],
    'Age': ['29', '30', '26', '22'],
    'Gender': ['Female', 'Male', 'Female', 'Male']
}

df = pd.DataFrame(data)
df.to_excel(file_path, sheet_name='Person', index=False)

# 覆盖写入，包含多个worksheet
data1 = {
    'Name': ['Rong', 'Gang', 'Xue', 'Peng'],
    'Age': ['29', '30', '26', '22'],
    'Gender': ['Female', 'Male', 'Female', 'Male']
}
data2 = {
    'Fruit': ['Apple', 'Strawberry', 'Orange'],
    'Numbers': ['10', '8', '6']
}

with pd.ExcelWriter(file_path) as writer:
    # 将data1写入第一个worksheet，Person
    df1 = pd.DataFrame(data1)
    df1.to_excel(writer, sheet_name='Person', index=False)
    # 将data2写入第二个worksheet，Fruits
    df2 = pd.DataFrame(data2)
    df2.to_excel(writer, sheet_name='Fruits', index=False)

# 在指定位置插入行数据
old_file_path = '../../files/excel-files/read.xlsx'
old_result = pd.read_excel(old_file_path, sheet_name='Person', index_col=False)

new_data = {
    'Name': ['Bo'],
    'Age': [51],
    'Gender': ['Male']
}
df_new = pd.DataFrame(new_data)
result = pd.concat([old_result.iloc[:1], df_new, old_result.iloc[1:]], ignore_index=True)  # 在第一行之后插入数据
print(result)
result.to_excel(file_path, sheet_name='Person', index=False)  # 将拼接好的数据写入新的Excel文件

# 在指定位置插入列数据
old_file_path = '../../files/excel-files/read.xlsx'
result = pd.read_excel(old_file_path, sheet_name='Person', index_col=False)

new_data = ['52kg', '100kg', '88kg', '65kg']
result.insert(2, 'Weight', new_data)  # 在第二列之后插入数据
print(result)
result.to_excel(file_path, sheet_name='Person', index=False)  # 将拼接好的数据写入新的Excel文件
