animals_list = ["Fox", "Fly", "Ant", "Bee", "Cod"]
animals_list2 = ["Yak", "Cow", "Hen"]
animals_list3 = ["Cat", "Dog", "Cow", "Koi", "Hog"]
animals_list4 = ["Cat", "Dog", "Fox"]


# def remove(x):



# prints my initial animal list
print(animals_list)

print(animals_list.count('Fox'))

# Adds my fourth animal list after the third animal in list 1
animals_list.insert(2, animals_list4)

# prints the first list with list4 inserted
print(animals_list)

# Counts each animal in the list
print(animals_list.count('Fox'))



count = 0

for animal in animals_list:
    if isinstance(animal, str):
        if animal == 'Fox':
            count = count + 1
        else:
            for item in animal:
                if item == 'Fox':
                    count = count + 1




print(count)


