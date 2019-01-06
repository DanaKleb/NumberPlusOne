#comparing string, "compare_to" will be the base
compare_to = "eolr"
word = "rore"
new_list = [i for i in compare_to if any (j in word for j in i if i in j)]
result = 'true' if len(word) == len(compare_to) and (len(new_list) >= len(word) and len(new_list) >= len(compare_to)) else 'false'
print(result)

#Greek numbers
ints = [1,5,10,50,100,1000]
nums = ['I','V','X','L','C','M']
def Greek_numbers(str):
    val = 0
    # for x in str:
    #     if x == 'I':
    #         val += 1
    #         continue
    #     elif x == 'V':
    #         val += 5
    #         continue
    #     elif x == 'X':
    #         val += 10
    #     elif x == 'L':
    #         val += 50
    #     elif x == 'C':
    #         val += 100
    #     elif x == 'M':
    #         val += 1000
    return val

# print (Greek_numbers('LXVI'))

# number + 1
def numberPlusOne(lst):
    if lst[-1] < 9:
        num = [s if i < (len(lst)-1) else s+1 for (i,s) in enumerate(lst)]
    elif lst[-1] == 9:
        if lst[-2] == 9:
            num = [0 if s == 9 and i == (len(lst) - 2) else 0 if s == 9 and i == (len(lst) - 1) else s + 1 if i == (len(lst) - 3) else s for (i, s) in enumerate(lst)]
        else:
            num = [0 if s== 9 and i == (len(lst)-1) else s+1 if i==(len(lst)-2) else s for (i,s) in enumerate(lst)]
    return (num)

print (numberPlusOne([5,0,9]))



