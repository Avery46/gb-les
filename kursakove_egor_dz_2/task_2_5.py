prices = [90, 23.3, 10.88, 65, 332.8, 122, 498.57, 200,
          159.99, 88]


def prices_show(list_prices):
    for i in range(len(list_prices)):
        price = str(float(list_prices[i]))
        price = price.split('.')
        price = f'{int(price[0]):.0f} руб {int(price[1]):02d} коп'
        print(price, end='')
        if i != len(prices) - 1:
            print(end=', ')
    print(end='\n')

print('1:')
prices_show(prices)

print('2:')
prices_show(prices)
print('Доказательство: id объекта до сортировки:', id(prices))
prices.sort()
prices_show(prices)
print('Доказательство: id объекта после сортировки:', id(prices))

print('3:')
new_prices = sorted(prices, reverse=True)
prices_show(new_prices)

print('4:')
new_prices = new_prices[:5]
prices_show(new_prices)