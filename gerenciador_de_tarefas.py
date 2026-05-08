#Code Smeel: Metodo longo - solução: quebrar em vario metodos
class GerenciadorDeVendas:

    def processar_venda_e_gerar_relatorio(self, itens, cliente, metodo_pagamento):
        total = self.calcular_total(itens)
        total = self.aplicar_desconto(total, cliente)

        self.processar_pagamento(total, metodo_pagamento)

        relatorio = self.gerar_relatorio(cliente, total)
        self.salvar_relatorio(relatorio)

        print("Venda processada com sucesso")


    def calcular_total(self, itens):
        total = 0

        for item in itens:
            total += item['preco'] * item['quantidade']

        return total


    def aplicar_desconto(self, total, cliente):
        if cliente['tipo'] == 'VIP':
            total = total * 0.90

        return total


    def processar_pagamento(self, total, metodo_pagamento):
        if metodo_pagamento == 'CARTAO':
            print(f'Cobrando R$ {total:.2f} no cartão de crédito')

        elif metodo_pagamento == 'BOLETO':
            print(f'Gerando boleto no valor de R$ {total:.2f}')

        else:
            print("Método de pagamento inválido")


    def gerar_relatorio(self, cliente, total):
        relatorio = (
            "--- RELATÓRIO DE VENDAS ---\n"
            f"Cliente: {cliente['nome']}\n"
            f"Total: R$ {total:.2f}\n"
        )

        return relatorio


    def salvar_relatorio(self, relatorio):
        with open("relatorio_vendas.txt", "a", encoding="utf-8") as f:
            f.write(relatorio)