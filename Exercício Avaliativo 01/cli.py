from dao import MotoristaDAO
from classes import Passageiro, Corrida, Motorista

class MotoristaCLI:
    def __init__(self, database_name="motoristas_db", collection_name="motoristas"):
        self.motorista_dao = MotoristaDAO(database_name, collection_name)

    def run(self):
        print("\n🚗 Bem-vindo ao Sistema de Gerenciamento de Motoristas por Aplicativo! 🚗")
        print("Aqui você pode gerenciar motoristas, suas corridas e passageiros.")
        while True:
            print("\n=== MENU ===")
            print("1 - Adicionar corridas de um motorista")
            print("2 - Buscar um motorista por ID")
            print("3 - Atualizar as corridas de um motorista")
            print("4 - Deletar um motorista")
            print("5 - Sair")
            opcao = input("Escolha uma opção (1-5): ")

            if opcao == "1":
                self.create()
            elif opcao == "2":
                self.read()
            elif opcao == "3":
                self.update()
            elif opcao == "4":
                self.delete()
            elif opcao == "5":
                print("Saindo do sistema... Até logo! 👋")
                break
            else:
                print("❌ Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

    def create(self):
        print("\n=== Adicionar Novo Motorista e Suas Corridas ===")
        # Criar Passageiro
        print("📋 Informações do Passageiro para as corridas:")
        nome = input("Nome do passageiro: ")
        documento = input("Documento do passageiro (ex: 12345678900): ")
        passageiro = Passageiro(nome, documento)

        # Criar Corrida(s)
        corridas = []
        while True:
            print("\n🏁 Informações da Corrida do Motorista:")
            try:
                nota = int(input("Nota da corrida (1-5): "))
                if nota < 1 or nota > 5:
                    print("❌ A nota deve estar entre 1 e 5!")
                    continue
                distancia = float(input("Distância da corrida (km): "))
                valor = float(input("Valor da corrida (R$): "))
                corrida = Corrida(nota, distancia, valor, passageiro)
                corridas.append(corrida)
            except ValueError:
                print("❌ Entrada inválida! Certifique-se de inserir números válidos.")
                continue

            mais_corridas = input("Deseja adicionar mais uma corrida para este motorista com o mesmo passageiro? (s/n): ").lower()
            if mais_corridas != "s":
                break

        # Criar Motorista
        nota_motorista = int(input("Nota do motorista (1-5): "))
        motorista = Motorista(nota_motorista, corridas)
        try:
            result = self.motorista_dao.create(motorista)
            print(f"✅ Motorista e suas corridas criados com sucesso! ID: {result.inserted_id}")
        except Exception as e:
            print(f"❌ Erro ao criar motorista: {e}")

    def read(self):
        print("\n=== Buscar Motorista ===")
        motorista_id = input("Digite o ID do motorista: ").strip()
        try:
            motorista = self.motorista_dao.read(motorista_id)
            if motorista:
                print("\n📋 Informações do Motorista:")
                print(f"ID: {motorista['_id']}")
                print(f"Nota média: {motorista['nota']:.1f}")
                print("Corridas:")
                for corrida in motorista["corridas"]:
                    print(f"  - Nota: {corrida['nota']}")
                    print(f"    Distância: {corrida['distancia']} km")
                    print(f"    Valor: R$ {corrida['valor']}")
                    print(f"    Passageiro: {corrida['passageiro']['nome']} (Documento: {corrida['passageiro']['documento']})")
            else:
                print("❌ Motorista não encontrado!")
        except Exception as e:
            print(f"❌ Erro ao buscar motorista: {e}")

    def update(self):
        print("\n=== Atualizar as Corridas de um Motorista ===")
        motorista_id = input("Digite o ID do motorista a ser atualizado: ").strip()
        try:
            motorista = self.motorista_dao.read(motorista_id)
            if not motorista:
                print("❌ Motorista não encontrado!")
                return

            print(f"📋 Atualizando as corridas do motorista '{motorista['_id']}'...")

            print("📋 Informações do Novo Passageiro para as corridas:")
            nome = input("Nome do passageiro: ")
            documento = input("Documento do passageiro (ex: 12345678900): ")
            passageiro = Passageiro(nome, documento)

            corridas = []
            while True:
                print("\n🏁 Informações da Nova Corrida do Motorista:")
                try:
                    nota = int(input("Nota da corrida (1-5): "))
                    if nota < 1 or nota > 5:
                        print("❌ A nota deve estar entre 1 e 5!")
                        continue
                    distancia = float(input("Distância da corrida (km): "))
                    valor = float(input("Valor da corrida (R$): "))
                    corrida = Corrida(nota, distancia, valor, passageiro)
                    corridas.append(corrida)
                except ValueError:
                    print("❌ Entrada inválida! Certifique-se de inserir números válidos.")
                    continue

                mais_corridas = input("Deseja adicionar mais uma corrida para este motorista? (s/n): ").lower()
                if mais_corridas != "s":
                    break

            corridas_dict = []
            for corrida in corridas:
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

            success = self.motorista_dao.update(motorista_id, {"corridas": corridas_dict})
            if success:
                print(f"✅ Motorista {motorista_id} atualizado com sucesso!")
                motorista_atualizado = self.motorista_dao.read(motorista_id)
                print(f"📊 Nova nota média: {motorista_atualizado['nota']}")
            else:
                print("❌ Nenhum documento foi atualizado (pode ser que os dados sejam iguais)")
        except Exception as e:
            print(f"❌ Erro ao atualizar motorista: {e}")

    def delete(self):
        print("\n=== Deletar Motorista ===")
        motorista_id = input("Digite o ID do motorista a ser deletado: ").strip()
        try:
            motorista = self.motorista_dao.read(motorista_id)
            if not motorista:
                print("❌ Motorista não encontrado!")
                return
            confirm = input(f"Tem certeza que deseja deletar o motorista com ID {motorista_id}? (s/n): ").lower()
            if confirm == "s":
                success = self.motorista_dao.delete(motorista_id)
                if success:
                    print(f"✅ Motorista {motorista_id} deletado com sucesso!")
                else:
                    print("❌ Nenhum documento foi deletado")
            else:
                print("Operação cancelada.")
        except Exception as e:
            print(f"❌ Erro ao deletar motorista: {e}")