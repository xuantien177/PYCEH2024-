my_list = [1, 2, 3, 4, 5]   #Vị trí mảng 0,1,2,3,4
sliced_list = my_list[1:4]  # Cắt từ index 1 đến index 3
print(f'\nSliced_list là: {sliced_list}')  # Output: [2, 3, 4]

my_favorite_cars = ['bmw','honda','vw','ford','hyundai','kia','nissan']
friends_favorite_cars = my_favorite_cars[:]   #Sử dụng phép copy mảng ban đầu
fake_list=my_list.copy()  #Hoặc sử dụng hàm .copy()

my_favorite_cars.remove('honda')
friends_favorite_cars.append('fiat')
sliced_fake_list=fake_list[1:3]  #Cắt từ index 1 tới index 2

print("\nMy favorite cars are : ")
print(my_favorite_cars)

print("\nMy firend's favorite cars are : ")
print(friends_favorite_cars)

print("\n My fake list from original list are:")
print(sliced_fake_list)

