# This problem was asked by Pinterest.
#
# The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order
# is an array representing whether each number is larger or smaller than the last. Given this information,
# reconstruct an array that is consistent with it. For example, given [None, +, +, -, +],
# you could return [1, 2, 3, 0, 4]

k = [None, '+', '+', '+', '-', '+' ]
lst = []
c = 0
for i in k:
    if i:
        c = eval(str(c)+i+'1')
        lst.append(c)
print(lst)


