# Created by erainm on 2025/7/18 22:31.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 打印人员信息
"""
请编写一个函数print_info，接受以下参数：

    name：表示一个人的姓名（必须）
    age：表示一个人的年龄（必须）
    city：表示一个人所在的城市（可选，默认值为“未知”）
    gender：表示一个人的性别（可选，默认值为“未知”）
    函数内部根据提供的参数打印人物信息，输出格式如下：
    姓名：xxx
    年龄：xxx
    城市：xxx
    性别：xxx
"""

def print_info(name, age, city="未知", gender="未知"):
    print("姓名：", name)
    print("年龄：", age)
    print("城市：", city)
    print("性别：", gender)
    print()

if __name__ == '__main__':
    print_info("张三", 18)
    print_info("李四", 19, "武汉", "男")