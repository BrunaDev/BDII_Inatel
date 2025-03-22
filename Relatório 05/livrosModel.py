from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database

    def create_livro(self, titulo: str, autor: str, ano: int, preco: float):
        """Cria um novo livro na coleção"""
        try:
            res = self.db.collection.insert_one({
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "preco": preco
            })
            print(f"Livro criado com ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def read_livro_by_id(self, id: str):
        """Lê um livro pelo ID"""
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            if res:
                print(f"Livro encontrado: {res}")
            else:
                print("Livro não encontrado")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o livro: {e}")
            return None

    def update_livro(self, id: str, titulo: str, autor: str, ano: int, preco: float):
        """Atualiza um livro pelo ID"""
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {
                    "titulo": titulo,
                    "autor": autor,
                    "ano": ano,
                    "preco": preco
                }}
            )
            print(f"Livro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def delete_livro(self, id: str):
        """Exclui um livro pelo ID"""
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento(s) excluído(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None
