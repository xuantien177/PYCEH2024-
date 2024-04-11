#Dãy trong Python bắt đầu từ vị trí 0
#Kết thúc bằng vị trí luôn luôn là -1 mà không cần biết chính xác độ dài của dãy, mảng đó
index=[4,6,3498,289,80]
car=["BMW", "Lexus", "Mercedes-Benz", "Honda", "Hyundai", "VM"]
#     0, 1, 2 ,  3, 4
print(index[3])
print(car[-1].upper()) # Sẽ in ra 'VM' viết hoa, phần tử cuối cùng trong danh sách 'car'
print(f"My first car is {car[3].title()}")
