from database import Database
from cli import MotoristaCLI

# Conectar ao banco de dados
db = Database(database="motoristas_db", collection="motoristas")

def main():
    # Criar uma instância da MotoristaCLI, passando o nome do banco e da coleção
    motorista_cli = MotoristaCLI(database_name="motoristas_db", collection_name="motoristas")
    
    # Iniciar o menu interativo
    motorista_cli.run()

if __name__ == "__main__":
    main()