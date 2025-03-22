from database import Database
from writeAJson import writeAJson
from personModel import PersonModel
from cli import PersonCLI

from livrosModel import LivroModel
from cli import LivroCLI

# db = Database(database="relatorio_05", collection="pessoas")
# personModel = PersonModel(database=db)


# personCLI = PersonCLI(personModel)
# personCLI.run()

# Conectar ao banco de dados
db = Database(database="Relatório_05", collection="Livros")

# Instanciar o CRUD
livro_model = LivroModel(database=db)

# Iniciar CLI
livro_cli = LivroCLI(livro_model)
livro_cli.run()