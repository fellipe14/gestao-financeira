class Financas:
    def __init__(self):
        self.saldo = 0.0

    def adicionar_valor(self, valor):
        self.saldo += valor
        print(f"Valor adicionado: R$ {valor:.2f}")
        self.mostrar_saldo()

    def aplicar_desconto(self, desconto):
        if desconto <= self.saldo:
            self.saldo -= desconto
            print(f"Desconto aplicado: R$ {desconto:.2f}")
        else:
            print("Saldo insuficiente para aplicar o desconto.")
        self.mostrar_saldo()

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")


def main():
    gestor_financeiro = Financas()

    while True:
        print("\nOpções:")
        print("1 - Adicionar valor")
        print("2 - Aplicar desconto")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser adicionado: "))
            gestor_financeiro.adicionar_valor(valor)
        elif opcao == '2':
            desconto = float(input("Digite o valor do desconto: "))
            gestor_financeiro.aplicar_desconto(desconto)
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()