from database import Database

class ProductAnalyzer:
    def __init__(self, db):
        self.db = db
    
    def total_vendas_por_dia(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ]
        return list(self.db.collection.aggregate(pipeline))
    
    def produto_mais_vendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_quantidade": -1}},
            {"$limit": 1}
        ]
        return list(self.db.collection.aggregate(pipeline))
    
    def cliente_que_mais_gastou(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ]
        return list(self.db.collection.aggregate(pipeline))
    
    def produtos_com_quantidade_maior_que_um(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total_quantidade": {"$gt": 1}}}
        ]
        return list(self.db.collection.aggregate(pipeline))
