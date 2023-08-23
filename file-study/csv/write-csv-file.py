import pandas as pd

old_file_path = '../../files/csv-files/read.csv'
file_path = '../../files/csv-files/write.csv'

# 覆盖写入文件
data = {
    'Name': ['Rong', 'Gang', 'Xue', 'Peng'],
    'Age': ['29', '30', '26', '22'],
    'Gender': ['Female', 'Male', 'Female', 'Male']
}

df = pd.DataFrame(data)
df.to_csv(file_path, index=False)

# 在指定位置插入行数据
old_data = pd.read_csv(old_file_path)
new_data = {
    'Fruit': ['Purple'],
    'Numbers': ['13'],
    'Color': ['Pur'],
    'Weight': ['10kg'],
    'Price': ['¥6']
}
df_new = pd.DataFrame(new_data)
result = pd.concat([old_data.iloc[:3], df_new, old_data.iloc[3:]], ignore_index=True)  # 在第三行之后插入行数据
print(result)
result.to_csv(file_path, index=False)

# 在指定位置插入列数据
old_data = pd.read_csv(old_file_path)
new_data = ['100', '90', '80', '70', '60', '50', '40', '30']
df_new = pd.DataFrame(new_data)

old_data.insert(5, 'Score', df_new)
old_data.to_csv(file_path, index=False)
