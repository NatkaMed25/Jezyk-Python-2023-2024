def sum_seq(sequence):
    result = 0

    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        else:
            result += item

    return result

seq = [1, 2, [], [4], (1,2), [3,4], (5,6,7)]
print('Suma sekwencji =', sum_seq(seq))