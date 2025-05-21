def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhập danh sách từ người dùng và xử lý chuỗi
input_list_str = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list_str.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ list:", my_tuple)