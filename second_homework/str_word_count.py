# Created by erainm on 2025/7/19 00:53.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: 字符串字符统计模块

"""
功能：
    统计字符串中各字符的出现次数
示例：
    "hello world" → "h:1 e:1 l:3 o:2 d:1 r:1 w:1"
"""

def str_word_count(str_data):
    """
    统计字符串中每个字符的出现次数

    参数:
        str_data (str): 要统计的字符串

    返回:
        str: 格式化后的统计结果，格式为"字符:次数 ..."
    """
    str_data = str_data.replace(" ", "")
    str_dict = {}
    for char in str_data:
        str_dict[char] = str_dict.get(char, 0) + 1

    # 将字典转换为示例要求的格式
    return " ".join(f"{k}:{v}" for k, v in sorted(str_dict.items()))

if __name__ == '__main__':
    print(str_word_count("hello world"))