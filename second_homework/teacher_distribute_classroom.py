# Created by erainm on 2025/7/19 00:30.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 使用列表嵌套，完成8名老师随机分配3个办公室
"""
提示：
    定义一个列表存放8位老师
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']，
    定义一个列表用来保存3个办公室offices = [[], [], []]
"""
import random

def teacher_distribute_classroom():
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    offices = [[], [], []]

    # 先确保每个办公室至少有1名老师
    for office in offices:
        teacher = random.choice(names)
        office.append(teacher)
        names.remove(teacher)

    # 剩余老师随机分配
    for name in names:
        office_idx = random.randint(0, 2)
        offices[office_idx].append(name)
    return offices

if __name__ == '__main__':
    result = teacher_distribute_classroom()
    for i, office in enumerate(result, 1):
        print(f"办公室{i}的老师：{office}")