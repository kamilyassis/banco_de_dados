import crud


def menu():
    print("Menu: ")

    crud_options = ["Create", "Read", "Update", "Delete"]

    for i in range(len(crud_options)):
        print(f'Opção ({i+1}).{crud_options[i]} LIVRO')


    opcao = int(input("\nQual opção deseja operar na tabela? \n"))

    if opcao == 1:
        titulo = input(('Insira o nome do livro: '))
        autor = input(('Insira o nome do Autor: '))
        num_copias_total = int(input(('Insira o nome do Cópias totais: ')))
        num_copias_disp = int(input(('Insira o nome do Cópias disponíveis: ')))
        num_copias_alug = int(input(('Insira o nome do Cópias alugadas: ')))
        crud.create_livro(autor, titulo, num_copias_total, num_copias_disp, num_copias_alug)

    elif opcao == 2:
        crud.read('livros')
    elif opcao == 3:
        at_ref = 'titulo'
        val_at_ref = input(('Insira o livro que deseja atualizar: '))
        at_change = input(('Insira o atributo que deseja atualizar: '))
        val_at_change = input(('Insira o novo valor do atributo: '))
        crud.update('livros', at_change, val_at_change, at_ref, val_at_ref)

    elif opcao == 4:
        at = 'livro'
        val_at = input(('Insira o livro que deseja deletar: '))
        crud.delete(at, val_at)

    else:
        print("Opção inválida")

if __name__ == "__main__":
    menu()