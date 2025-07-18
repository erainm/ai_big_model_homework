# Created by erainm on 2025/7/18 22:35.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 写一个lambda表达式，用于将字符串列表中的字符串都转换为大写

def str_to_upper(str_list):
    return list(map(lambda a: a.upper(), str_list))

if __name__ == '__main__':
    print(str_to_upper(["hello", "world"]))
