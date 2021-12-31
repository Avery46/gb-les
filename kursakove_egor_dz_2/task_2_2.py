#list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#i = 0
#for i in range (len(list)):
#   if list[i] 
#
#message = ''
#for item in list:
#   message += item 
#   message += ' '
#print(message) 
#
def temp(x):
    if x[0] in '+-':
        return x[0]

list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(list):
    newtemp = temp(list[i])
    if list[i].isdigit() or (newtemp and list[i][1:].isdigit()):
        if newtemp:
            list[i] = newtemp + list[i][1:].zfill(2)
        else:
            list[i] = list[i].zfill(2)
        list.insert(i, '"')
        list.insert(i + 2, '"')
        i += 2

    i += 1

message = ''
for item in list:
   message += item 
   message += ' '
print(message) 
