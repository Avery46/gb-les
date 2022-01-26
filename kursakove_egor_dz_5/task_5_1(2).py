


def odd_num(to):
    for i in range(1, to + 1, 2):
        yield i

def odd_num_no_yield(to):
    return (x for x in range(1, to + 1, 2))

first = odd_num(int(input()))
for elem in first:
        print(elem)