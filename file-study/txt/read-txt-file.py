# 整体读取.txt文件
file_path = '../../files/txt-files/read.txt'
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

# 逐行读取.txt文件
file_path = '../../files/txt-files/read.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)


# 读取.txt文件的首行
file_path = '../../files/txt-files/read.txt'
with open(file_path, 'r') as file:
    first_line = file.readline()
    print(first_line)

# 读取.txt文件的末行
file_path = '../../files/txt-files/read.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()
    last_line = lines[-1].strip()  # 去除行尾的换行符和空格
    print(last_line)


# 读取.txt文件的特定行
def read_specific_line(file_path, line_number):
    with open(file_path, 'r') as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == line_number:
                return line.strip()
    return None


file_path = '../../files/txt-files/read.txt'
line_number = 3

specific_line = read_specific_line(file_path, line_number)
if specific_line is not None:
    print(specific_line)
else:
    print('The line is not exist.')
