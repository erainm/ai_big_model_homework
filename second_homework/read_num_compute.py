# Created by erainm on 2025/7/19 00:12.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 从文本中读取数值并计算
"""
请编写一个程序，实现从文本文件中读取数据，并进行简单的处理和输出。
    1. 首先，程序需要从文本文件中读取一串数字，每个数字占据一行。文本文件的名称为numbers.txt。
    2. 然后，程序需要将读取到的数字进行累加求和，并输出求和结果。
注意：
    · 文本文件中的每行只包含一个整数。
    · 文件中的数字可能有正数、负数或零。
"""

class FileRead(object):
    def __init__(self):
        self.sum = 0
    def file_read(self):
        with open("../file/number.txt", "r") as f:
            for line in f:
                num = int(line.strip())
                self.sum += num
        print("The sum of numbers in the file is:", self.sum)

if __name__ == '__main__':
    file_read = FileRead()
    file_read.file_read()