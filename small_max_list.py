#!/usr/bin/env python
#-*-coding:utf-8-*-
i=[0]
def mean(sorted_list):

    i[0] = i[0]+1
    if not sorted_list:
        return (([],[]))
    big = sorted_list[-1]
    small = sorted_list[-2]
    print i,big,small,sorted_list
    big_list,small_list = mean(sorted_list[:-2])
    big_list.append(small)
    small_list.append(big)
    big_list_sum = sum(big_list)
    small_list_sum = sum(small_list)
    if big_list_sum > small_list_sum:
        print i,sorted_list,big_list,small_list
        return ((big_list,small_list))
    else:
        print i,sorted_list,big_list,small_list
        return ((small_list,big_list))





if __name__ == "__main__":
    tests=[1,2,3,4,5,6,7,8,9,10]
    print  mean(tests)


