class tarefasClass():
    def __init__(self):
        pass

    def listarTarefas(self,lista):
        print("Lista de tarefas: ")
        for index,item in enumerate(lista):
            print(index, lista[index])
        print()

    def inserirTarefas(self,lista):
        tempTarefa=input("Insira uma tarefa: ")
        lista.append(tempTarefa)

    def deletarTarefas(self,lista):
        optionDelete=None
        print("Qual tarefa deseja deletar? (numero)")
        for index,item in enumerate(lista):
            print(index, lista[index])
        optionDelete= int(input())
        lista.pop(optionDelete)


