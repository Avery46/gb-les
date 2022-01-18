list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
a = 'Привет, {}!'
for item in list:
    print (a.format(list.split()[-1].title()))
#    name = list.split()[-1].title()
#    print('Привет, {}!'.format(name))

  


