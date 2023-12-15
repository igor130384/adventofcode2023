path = 'input_2.txt'


def file_read(path):
    with open(path, 'r') as file:
        return file.readlines()


def sum_of_intervals():
    digit1 = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
              'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
              }
    file = file_read(path)
    list = []

    for str in file:
        list1 = []
        for k, v in enumerate(str):
            if v.isdigit():
                index = k
                list1.append((v, index))
        list2 = []
        for j in digit1.keys():
            if j in str:
                index = str.find(j)
                list2.append((digit1[j], index))

        result = (list1 + list2)
        sorted_data = sorted(result, key=lambda x: x[1])
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
                list.append((int(str1)))
        # with open('1.txt', 'w') as f:
        # for line in list:
        #     f.write('%s\n' % line)

    sum1 = sum(list)
    return list


print(sum_of_intervals())


# str = '8czmcdhonejzpsbpjgngdvtwotxczgsl6th36'
def count_substrings(string, substring):
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += len(substring)
    return count


string = "four2tszbgmxpbvninebxns6nineqbqzgjpmpqr"
substring = "nine"
print(count_substrings(string, substring))
