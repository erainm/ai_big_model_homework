# Created by erainm on 2025/7/18 23:47.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 用户信息录入文本
"""
请编写一个程序，实现将用户输入的信息写入文本文件中。
首先，程序需要提示用户输入姓名、年龄和性别。
然后，程序将用户输入的信息写入文本文件中。文本文件的路径为output.txt，如果文件不存在，则创建新文件；如果文件已存在，则覆盖原有内容。
最后，程序输出写入完成后的提示信息，例如“写入完成！”。
你需要编写完整的代码来实现上述功能。
"""
class UserInfoEnterTxt(object):
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
    def get_user_info(self):
        self.name = input("请输入姓名：")
        self.age = input("请输入年龄：")
        self.gender = input("请输入性别：")

    def write_user_info_to_txt(self):
        with open("../file/output.txt", "w") as f:
            f.write("姓名：" + self.name + "\n")
            f.write("年龄：" + self.age + "\n")
            f.write("性别：" + self.gender + "\n")
        print("写入完成！")

if __name__ == '__main__':
    user_info_enter_txt = UserInfoEnterTxt()
    user_info_enter_txt.get_user_info()
    user_info_enter_txt.write_user_info_to_txt()