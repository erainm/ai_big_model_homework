# Created by erainm on 2025/7/18 23:39.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 文件读取每一行

def file_read():
    with open("../file/python.txt", "r") as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    file_read()