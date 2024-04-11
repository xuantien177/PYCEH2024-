car_model="bmw"
car_year=2011

if(2024-car_year)<10:
        print(f"Your {car_model} is a new model with {2024-car_year} years")
else:
        print(f"Sorry but Our Company doesn't buy {car_model.upper()} that age is more than 10 years")
        print(f"\nYour car is {2024-car_year} years.\tIt's too old")

car=["bmw", "lexus", "mercedes-benz", "honda", "hyundai", "vm"]
for model in car:
    if model == "bmw":
        print(model.lower())     
    else:
        print(model.upper())   
