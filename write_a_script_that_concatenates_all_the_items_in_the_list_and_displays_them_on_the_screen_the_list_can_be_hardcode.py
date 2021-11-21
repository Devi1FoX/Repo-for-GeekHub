chek_list = ['морква', 'картошка', 3, 1, 6]
def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(['морква', 'картошка', 3, 1, 6]))