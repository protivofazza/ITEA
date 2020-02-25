# P1
n = int(input())

lst = [i for i in range(0, n+1)]

for i in lst:
    if not (i % 2):
        print(i)


# P2
country_list = ['Ukraine', 'USA', 'Canada', 'Japan']

country_dict = {
    'Ukraine': 'Kyiv',
    'Russia': 'Moscow',
    'Japan': 'Tokyo',
    'UK': 'London'
}

for i in country_list:
    if i in country_dict:
        print(country_dict[i])


# P3
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)


# P4
def bank(money_sum, duration, percent):
    return money_sum*(1 + duration*percent/100)


print(bank(1000, 2, 10))
