def pet(category, name, color, age):
    pet_info= f"\nPet information : This is {category} and with name {name}, {color} color. It is {age} years old"
    return pet_info

pet1=pet('cat','Kitty','pink',3)
pet2=pet('dog','The Rock','black',2)
print(pet1)
print(pet2)