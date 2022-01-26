src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
   
   
def func(*argv):
    ans = set()
    for elem in argv:
        if not elem in ans:
            ans.add(elem)
        else:
            ans.remove(elem)
 
    return [x for x in argv if x in ans] 

r = func(*src)
print(r)