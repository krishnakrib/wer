def swapPosition(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[37,73,15,89]
pos1, pos2 = 1,3
print(swapPosition(list,pos1-1,pos2-1))
