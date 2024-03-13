import crud as crud


def menu():
    print("Menu: ")

    crud_options = ["Create", "Read", "Update", "Delete"]

    for i in range(len(crud_options)):
        print(f'Opção ({i+1}).{crud_options[i]} LIVRO')


    opcao = int(input("\nQual opção deseja operar na tabela? \n"))

    if opcao == 1:
        titulo = input(('Insira o nome do livro: '))
        autor = input(('Insira o nome do Autor: '))
        genero = input(('Insira o gênero: '))
        crud.create_livro(autor, titulo, genero)

    elif opcao == 2:
        read_dados = crud.read_table('livros')
        print(read_dados)
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
