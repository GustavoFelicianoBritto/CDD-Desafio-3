class TarefasClass():
    def __init__(self):
        self.listaClasse=[]
        self.tempTarefa = ""

    def listartarefas(self):
        if self.listaClasse:
            print("Lista de tarefas: ")
            for index,item in enumerate(self.listaClasse):
                print(f"{index} - {self.listaClasse[index]}")
            print()
        else:
            print("Lista se encontra Vazia")

    def inserirtarefas(self):
        temptarefa=input("Insira uma tarefa: ")
        self.listaClasse.append(temptarefa)
        print(f"Tarefa {temptarefa} registrada.")
        print()

    def deletartarefas(self):
        optiondelete=None
        if self.listaClasse:
            print("Qual tarefa deseja deletar? (numero)")
            self.listartarefas()
            optiondelete= int(input())
            self.tempTarefa=self.listaClasse[optiondelete]
            self.listaClasse.pop(optiondelete)
            print(f"Tarefa {self.tempTarefa} deletada.")


        else:
            print("Lista se encontra vazia")


    def menu(self):
        option=0
        while True:
            option = int(
                input("\n1- listar tarefas \n2- inserir uma tarefa \n3- deletar tarefa\n4- sair\nEscolha uma opção:\n"))
            print()
            print()
            if option == 4:
                print("Programa finalizado, Lista final:")
                self.listartarefas()
                break
            elif option == 1:
                self.listartarefas()
            elif option == 2:
                self.inserirtarefas()
            elif option == 3:
                self.deletartarefas()
            else:
                print("Opção inválida")