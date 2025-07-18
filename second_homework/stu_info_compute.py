# Created by erainm on 2025/7/18 22:54.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 学生信息计算
"""
题目描述
假设有一个学生信息列表，每个元素包含学生姓名、年龄和成绩。需要按照以下要求完成操作：
使用reverse()方法将列表反转。
使用sort()方法按照成绩从高到低对列表进行排序。
输出平均年龄和前三名学生的信息（姓名、年龄和成绩）。
提示：如果列表里面嵌套了元组，需要依据元组中的元素，对列表进行排序，可以参考如下代码。
    # 学生信息列表定义
    students = [('Alice', 20, 85), ('Bob', 19, 92), ('Catherine', 21, 78), ('David', 20, 95)]
    # 获取student中的第三个元素，例如：('Alice',20,85)获取85
        def get_score(student):
            return student[2]
    # 获取students列表中每个student元素，并使用get_score将每个学生中的分数拎出来，进students.sort(key=get_score,reverse=True)
"""
class StudentInfo(object):
    def __init__(self, students):
        self.students = students

    def reverse_students(self):
        self.students.reverse()
        return self.students

    @staticmethod
    def get_score(student):
        return student[2]

    def sort_students(self):
        self.students.sort(key=self.get_score, reverse=True)
        return self.students

    def print_students_info(self):
        for student in self.students[:3]:
            print("姓名：{}，年龄：{}，成绩：{}".format(student[0], student[1], student[2]))
        print("平均年龄：{}".format(sum(student[1] for student in self.students) / len(self.students)))


if __name__ == '__main__':
    students = [('Alice', 20, 85), ('Bob', 19, 92), ('Catherine', 21, 78), ('David', 20, 95)]
    student_info = StudentInfo(students)
    print("打印学生信息")
    print(student_info.students)
    print("打印学生信息反转")
    print(student_info.reverse_students())
    print("打印学生信息排序")
    print(student_info.sort_students())
    print("打印学生平均年龄和前三名学生信息")
    student_info.print_students_info()