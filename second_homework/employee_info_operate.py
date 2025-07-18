# Created by erainm on 2025/7/18 23:21.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 员工信息操作
"""
某个公司的员工信息以字典形式存储，键为员工的工号，值为包含姓名、年龄和职位的字典。现在，你需要编写一个程序来完成对员工信息的增删改查操作。

要求
    查询：根据给定的员工工号，从字典中查找对应员工的信息，并返回员工的姓名、年龄和职位。
    增加：将给定的员工信息添加到字典中。
    删除：根据给定的员工工号，从字典中删除对应的员工信息。
已知有如下员工
    employee_records['1001'] = {'name': 'Alice', 'age': 25, 'position': 'Manager'}
    employee_records['1002'] = {'name': 'Bob', 'age': 30, 'position': 'Engineer'}
"""
class EmployeeInfo(object):
    def __init__(self, employee_records):
        self.employee_records = employee_records
    def query_employee(self, employee_id):
        return self.employee_records.get(employee_id)
    def add_employee(self, employee_id, employee_info):
        self.employee_records[employee_id] = employee_info
    def delete_employee(self, employee_id):
        if employee_id in self.employee_records:
            del self.employee_records[employee_id]

    def print_employees(self):
        for employee_id, employee_info in self.employee_records.items():
            print(f"员工工号：{employee_id}")
            print(f"员工姓名：{employee_info['name']}")
            print(f"员工年龄：{employee_info['age']}")
            print(f"员工职位：{employee_info['position']}")
            print("-" * 20)

if __name__ == '__main__':
    employee_records = {
        '1001': {'name': 'Alice', 'age': 25, 'position': 'Manager'},
        '1002': {'name': 'Bob', 'age': 30, 'position': 'Engineer'}
    }
    employee_info = EmployeeInfo(employee_records)
    print("查询员工信息：")
    print(employee_info.query_employee('1001'))
    print("增加员工信息：")
    employee_info.add_employee('1003', {'name': 'erainm', 'age': 34, 'position': 'Engineer'})
    employee_info.print_employees()
    print("删除员工信息：")
    employee_info.delete_employee('1002')
    employee_info.print_employees()
    print("打印所有员工信息：")
    employee_info.print_employees()