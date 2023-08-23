# 删除指定行
file_path = '../../files/txt-files/delete.txt'
lines_to_remove = [2, 4]


def remove_lines_from_file(file_path, lines_to_remove):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # 按行读出文件内容

    filtered_lines = [line for idx, line in enumerate(lines) if idx + 1 not in lines_to_remove]  # 过滤不删除的行
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)  # 将不删除的行重新写入文件


remove_lines_from_file(file_path, lines_to_remove)
