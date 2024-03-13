import CRUD_BIBLIO_PT1.crud as crud

def aba_crud(table,crud):
    result = []
    for i in range(len(crud)):
        print(f'{crud[i]} {table[:-1]}')
    return result

def menu():
    print("Menu: ")
    
    tables = ["Livros", "Alunos", "Emprestimos"]
    crud = ["Create", "Read", "Update", "Delete"]

    for i in range(len(tables)):
        print(f'Opção {i+1}.{tables[i]}')


    opcao_aba1 = int(input("\nQual opção deseja escolher? \n"))

    if opcao_aba1 == 1:
        aba_2 = aba_crud(tables[0],crud)
        for item in aba_2:
            print(item)

    elif opcao_aba1 == 2:
        aba_2 = aba_crud(tables[1],crud)
        for item in aba_2:
            print(item)
            
    elif opcao_aba1 == 3:
        aba_2 = aba_crud(tables[2],crud)
        for item in aba_2:
            print(item)
    else:
        ("Opção inválida")

if __name__ == "__main__":
    menu()

'''a = "amoras"
b = a[:-1]
print(b)'''