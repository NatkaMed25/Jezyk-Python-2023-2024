seq1 = [1, 65, 2, 3, 'kot', 89, 'kura', 7, 33, 'abc']
seq2 = [33, 2, 'abc', 3, 71, 'kot', 'pies', 15, 7, 'kwiatek']

common_elements = list(set(seq1) & set(seq2))
all_elements = list(set(seq1) | set(seq2))

print('Elementy wspólne:', common_elements)
print('Wszystkie elementy bez powtórzeń:', all_elements)