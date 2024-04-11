# Khởi tạo một list chứa các số từ 1 đến 10
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Duyệt qua các phần tử của list bắt đầu từ phần tử thứ 4 (index 3)
for i in list[3:]:
    # Tính bình phương của phần tử hiện tại
    siu = i ** 2
    # Thêm kết quả bình phương vào cuối list
    list.append(siu)

# In ra list sau khi thêm các phần tử bình phương
print(list)