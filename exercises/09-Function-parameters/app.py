# Your code goes here:
def render_person(name, year, color, age, gender):
    paragraph = (name + ' is a ' + str(age) + ' years old ' + gender + ' born in ' + str(year) + ' with ' + color + ' eyes')
    return paragraph


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))