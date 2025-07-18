# Created by erainm on 2025/7/16 12:07.
# @Description: TODO：猴子吃桃问题
"""
题目猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个；第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了，第一天共摘了多少。
分析：
    摘了peaches个桃子        吃了的桃子                           剩余的桃子
    第一天：            peaches/2 + 1                       peaches - peaches/2 + 1
    第二天：            (peaches/2 +1)/2 + 1
    第三天：            ((peaches/2 +1)/2 + 1)/2 + 1
    第n天：                ……
    第10天：                                                   1个
"""
def monkey_eat_peaches():
    day = 9
    peaches = 1

    while day >= 1:
        peaches = (peaches + 1) * 2
        day -= 1
    print(f'第一天公摘了{peaches}个桃子')

if __name__ == '__main__':
    monkey_eat_peaches()