# Created by erainm on 2025/7/19 00:26.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 字符串查找hello
"""
定义函数findall，要求返回符合要求的所有位置的起始下标，如字符串“helloworldhellopythonhelloc++hellojava”需要找出里面所有的“hello”的位置，返回的格式是一个元组，即：(0, 10, 21, 29)
"""

def findall(str_data, str_find):
    """
    :param str_data: 字符串
    :param str_find: 查找的字符串
    :return: 查找到的字符串的起始位置
    """
    start = 0
    result = []
    while True:
        index = str_data.find(str_find, start)
        if index == -1:
            break
        result.append(index)
        start = index + 1
    return tuple(result)

print(findall("helloworldhellopythonhelloc++hellojava", "hello"))