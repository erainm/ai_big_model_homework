# Created by erainm on 2025/7/18 22:26.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 元组拆包操作
# 请编写一个程序，定义一个元组student，包含学生的信息，包括姓名、年龄和性别。然后，使用元组拆包的方式将学生的信息提取出来，并分别存储到对应的变量中。最后，分别输出学生的姓名、年龄和性别。

def print_student_info(student):
    name, age, gender = student
    print("姓名：", name)
    print("年龄：", age)
    print("性别：", gender)
    print()
if __name__ == '__main__':
    student = ("张三", 18, "男")
    print_student_info(student)