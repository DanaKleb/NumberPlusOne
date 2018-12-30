s = "anagram"
t = "nagaram"
result = 0
for i in s:
    for j in t:
        if i==j:
            result += 1
            t = t.replace("i","")
            break
if result == len(s) and result == len(t):
    print ("true")
else:
    print ("false")

s ="anagram"
t = "nagaram"
outcome = [(i,j) for i in s for j in t if i==j and len(s) == len (t)]
print(outcome)


# number + 1
def numberPlusOne(lst):
    if lst[-1] < 9:
        num = [s if i < (len(lst)-1) else s+1 for (i,s) in enumerate(lst)]
    elif lst [-1] == 9:
        num = "".join(reversed(lst))
    return (num)

print (numberPlusOne([5,9,3,9,9]))

