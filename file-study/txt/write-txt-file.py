# 直接写入.txt文件，会替换原有文本
file_path = '../../files/txt-files/write.txt'
content = 'My name is Rong.\nMy age is 29.\nI am a girl.'  # \n为换行符
with open(file_path, 'w') as file:
    file.write(content)

# 追加新文本到.txt文件（会在原有文本最后不换行，直接添加新文本）
file_path = '../../files/txt-files/write.txt'
content = 'This is additional words.'
with open(file_path, 'a') as file:
    file.write(content)

# 追加新文本到.txt文件（会在原有文本最后进行换行，然后添加新文本）
file_path = '../../files/txt-files/write.txt'
content = 'This is newline words.'
with open(file_path, 'a') as file:
    file.write('\n' + content)

# 逐行将列表内容追加到.txt文件最后
file_path = '../../files/txt-files/write.txt'
Lines = ['This is line1', 'This is line2', 'This is line3']
with open(file_path, 'a') as file:
    for line in Lines:
        file.write('\n' + line)

# 在特定行之前插入新文本
def insert_text_before_line(file_path, line_number, new_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines.insert(line_number - 1, new_text + '\n')
    with open(file_path, 'w') as file:
        file.writelines(lines)


file_path = '../../files/txt-files/write.txt'
line_number = 2
new_text = 'This is the middle line before.'

insert_text_before_line(file_path, line_number, new_text)


# 在特定行之后插入新文本
def insert_text_after_line(file_path, line_number, new_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines.insert(line_number, new_text + '\n')
    with open(file_path, 'w') as file:
        file.writelines(lines)


file_path = '../../files/txt-files/write.txt'
line_number = 2
new_text = 'This is the middle line after.'

insert_text_after_line(file_path, line_number, new_text)