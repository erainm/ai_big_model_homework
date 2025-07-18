# Created by erainm on 2025/7/18 23:34.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 购物车
"""
假设你正在开发一个在线商店的购物车功能，需要编写Python代码来处理购物车内的商品。请完成以下要求：
已知有一个购物车商品列表 cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]，其中每个元组表示一种商品及其数量。请使用列表推导式编写代码，实现以下功能：
创建一个新列表 cart_items，其中仅包含购物车中的商品名称（即去除商品数量信息）。
创建一个新列表 expensive_items，其中仅包含购物车商品数量>=3的商品名称。
将购物车中每个商品的数量加倍，并创建一个新的购物车列表 cart_doubled。
"""

class ShoppingCart(object):
    def __init__(self, cart):
        self.cart = cart
    def cart_items(self):
        return [item[0] for item in self.cart]

    def expensive_items(self):
        return [item[0] for item in self.cart if item[1] >= 3]

    def cart_doubled(self):
        return [(item[0], item[1]*2) for item in self.cart]

    def print_cart_info(self):
        print("购物车中的商品名称：", self.cart_items())
        print("购物车中数量>=3的商品名称：", self.expensive_items())
        print("购物车中商品数量加倍后的列表：", self.cart_doubled())

if __name__ == '__main__':
    cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]
    shopping_cart = ShoppingCart(cart)
    shopping_cart.print_cart_info()