# main.py
from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex
from tabulate import tabulate

def format_pokemon_table(pokemon_list):
    if not pokemon_list:
        return "Nenhum Pokémon encontrado."
    
    # Criando uma lista de listas para a tabela
    table_data = []
    headers = ["Nome", "Tipo", "Candy Count"]
    for pokemon in pokemon_list:
        name = pokemon.get("name", "Desconhecido")
        types = ", ".join(pokemon.get("type", []))
        candy_count = pokemon.get("candy_count", "N/A")
        table_data.append([name, types, candy_count])
    
    return tabulate(table_data, headers=headers, tablefmt="grid")

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

# Criando instância da Pokedex
pokedex = Pokedex(db)

print("Buscando Pikachu:")
result = pokedex.get_pokemon_by_name("Pikachu")
print(f"Nome: {result['name']} | Tipo: {', '.join(result['type'])} | Candy Count: {result['candy_count']}")

print("\nBuscando Pokémon do tipo Fire:")
print(format_pokemon_table(pokedex.get_pokemons_by_type("Fire")))

print("\nBuscando Pokémon com candy count entre 20 e 50:")
print(format_pokemon_table(pokedex.get_pokemons_by_candy_count_range(20, 50)))

print("\nBuscando Pokémon com fraqueza Fire:")
print(format_pokemon_table(pokedex.get_pokemons_by_weakness("Fire")))