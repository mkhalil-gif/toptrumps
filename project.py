
# Pokemon Toptrumps

# 1. Generate a random number between 1 and 151 to use as the Pokemon ID number
import random

pokemon_id = random.randint(1, 151)
print("ID of Pokemon is " + str(pokemon_id))

# 2. Using the Pokemon API get a Pokemon based on its ID number
import requests

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
response = requests.get(url)
pokemon = response.json()
print("Name of the pokemon is " + str(pokemon['name']))

# 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (★
# https://pokeapi.co/)
poke = {
    'name': print("Name of the Pokemon is " + str(pokemon['name'])),
    'ID': print("ID of of the Pokemon is " + str(pokemon_id)),
    'height': print("The height of the Pokemon is " + str(pokemon['height'])),
    'weight': print("The weight of the Pokemon is " + str(pokemon['weight']))
}

# 4. Get a random Pokemon for the player and another for their opponent

id_player1 = random.randint(1, 151)
id_player2 = random.randint(1, 151)
print("ID of player 1 is " + str(id_player1))
print("ID of player 2 is " + str(id_player2))

url1 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id_player1)
url2 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id_player2)

response1 = requests.get(url1)
response2 = requests.get(url2)
pokemon1 = response1.json()
pokemon2 = response2.json()
print("Name of the pokemon is " + str(pokemon1['name']))
print("Name of the pokemon is " + str(pokemon2['name']))


# 5. Ask the user which stat they want to use (id, height or weight)
def get_user_stat(player):
    stat = input("Which stat do you want to use? (ID, height or weight)")
    print(player + " chose " + stat)
    return stat


output_player_1 = get_user_stat('player 1')
print(output_player_1)
output_player_2 = get_user_stat('player 2')
print(output_player_2)


# 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
def check_output(player_output, pokemon):
    if player_output == 'ID':
      player_output = str(pokemon['ID'])
    elif player_output == 'height':
      player_output = str(pokemon['height'])
    elif player_output == 'weight':
        player_output = str(pokemon['weight'])
    return (player_output)


output_player1 = check_output(output_player_1, pokemon1)
output_player2 = check_output(output_player_2, pokemon2)

if output_player1 > output_player2:
    print("Player 1 wins")
elif output_player1 < output_player2:
    print("Player 2 wins")
else:
    print("It's a draw")
