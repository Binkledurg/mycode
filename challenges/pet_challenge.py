pets = ['fido', 'spot', 'fluffy']

pets.insert(1, 'sparky')

pets.append("Barky Von Schnauzer")

pet_name = input("What is your dog's name?")

pets.append(pet_name)

pet2 = input("What about your hamster?")

pets.append(pet2)


#index = pets.index("fido")

#print(index)
#print(pets)

for i, v in enumerate(pets):
    print(i, v)






















