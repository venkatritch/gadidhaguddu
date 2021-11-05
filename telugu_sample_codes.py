# e42:
# first program

n = 10
చూపించు(n)
m = 10
k = n + m + 5
చూపించు("k:", k)


# e42:
# second program

def చూపించు_n_varaku(n):
    number = 1
    అయ్యేవరకు(number <= n):
        చూపించు(number)
        number += 1


n = 10
చూపించు_n_varaku(n)
