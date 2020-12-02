'''
2048实现方法
'''

list_merge = [2, 2, 2, 0]
map = [
    [2, 0, 2, 0],
    [4, 4, 2, 0],
    [0, 4, 0, 4],
    [2, 2, 0, 4],
]


# 1.定义函数，将list_merge列表中的零元素移动到末尾
# 例如2 0 2 0 ——> 2 2 0 0
# 0 0 2 0   ——>2 0 0 0
# 0 0 2 0   ——>2 0 0 0
# 4 0 2 4   ——>4 2 4 0
# def move_zero_end(zero):
#     for k in range(len(zero) - 1):
#         for i in range(len(zero) - 1):
#             if zero[i] == 0:
#                 zero[i], zero[i + 1] = zero[i + 1], zero[i]
def move_zero_end():
    '''
    从后往前判断是否为0
    如果为0从列表删除，在列表最后添加一个0
    '''
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


def move_add():
    '''
    调用0向后移动函数
    判断相邻的两个数是否相同
    相同则合并
    '''
    move_zero_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] = list_merge[i] * 2
            del list_merge[i + 1]
            list_merge.append(0)
    # for i in range(len(zero) - 1):
    #     for k in range(i + 1, len(zero)):
    #         if zero[i] == zero[k]:
    #             zero[i] = zero[i] * 2
    #             del zero[k]
    #             zero.append(0)


def move_left():
    '''
    二维列表左移操作
    '''
    global list_merge  # 修改全局变量
    for i in map:  # 循环取出map列表的值
        list_merge = i  # 赋值到list_merge列表
        move_add()  # 进行相加


def move_right():
    '''
    二位列表向右移动操作。
    '''
    global list_merge
    for i in map:
        list_merge = i[::-1]  # 单个列表进行切片倒序
        move_add()  # 倒叙完成后进行相同且相邻数值的相加
        i[::-1] = list_merge  # 相加完成后再进行一个切片翻转


def list_matrix(par_matrix):
    '''
    二维列表斜角45度对折翻转，行变列，列变行
    '''
    for i in range(len(par_matrix)):
        for k in range(i, len(par_matrix)):
            par_matrix[i][k], par_matrix[k][i] = par_matrix[k][i], par_matrix[i][k]


def move_update():
    '''
    向上移动使用翻转函数进行翻转在进行向左移动操作，再进行翻转
    '''
    list_matrix(map)
    move_left()
    list_matrix(map)


def move_down():
    '''
    向上移动使用翻转函数进行翻转在进行向右移动操作，再进行翻转
    '''
    list_matrix(map)
    move_right()
    list_matrix(map)


move_update()
print(map)
