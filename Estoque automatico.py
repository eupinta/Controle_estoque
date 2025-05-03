class Produto:
    def __init__(self, nome, quantidade, codigo):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade

    def entrada(self, quantidade):
        self.quantidade += quantidade
        print(f"Entrada de {quantidade} unidades de {self.nome}. Estoque atual: {self.quantidade}")

    def saida(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"Saída de {quantidade} unidades de {self.nome}. Estoque atual: {self.quantidade}")
        else:
            print("Quantidade insuficiente no estoque.")

    def mostrar_estoque(self):
        print(f"Produto: {self.nome} | Estoque: {self.quantidade}")


class Estoque:
    def __init__(self):
        self.produtos = {}
        self.contador_codigo = 1  # Contador para gerar códigos automáticos

    def gerar_codigo(self):
        codigo = str(self.contador_codigo).zfill(3)  # Código de 3 dígitos
        self.contador_codigo += 1
        return codigo

    def adicionar_produto(self, nome, quantidade):
        codigo = self.gerar_codigo()
        novo_produto = Produto(nome, quantidade, codigo)
        self.produtos[codigo] = novo_produto
        print(f"Produto {nome} adicionado com código {codigo}.")

    def buscar_produto(self, codigo):
        return self.produtos.get(codigo)

    def exibir_menu(self):
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Produto")
        print("2 - Registrar Saída de Produto")
        print("3 - Registrar Entrada de Produto")
        print("4 - Exibir Quantidade Estocada")
        print("5 - Sair")


def main():
    estoque = Estoque()

    while True:
        estoque.exibir_menu()
        opcao = input("Digite a opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade inicial: "))
            estoque.adicionar_produto(nome, quantidade)

        elif opcao == "2":
            codigo = input("Digite o código do produto: ")
            produto = estoque.buscar_produto(codigo)
            if produto:
                quantidade = int(input(f"Digite a quantidade de saída de {produto.nome}: "))
                produto.saida(quantidade)
            else:
                print("Produto não encontrado.")

        elif opcao == "3":
            codigo = input("Digite o código do produto: ")
            produto = estoque.buscar_produto(codigo)
            if produto:
                quantidade = int(input(f"Digite a quantidade de entrada de {produto.nome}: "))
                produto.entrada(quantidade)
            else:
                print("Produto não encontrado.")

        elif opcao == "4":
            codigo = input("Digite o código do produto: ")
            produto = estoque.buscar_produto(codigo)
            if produto:
                produto.mostrar_estoque()
            else:
                print("Produto não encontrado.")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
