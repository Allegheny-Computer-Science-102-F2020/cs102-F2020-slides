# create the dictionary

mlb_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

# determine details about the dictionary

print(type(mlb_team))
print(mlb_team)

# access content that exists in the dictionary

print(mlb_team['Minnesota'])
print(mlb_team['Colorado'])

# add new content to the dictionary

mlb_team['Kansas City'] = 'Royals'

# determine details about the dictionary

print(type(mlb_team))
print(mlb_team)

# access content that does not exist in the dictionary

print(mlb_team['Toronto'])
