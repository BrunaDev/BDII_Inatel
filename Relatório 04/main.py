from database import Database
from helper.writeAJson import writeAJson
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
## db.resetDatabase()

analyzer = ProductAnalyzer(db)

# 1- Média de gasto total:
## result = db.collection.aggregate([
##    {"$unwind": "$produtos"},
##    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
##    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
## ])

## writeAJson(result, "Média de gasto total")

# 2- Cliente que mais comprou em cada dia:
## result2 = db.collection.aggregate([
##     {"$unwind": "$produtos"},
##     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
##     {"$sort": {"_id.data": 1, "total": -1}},
##     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
## ])

## writeAJson(result2, "Cliente que mais comprou em cada dia")

# 3- Produto mais vendido:
## result3 = db.collection.aggregate([
##     {"$unwind": "$produtos"},
##     {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
##     {"$sort": {"total": -1}},
##     {"$limit": 1}
## ])

## writeAJson(result3, "Produto mais vendido")

# Executando os pipelines e salvando os resultados
writeAJson(analyzer.total_vendas_por_dia(), "Total de vendas por dia")
writeAJson(analyzer.produto_mais_vendido(), "Produto mais vendido")
writeAJson(analyzer.cliente_que_mais_gastou(), "Cliente que mais gastou")
writeAJson(analyzer.produtos_com_quantidade_maior_que_um(), "Produtos com mais de 1 unidade vendida")