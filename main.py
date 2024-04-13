class Initialize():

    def __init__(self):
        self.__transactions = []

    def show_menu(self):
        print(50*'-')
        print('Bem vindo ao Controle Financeiro')
        print(50*'-')

        print('1 - Adicionar transação')
        print('2 - Visualizar transações')
        print('3 - Sair')

    def choose_options(self):
        option = input('\nEscolha uma das opções: ')

        if option != '1' and option != '2' and option != '3':
            print('\nOpção inválida')
        
        return option

    def to_add(self):
        operation = input('Informe o tipo da operação: ')
        value = input('Informe o valor: ')
        description = input('Informe a descrição: ')

        self.__transactions.append(
            (operation, value, description)
        )

    def to_view(self):
        for transaction in self.__transactions:
            print(f'Operation: {transaction[0]} - Value: {transaction[1]} - Description: {transaction[2]}')

    def to_go_out(self):
        print('\nVolte sempre')

if __name__ == '__main__':
    init = Initialize()
    option = ''

    while option != '3':
        init.show_menu()
        option = init.choose_options()

        if option == '1':
            init.to_add()
        elif option =='2':
            init.to_view()
        elif option == '3':
            init.to_go_out()
