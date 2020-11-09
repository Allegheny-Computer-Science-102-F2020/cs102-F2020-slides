# create the dictionary

MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

# determine details about the dictionary

print(type(MLB_team))
print(MLB_team)

# access content that exists in the dictionary

print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])

# add new content to the dictionary

MLB_team['Kansas City'] = 'Royals'

# determine details about the dictionary

print(type(MLB_team))
print(MLB_team)

# access content that does not exist in the dictionary

print(MLB_team['Toronto'])
