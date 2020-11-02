def probability(space, event):
    return len(event) / len(space)

six_sided = {*[1, 2, 3, 4, 5, 6]}
three = {*[3]}

roll_three = probability(six_sided, three)
print(roll_three)
