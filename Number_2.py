digit = ['one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5',
         'six', '6', 'seven', '7', 'eight', '8', 'nine', '9'
         ]
digit1 = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
          'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
          }

stroki = []
with open('input_2.txt', 'r') as file:
    for i in file:
        stroki.append(i)


def digit(file):
    digit = ['one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5',
             'six', '6', 'seven', '7', 'eight', '8', 'nine', '9'
             ]
    digit1 = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
              'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
              }

    d = []

    for str in file:
            a = []
            for j in digit:
                if j in str:
                    index = str.find(j)
                    if j.isdigit():
                        a.append((j, index))
                    else:
                        a.append((digit1[j], index))
            sorted_data = sorted(a, key=lambda x: x[1])
            if len(sorted_data) == 0:
                sorted_data = sorted_data
            elif len(sorted_data) == 1:
                sorted_data = sorted_data * 2
            else:
                sorted_data = sorted_data[:len(sorted_data):len(sorted_data) - 1]
            str1 = ''
            for i in sorted_data:
                str1 += i[0]
                if len(str1) >= 2:
                    d.append(int(str1))

    return d


print(digit(stroki))

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

#   29, 83, 13, 24, 42, 14, 76.
# Adding these together produces 281.
