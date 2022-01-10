# def SwapList(NewList):
#     size = len(NewList)
#
#     temp = NewList[0]
#     NewList[0] = NewList[size - 1]
#     NewList[size - 1] = temp
#     return NewList
#
#
# InputList = [40, 10, 20, 50, 5]
# print(SwapList(InputList))

# def SwapList(NewList):
#     first = NewList.pop(0)
#     last = NewList.pop(-1)
#
#     NewList.insert(0, last)
#     NewList.append(first)
#
#     return NewList
#
#
# List = list(map(int, input().split()))
# print(SwapList(List))

def Swap(List, pos1, pos2):
    first = List.pop(pos1)
    last = List.pop(pos2-1)

    List.insert(pos1, last)
    List.insert(pos2, first)
    return List


L = [1, 2, 3, 4]
pos1, pos2 = 1, 3
print(Swap(L, pos1-1, pos2-1))
