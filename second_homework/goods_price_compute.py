# Created by erainm on 2025/7/18 22:38.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 商品价格计算
"""
假设存在一个名为“prices”的列表，其中每个元素代表一个商品的价格。需要完成以下任务：
    将价格列表按升序排序。
    将价格列表反转，得到降序排序的列表。
    找到最高价格和最低价格。
    计算所有商品的平均价格。
"""
class GoodsPriceCompute(object):
    def __init__(self, prices):
        self.prices = prices
    # 升序排序价格列表
    def sort_prices(self):
        return sorted(self.prices)
    # 反转升序后的价格列表，得到降序排序的列表
    def reverse_prices(self):
        return self.sort_prices()[::-1]
    # 找到最高价格和最低价格
    def find_max_min_price(self):
        return min(self.prices), max(self.prices)
    # 计算所有商品的平均价格
    def calculate_average_price(self):
        return sum(self.prices) / len(self.prices)

if __name__ == '__main__':
    prices = [10.2, 9.5, 5, 8, 12.2, 712, 1.2, 0.5, 0.1]
    compute = GoodsPriceCompute(prices)
    print("价格列表：", prices)
    print("按升序排序后的价格列表：", compute.sort_prices())
    print("反转后降序的价格列表：", compute.reverse_prices())
    print("最高价格和最低价格：", compute.find_max_min_price())
    print("平均价格：", compute.calculate_average_price())