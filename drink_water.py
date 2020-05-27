# 你现在有20瓶水，两个空瓶子可以换一瓶水，三个瓶盖可以换一瓶水。
# 求最多能喝多少瓶水？

# while循环实现：


def while_solution(water_bottles):      # water_bottles 是有水的瓶子数量
    caps = 0                            # 瓶盖数量
    bottles = 0                         # 空瓶子数量
    drunk_water = 0                     # 喝过的水的瓶数
    while water_bottles > 0:            # 在有水可以喝的情况下，一直循环
        drunk_water += water_bottles    # 喝水
        caps += water_bottles           # 产生瓶盖
        bottles += water_bottles        # 产生空瓶子
        water_bottles = 0               # 喝掉了所有有水的瓶子

        water_bottles += bottles // 2   # 空瓶换新水瓶
        bottles = bottles % 2           # 消耗空瓶后剩下余数个空瓶

        water_bottles += caps // 3      # 瓶盖换新水瓶
        caps = caps % 3                 # 消耗瓶盖后剩下余数个瓶盖

    print(f"喝了{drunk_water}瓶水")     # 输出喝了多少水


while_solution(20)

# 递归实现：


def drink(water, caps, bottles):            # 参数含义和while循环的实现基本相同
    water += caps // 3                      # 瓶盖换水
    caps = caps % 3                         # 留下余数个瓶盖
    water += bottles // 2                   # 空瓶换水
    bottles = bottles % 2                   # 留下余数个空瓶
    if water == 0:                          # 无水可喝，是递归的终点
        return 0
    caps += water                           # 产生瓶盖
    bottles += water                        # 产生空瓶
    return water + drink(0, caps, bottles)  # 总的喝水数量是现在的水加上喝完以后能喝的水


print(f"喝了{drink(20, 0, 0)}瓶水")         # 输出喝了多少水


# 尽管递归算法代码比while循环实现少了几行，
# 但是递归算法在递归调用时需要压栈，
# 因此受到python的最大调用堆栈限制（最多1000层调用栈）。
# 所以，递归算法无法处理过大的数据，例如一开始有2**1000瓶水。
# 下面的代码将会产生RecursionError异常（递归错误）：

# print(f"喝了{drink(2 ** 1000, 0, 0)}瓶水")

# 但是，循环实现的算法不会产生这样的异常，并且也能正常输出结果。
while_solution(2 ** 1000)
# 因此，在能使用循环实现的情况下，应当尽量选择循环/迭代实现。
# 适合用递归算法实现的问题是：
# 在进行分解时具有多个相同（或相似）的子问题的问题（例如典型的汉诺塔问题，就有两个移动子塔的子问题）。
# 而本题只有一个子问题（用剩下的材料换水），因此递归算法可以直接退化成循环/迭代算法。
