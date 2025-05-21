def kiem_tra_so_nguyen_to(n):
    if n < 2:  # Số nguyên tố phải lớn hơn 1
        return False
    for i in range(2, int(n ** 0.5) + 1): # Chỉ cần kiểm tra đến căn bậc hai của n
        if n % i == 0:
            return False # Nếu tìm thấy ước số, không phải là số nguyên tố
    return True # Nếu không tìm thấy ước số nào, là số nguyên tố

# Kiểm tra số nguyên tố và in kết quả
number = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")