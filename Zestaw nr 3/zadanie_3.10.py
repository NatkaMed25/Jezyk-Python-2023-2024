def roman2int(roman_num):
    roman_to_arabic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    final_num = 0
    temp= 0

    for num in roman_num:
        arabic = roman_to_arabic[num]
        if arabic > temp:
            final_num += arabic - 2 * temp
        else:
            final_num += arabic
        temp = arabic
    
    return final_num

print('DCXLVI =', roman2int('DCXLVI'))
print('XXVII =', roman2int('XXVII'))
print('MMCDIII =', roman2int('MMCDIII'))
print('MCCLXV =', roman2int('MCCLXV'))
print('X =', roman2int('X'))