"""creating a list from a list with one line"""
#new_list = [{new_item} for {item} in {old_list or any sequence} if {test}]

"""creating list from range"""
# new_list =[2*n for n in range(1,5)]
# print(new_list)

"""using if statement in list comprehension"""
names = ['Jonathan', 'Emily', 'Christopher', 'Liam', 'Sophia']
new_names = [name.upper() for name in names if len(name)>5]
print(new_names)