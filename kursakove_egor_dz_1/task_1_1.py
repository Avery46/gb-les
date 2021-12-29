minute = 60
hour = 3600
day = 86400
week = 604800
month = 2678400
year = 31536000

duration = int (input('Укажите кол-во секунд: '))
# до минуты
if duration<minute:
    print ('{} сек'.format(duration))

# до часа
elif minute <= duration and hour > duration:
    new_minute=duration//minute
    new_sec=duration%minute
    print ('{} мин {} сек'.format(new_minute,new_sec));

# до дня
elif hour <= duration and duration < day:
    new_hour=duration // hour
    duration=duration % hour
    new_minute = duration // minute
    new_sec = duration % minute
    print ('{} час {} мин {} сек'.format(new_hour,new_minute,new_sec));
# до недели

elif duration >= day and duration < week:
    new_day = duration // day
    duration=duration % day
    new_hour = duration // hour
    duration = duration % hour
    new_minute = duration // minute
    new_sec = duration % minute
    print('{} дн {} час {} мин {} сек'.format(new_day, new_hour, new_minute, new_sec));
# до месяца

elif duration >= week and duration < month:
    new_week = duration // week
    duration=duration % week
    new_day = duration // day
    duration=duration % day
    new_hour = duration // hour
    duration = duration % hour
    new_minute = duration // minute
    new_sec = duration % minute
    print('{} нед {} дн {} час {} мин {} сек'.format(new_day, new_hour, new_minute, new_sec));
# до года

elif duration >= month and duration < year:
    new_week = duration // week
    duration=duration % week
    new_day = duration // day
    duration = duration % day
    new_hour = duration // hour
    duration = duration % hour
    new_minute = duration // minute
    new_sec = duration % minute
    print('{} нед {} дн {} час {} мин {} сек'.format(new_week, new_day, new_hour, new_minute, new_sec));
# до года

elif duration >= year:
    new_year=duration // year
    duration = duration % year
    new_week = duration // week
    duration=duration % week
    new_day = duration // day
    duration = duration % day
    new_hour = duration // hour
    duration = duration % hour
    new_minute = duration // minute
    new_sec = duration % minute
    print('{} год {} нед {} дн {} час {} мин {} сек'.format(new_year, new_week, new_day, new_hour, new_minute, new_sec)); 

    
    cubes = [x**3 for x in range (100) if  x%2 != 0 ]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list=[]


for i in range(len(cubes)):
  
    my_str = str(cubes[i])
    my_list = list(my_str)
  
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
   
    
    my_numbers_sum = sum(my_list)
    print(my_numbers_sum)
    
    if my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list.append(my_numbers_sum)

print('Список чисел, делящихся на 7: ',my_numbers_sum_list)



for i in range(100):
    new_str=str(i+1)
    new_list = list(new_str)
    if int(new_list[-1])==1 and i+1!=11:
        print('{} процент'.format(i + 1))
    elif int(new_list[-1])>1 and int(new_list[-1])<= 4:
        if  i+1> 10 and i+1<= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))

