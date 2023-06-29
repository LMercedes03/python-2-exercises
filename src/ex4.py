def get_people(people_list):
    # Return names if age is => than 15
    new_list = [p['name'] for p in people_list if p['age'] >= 15]
    return new_list


people_list = [
    {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
    {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
print(get_people(people_list))
