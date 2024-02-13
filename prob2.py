people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Haitham", "laith"]
new_people = sorted(people, key=lambda x: (len(x), x))
print(new_people)