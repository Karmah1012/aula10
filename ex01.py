class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    def imprime_valor(self):
        print(f"Valor do ingresso R$: {self.valor}")

class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)

    def valor_vip(self):
        add = self.valor *0.5
        return self.valor + add

    def imprime_valor(self):
        print(f"Valor do ingresso VIP {self.valor_vip()}")

    def escolher_ingresso(self):
        print("Fala, meu nobre gafanhoto! Qual tipo de ingresso você quer comprar?")
        print("Primeira opção - Ingresso Comum")
        print("Segunda opção - Ingresso VIP")

        escolha_do_ing = input("Digite o número da sua escolha: ")
        valor_base = 50
        if escolha_do_ing == '1':
            ingresso = Ingresso(valor_base)
            print("Você escolheu o Ingresso Comum, tás liso, benção?")
            print("Oxe, quase que não tem limite nesse teu Nubank Gold aí, boy!")
            ingresso.imprime_valor()
        elif escolha_do_ing == '2':
            ingresso_vip = Vip(valor_base)
            print("Você escolheu o Ingresso VIP, tua mãe te deu dinheiro, foi?")
            print("Dica pra tu, macho liso, paga o da novinha também!")
            ingresso_vip.imprime_valor()
        else:
            print("Essa opção é inválida, jovem, escolhe outra dentro da nossa realidade")
            print("Viesse bêbado pro cinema, foi?")