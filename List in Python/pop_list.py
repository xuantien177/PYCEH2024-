car_makers = ['Honda','BMW','VW','JEEP','Fiat','Opel','SAAB']
print(car_makers)
owned_car = car_makers.pop(1)  #Lấy ra phần tử thứ 2 của dãy
print(car_makers) #Dãy sau khi đã lấy phần tử ra

#Sử dụng phần tử đã lấy ra ở phía trên
print(f"\nThe car model that I owned was a {owned_car}")