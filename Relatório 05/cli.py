class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class PersonCLI(SimpleCLI):
    def __init__(self, person_model):
        super().__init__()
        self.person_model = person_model
        self.add_command("create", self.create_person)
        self.add_command("read", self.read_person)
        self.add_command("update", self.update_person)
        self.add_command("delete", self.delete_person)

    def create_person(self):
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        self.person_model.create_person(name, age)

    def read_person(self):
        id = input("Enter the id: ")
        person = self.person_model.read_person_by_id(id)
        if person:
            print(f"Name: {person['name']}")
            print(f"Age: {person['age']}")

    def update_person(self):
        id = input("Enter the id: ")
        name = input("Enter the new name: ")
        age = int(input("Enter the new age: "))
        self.person_model.update_person(id, name, age)

    def delete_person(self):
        id = input("Enter the id: ")
        self.person_model.delete_person(id)
        
    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        
class LivroCLI:
    def __init__(self, livro_model):
        self.livro_model = livro_model

    def run(self):
        while True:
            print("\n📚 MENU - GERENCIAMENTO DE LIVROS 📚")
            print("1 - Adicionar um livro")
            print("2 - Buscar um livro por ID")
            print("3 - Atualizar um livro")
            print("4 - Deletar um livro")
            print("5 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                ano = int(input("Ano: "))
                preco = float(input("Preço: "))
                self.livro_model.create_livro(titulo, autor, ano, preco)

            elif opcao == "2":
                id_livro = input("ID do livro: ")
                self.livro_model.read_livro_by_id(id_livro)

            elif opcao == "3":
                id_livro = input("ID do livro a ser atualizado: ")
                titulo = input("Novo título: ")
                autor = input("Novo autor: ")
                ano = int(input("Novo ano: "))
                preco = float(input("Novo preço: "))
                self.livro_model.update_livro(id_livro, titulo, autor, ano, preco)

            elif opcao == "4":
                id_livro = input("ID do livro a ser deletado: ")
                self.livro_model.delete_livro(id_livro)

            elif opcao == "5":
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida. Tente novamente!")
