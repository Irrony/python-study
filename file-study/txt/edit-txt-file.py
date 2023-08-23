def wirte_init_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


# 替换指定文本
def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()
    new_content = content.replace(old_text, new_text)
    with open(file_path, 'w') as file:
        file.write(new_content)


file_path = '../../files/txt-files/edit.txt'
content = 'My name is Rong.\nMy age is 29.\nI am a girl.'
old_text = '29'
new_text = '18'

wirte_init_file(file_path, content)
replace_text_in_file(file_path, old_text, new_text)


# 替换指定行文本为新内容
def replace_text_in_line(file_path, line_number, new_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_text + '\n'
        with open(file_path, 'w') as file:
            file.writelines(lines)
        return True
    else:
        return False


file_path = '../../files/txt-files/edit.txt'
content = 'My name is Rong.\nMy age is 29.\nI am a girl.'
line_number = 3
new_text = 'I am not a boy.'


wirte_init_file(file_path, content)
replace_text_in_line(file_path, line_number, new_text)
