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

    

