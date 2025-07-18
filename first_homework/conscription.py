# Created by erainm on 2025/7/16 11:05.
# @Description: TODO 征兵

"""
【征兵标准】
性别要求：征收男兵
身高标准：男性160cm以上，女性158cm以上。
男性体重：男性不超过90kg，不低于60kg。
视力标准：右眼裸眼视力不低于4.6，左眼裸眼视力不低于4.5
"""
class Conscription(object):
    def __init__(self,gender,height,weight,right_eye,left_eye):
        # 初始化征兵人员属性
        # 初始化征兵人员属性
        if gender not in ('男', '女'):
            raise ValueError("性别必须为'男'或'女'")
        if height <= 0:
            raise ValueError("身高必须为正数")
        if weight <= 0:
            raise ValueError("体重必须为正数")
        if not (0.0 <= right_eye <= 5.0):
            raise ValueError("右眼视力必须在0.0到5.0之间")
        if not (0.0 <= left_eye <= 5.0):
            raise ValueError("左眼视力必须在0.0到5.0之间")

        self.gender = gender
        self.height = height
        self.weight = weight
        self.right_eye = right_eye
        self.left_eye = left_eye
        self.reasons = [] #用于存储不符合标准的原因

    def check_gender(self):
        # 检查性别是否符合标准
        if self.gender.strip() != '男':
            self.reasons.append("只招收男兵")
            return False
        return True

    def check_height(self):
        # 检查身高是否符合标准
        if self.gender.strip() == "男" and self.height < 160:
            self.reasons.append("男性身高不足160cm")
            return False
        return True

    def check_weight(self):
        # 检查体重是否符合标准
        if self.gender.strip() == '男':
            if  self.weight > 90:
                self.reasons.append("男性体重大于90kg")
                return False
            if self.weight < 60:
                self.reasons.append("男性体重小于60kg")
                return False
        return True

    def check_vision(self):
        # 检查左眼视力
        if  not isinstance(self.left_eye, (int, float)) or self.left_eye < 4.5:
            self.reasons.append("左眼视力低于4.5")
            return False
        # 检查右眼视力
        if not isinstance(self.right_eye, (int, float)) or  self.right_eye < 4.6:
            self.reasons.append("右眼视力低于4.6")
            return False
        return True

    """
    检查是否满足征兵标准
    该方法会执行一系列检查来判断是否满足征兵条件，包括性别、身高、体重和视力检查。
    Returns:
        tuple: 包含两个元素的元组
            - bool: 是否满足所有征兵标准(True表示满足，False表示不满足)
            - list: 如果不满足，包含不满足的原因列表；如果满足，包含"符合所有征兵标准"信息
    """
    def is_qualified(self):
            self.reasons = []
            # 所有检查
            checks = [
                self.check_gender(),  # 检查性别是否符合标准
                self.check_height(),  # 检查身高是否符合标准
                self.check_weight(),  # 检查体重是否符合标准
                self.check_vision()   # 检查视力是否符合标准
            ]
            if all(checks):
                return True,["符合所有征兵辨准"]
            else:
                return False,self.reasons

if __name__ == '__main__':
    # 创建征兵人员对象
    recruit1 = Conscription('男',165,70,4.8,4.7)
    result = recruit1.is_qualified()
    print(f'应征者1:{result}')

    recruit2 = Conscription('男', 158, 95, 4.5, 4.4)
    result = recruit2.is_qualified()
    print(f'应征者2:{result}')



