#coding:utf-8
import numpy as np

#判断是否有负数
def check_state(num1,num2):
    if num1[0] == '-' and num2[0] == '-':
        r = "-" + longnum_added(num1[1:len(num1)],num2[1:len(num2)])
    elif num1[0] == '-':
        r = longnum_sub(num1[1:len(num1)],num2)
    elif num2[0] == '-':
        r = longnum_sub(num2[1:len(num2)],num1)
    else:
        r = longnum_added(num1,num2)
    return r

#负数加法
def longnum_sub(nega, posi):
    #分离整数和小数
    (I1,D1) = IntAndDec(nega)
    (I2,D2) = IntAndDec(posi)
    #小数部分
    no_deci = 0
    if D1 == "0" and D2 == "0":
        no_deci = 1
    max_length = max(len(D1),len(D2))
    D_sum = [0]*(max_length+1)
    if len(D1) > len(D2):
        for i in range(len(D1) - len(D2)):
            D2 += "0"
    else:
        for i in range(len(D2) - len(D1)):
            D1 += "0"
    D1 = list(D1)
    D2 = list(D2)
    lose = 0    #借位
    D_lose = 0
    for idx in range(max_length-1,-1,-1):
        temp1 = int(D1[idx])
        temp2 = int(D2[idx])
        
        temp2 -= lose
        if temp2 == -1:
            temp2 = 9
            D_lose = 1 #已经借位
        else:
            D_lose = 0
        
        temp_diff = temp2 - temp1
        
        if temp_diff < 0:
            D2[idx] = str(temp_diff+10)
            lose = 1
        else:
            D2[idx] = str(temp_diff)
            if D_lose == 0:
                lose = 0
    
    #整数部分
    max_length = max(len(I1),len(I2))
    #通过加0来使input长度相同
    I1 = I1.zfill(max_length)
    I2 = I2.zfill(max_length)
    
    #将input转化成list of char
    n1 = list(I1)
    n2 = list(I2)
    
    #sub each index of two input into ret
    for idx in range(max_length-1,-1,-1):
        temp1 = int(n1[idx])
        temp2 = int(n2[idx])

        temp2 -= lose
        if temp2 == -1:
            temp2 = 9
            D_lose = 1
        else:
            D_lose = 0
        
        
        temp_diff = temp2 - temp1
        
        if temp_diff < 0:
            n2[idx] = str(temp_diff + 10)
            lose = 1
        else:
            n2[idx] = str(temp_diff)
            if D_lose == 0:
                lose = 0
    
    #结果为负数的情况
    if lose == 1:
        ret = "-"
        for i in range(max_length):
            n2[i] = 9 - int(n2[i])
        #如果都为整数   
        if no_deci == 1:
            n2[max_length-1] = str(int(n2[max_length-1]) + 1)
            ret += ''.join(map(str,n2))
        else:
            for i in range(len(D2)):
                D2[i] = 9 - int(D2[i])
            D2[len(D2)-1] =str(int(D2[len(D2)-1]) + 1)
            ret = ret + ''.join(map(str,n2)) + '.'+ ''.join(map(str,D2))
    #结果为正数的情况
    else:
        if no_deci == 1:
            ret = ''.join(map(str,n2))
        else:
            ret = ''.join(map(str,n2))
            ret = ret + '.'+ ''.join(map(str,D2))
    if ret[0] == '0':
        ret = ret[1:len(ret)]
    if ret[0] == '-' and ret[1] == '0':
        ret = '-' + ret[2:len(ret)]
    return ret

#正整数加法
def longnum_added(num1,num2):
    """
    :type num1: string of numbers
    :type num2: string of numbers
    :rtype: str
    """
    #分离整数和小数
    (I1,D1) = IntAndDec(num1)
    (I2,D2) = IntAndDec(num2)
    #小数部分
    no_deci = 0
    if D1 == "0" and D2 == "0":
        no_deci = 1
    max_length = max(len(D1),len(D2))
    D_sum = [0]*(max_length+1)
    if len(D1) > len(D2):
        for i in range(len(D1) - len(D2)):
            D2 += "0"
    else:
        for i in range(len(D2) - len(D1)):
            D1 += "0"
    D1 = list(D1)
    D2 = list(D2)
    for idx in range(max_length-1,-1,-1):
        temp1 = int(D1[idx])
        temp2 = int(D2[idx])
        temp_sum = temp1 + temp2
        
        if temp_sum >= 10:
            D_sum[idx+1] += temp_sum - 10
            D_sum[idx] = 1
        else:
            if D_sum[idx+1] + temp_sum >= 10:
                D_sum[idx+1] += temp_sum - 10
                D_sum[idx] = 1
            else:
                D_sum[idx+1] += temp_sum
    
    #整数部分
    max_length = max(len(I1),len(I2))
    ret = [0]*(max_length+1)
    if D_sum[0] == 1:
        ret[max_length] = 1
    #通过加0来使input长度相同
    I1 = I1.zfill(max_length)
    I2 = I2.zfill(max_length)
    
    #将input转化成list of char
    n1 = list(I1)
    n2 = list(I2)

    #add each index of two input into ret
    for idx in range(max_length-1,-1,-1):
        #switch string into int
        temp1 = int(n1[idx])
        temp2 = int(n2[idx])
        temp_sum = temp1 + temp2
        
        if temp_sum >= 10:
            ret[idx+1] += temp_sum - 10
            ret[idx] = 1
        else:
            if ret[idx+1] + temp_sum >= 10:
                ret[idx+1] += temp_sum - 10
                ret[idx] = 1
            else:
                ret[idx+1] += temp_sum
    #结果与input数位相同
    if ret[0] == 0:
        ret = ret[1:max_length+1]
    
    ret = ''.join(map(str,ret))
    #有小数
    if no_deci == 0:
        ret = ret + '.'+ ''.join(map(str,D_sum[1:len(D_sum)]))
    return ret

#分离整数和小数
def IntAndDec(num):
    posn = num.find('.')
    if posn == -1:
        Inti = num
        Deci = "0"
    else:
        Inti = num[0:posn]
        Deci = num[posn+1:len(num)]
    return (Inti, Deci)
    
#Unit test
#假设输入的都是有效的非负整数，并且起始都不为0
str1 = "1000000000000000000000000000000000000000000"
str2 = "16000000000000000000000000"
ans = int(str1) + int(str2)
assert check_state(str1,str2) == str(ans)
str1 = "55555555555555555555555555555555555555555555"
str2 = "55555555555555555555555555555555555555555555"
ans = int(str1) + int(str2)
assert check_state(str1,str2) == str(ans)
#假设输入的都是有效的负整数
str1 = "-1000000000000000000000000000000000000000000"
str2 = "-16000000000000000000000000"
ans = int(str1) + int(str2)
assert check_state(str1,str2) == str(ans)
str1 = "-1234567890123456789012345678901234567890"
str2 = "-9876542123894289989248923489235393895994"
ans = int(str1) + int(str2)
assert check_state(str1,str2) == str(ans)
#假设输入的一个为正整数，一个为负整数
str1 = "11111111119999999999999994444444444444449999999999992"
str2 = "-3000000000444444444222222442"
ans = int(str1) + int(str2)
assert check_state(str1,str2) == str(ans)
str1 = "-11111111111111111111111111111111111111111111111111111"
str2 = "333333333333"
ans = int(str1) + int(str2)
assert check_state(str1,str2) == str(ans)
#假设输入的是正有理数,int（）无法转换小数点，所以我用比较直观的数字来检查
str1 = "111323.948"
str2 = "3233342.9438"
assert check_state(str1,str2) == "3344666.8918"
str1 = "999.999"
str2 = "88.8888"
assert check_state(str1,str2) == "1088.8878"
#假设输入的是负有理数
str1 = "-1111.22"
str2 = "-32323.34"
assert check_state(str1,str2) == "-33434.56"
str1 = "-99.22"
str2 = "-9.78"
assert check_state(str1,str2) == "-109.00"
#假设输入的是有正有负的有理数
str1 = "-10.933"
str2 = "20.84"
assert check_state(str1,str2) == "9.907"
str1 = "10.933"
str2 = "-19.04"
assert check_state(str1,str2) == "-8.107"
str1 = "100000000000000000000000000000000000000.99999999999999999999"
str2 = "-1000000000000000000000000000.99999999"
assert check_state(str1,str2) == "99999999999000000000000000000000000000.00000000999999999999"
