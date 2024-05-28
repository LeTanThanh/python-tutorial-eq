from person import Person

# Python __eq__

john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)

print(john is jane)
print(john == jane)
