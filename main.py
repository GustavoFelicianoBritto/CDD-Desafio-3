from library import tarefasClass
# menu
#
# 1- listar tarefasClass
# 2- inserir uma tarefa
# 3- deletar tarefa
# 4- sair

gerenciadorDeTarefas = tarefasClass()

tarefasLista=["teste1","teste2","teste3"]
option=0

while True:
    option = int(input("Escolha uma opção:\n\n1- listar tarefas \n2- inserir uma tarefa \n3- deletar tarefa\n4- sair"))
    print()
    print()
    if option==4:
        print("Programa finalizado")
        break
    elif option==1:
        gerenciadorDeTarefas.listarTarefas(tarefasLista)
    elif option==2:
        gerenciadorDeTarefas.inserirTarefas(tarefasLista)
    elif option==3:
        gerenciadorDeTarefas.deletarTarefas(tarefasLista)
    else:
        print("Opção inválida")

