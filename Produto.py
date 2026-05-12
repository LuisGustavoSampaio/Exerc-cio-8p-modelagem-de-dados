# Classe Grande / muitas responsabilidades 
class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self):
        return self.preco * 1.15
    
class ProdutoRepository:
    def salvar(self, produto):
        print(
            f"INSERT INTO produtos (id, nome, preco) "
            f"VALUES ({produto.id_produto}, '{produto.nome}', {produto.preco});"
        )

class ProdutoXMLExporter:
    def exportar(self, produto):
        return (
            f"<produto>"
            f"<id>{produto.id_produto}</id>"
            f"<nome>{produto.nome}</nome>"
            f"<preco>{produto.preco}</preco>"
            f"</produto>"
        )