from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        # Relação de agregação com a classe Database
        self.db = database

    def get_pokemon_by_name(self, name: str):
        """Busca um Pokémon pelo nome"""
        try:
            result = self.db.collection.find_one({"name": {"$regex": name, "$options": "i"}})
            writeAJson(result, f"pokemon_by_name_{name}")
            return result
        except Exception as e:
            print(f"Erro ao buscar Pokémon por nome: {e}")
            return None

    def get_pokemons_by_type(self, pokemon_type: str):
        """Busca todos os Pokémon de um tipo específico"""
        try:
            result = list(self.db.collection.find({"type": pokemon_type}))
            writeAJson(result, f"pokemons_by_type_{pokemon_type}")
            return result
        except Exception as e:
            print(f"Erro ao buscar Pokémon por tipo: {e}")
            return None

    def get_pokemons_by_spawn_chance_range(self, min_chance: float, max_chance: float):
        """Busca Pokémon com taxa de spawn dentro de um intervalo"""
        try:
            result = list(self.db.collection.find({
                "spawn_chance": {"$gte": min_chance, "$lte": max_chance}
            }))
            writeAJson(result, f"pokemons_spawn_chance_{min_chance}_to_{max_chance}")
            return result
        except Exception as e:
            print(f"Erro ao buscar Pokémon por taxa de spawn: {e}")
            return None

    def get_pokemons_by_weakness(self, weakness: str):
        """Busca Pokémon com uma fraqueza específica"""
        try:
            result = list(self.db.collection.find({"weaknesses": weakness}))
            writeAJson(result, f"pokemons_with_weakness_{weakness}")
            return result
        except Exception as e:
            print(f"Erro ao buscar Pokémon por fraqueza: {e}")
            return None

    def get_pokemons_by_candy_count_range(self, min_candy: int, max_candy: int):
        """Busca Pokémon com quantidade de candy dentro de um intervalo"""
        try:
            result = list(self.db.collection.find({
                "candy_count": {"$gte": min_candy, "$lte": max_candy}
            }))
            writeAJson(result, f"pokemons_candy_count_{min_candy}_to_{max_candy}")
            return result
        except Exception as e:
            print(f"Erro ao buscar Pokémon por candy count: {e}")
            return None