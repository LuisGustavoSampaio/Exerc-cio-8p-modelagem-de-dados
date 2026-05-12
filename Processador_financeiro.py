# Código duplicado
# Muitos comentários desnecessários
class ProcessadorFinanceiro:
    def processar_pagamento(self, tipo_pagamento, valor, taxa):
        if valor <= 0:
            print("Valor inválido")
            return

        valor_com_taxa = self.calcular_valor_com_taxa(valor, taxa)
        print(f"Processando {tipo_pagamento}: R$ {valor_com_taxa}")

    def calcular_valor_com_taxa(self, valor, taxa):
        return valor + (valor * taxa)

    def processar_pagamento_credito(self, valor):
        self.processar_pagamento("crédito", valor, 0.05)

    def processar_pagamento_debito(self, valor):
        self.processar_pagamento("débito", valor, 0.02)