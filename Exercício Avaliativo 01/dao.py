from database import Database
from bson import ObjectId 

class MotoristaDAO:
    def __init__(self, database_name="motoristas_db", collection_name="motoristas"):
        self.database = Database(database_name, collection_name)
        self.collection = self.database.get_collection()

    def create(self, motorista):
        corridas_dict = []
        for corrida in motorista.corridas:
            corrida_dict = {
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": {
                    "nome": corrida.passageiro.nome,
                    "documento": corrida.passageiro.documento
                }
            }
            corridas_dict.append(corrida_dict)

        motorista_dict = {
            "nota": motorista.nota,
            "corridas": corridas_dict
        }
        result = self.collection.insert_one(motorista_dict)
        return result

    def read(self, motorista_id):
        obj_id = ObjectId(motorista_id)
        return self.collection.find_one({"_id": obj_id})

    def update(self, motorista_id, update_data):
        obj_id = ObjectId(motorista_id)
        # Recalcular a nota do motorista
        corridas = update_data.get("corridas", [])
        if corridas:
            total_notas = sum(corrida["nota"] for corrida in corridas)
            update_data["nota"] = int(round(total_notas / len(corridas)))
        
        result = self.collection.update_one(
            {"_id": obj_id},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete(self, motorista_id):
        obj_id = ObjectId(motorista_id)
        result = self.collection.delete_one({"_id": obj_id})
        return result.deleted_count > 0