MAX_LINES = 3


def deposit():
    while True:
        amount = input('Digite o valor do depósito: R$')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('O valor deve ser maior que zero.')
        else:
            print('Por favor, digite um número.')

    return amount


deposit()


def get_number_of_lines():
    while True:
        lines = input('Insira o número de linhas que você quer apostar (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Insira um número de linhas valido. ')
        else:
            print('Por favor insira um número. ')


    return lines
            
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)



main()
