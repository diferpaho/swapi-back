pokemons ="audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

pokemon_list=pokemons.split(" ")
x_pokemon_list =[]
y_pokemon_list=[]

for i in range(0,len(pokemon_list)-1):
        for j in range(0,len(pokemon_list)-1):
            if pokemon_list[i] != pokemon_list[j]:
                if pokemon_list[i][len(pokemon_list[i])-1] == pokemon_list[j][0]:
                    x_pokemon_list.append(pokemon_list[i]+" "+pokemon_list[j])

while True:

    for i in range(0,len(x_pokemon_list)-1):
        for j in range(0,len(pokemon_list)-1):
            if x_pokemon_list[i].find(pokemon_list[j]) == -1:
                if x_pokemon_list[i][len(x_pokemon_list[i])-1] == pokemon_list[j][0]:
                    y_pokemon_list.append(x_pokemon_list[i]+" "+pokemon_list[j])

    if len(y_pokemon_list)==0:
         break
    x_pokemon_list = y_pokemon_list
    y_pokemon_list= []
    
sequences = x_pokemon_list[0].split(" ")
print("Mayor número posible de nombres de Pokémon: "+str(len(x_pokemon_list[0].split(" "))))
print("Cantidas de secuencias con este numero: "+str(len(x_pokemon_list)))
print("Primera sentencia que cumple los parametros: ")
print(x_pokemon_list[0])