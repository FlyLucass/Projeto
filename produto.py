class Produto():
    
    def __init__(self,nome,id,preco,quantidade):
        self.nome
        self.id
        self.preco
        self.quantidade=int
             

def produtocadastrado(Produto,nome,id,preco,quantidade ):
    Produto={}
    try:
        nome=input("Digite o nome do produto: ")
        id=input("Digite o indetificador do produto: ")
        preco=float(input("Digite o preço do produto "))
        quantidade=int(input("Digite a quantidade desse produto "))
        
    #except self.id in Estoque.cla.keys(Estoque):
    #             print("Erro ja existe um produto cadastrado com esse ID")
    finally:
        Produto.update({"Nome":nome})
        Produto.update({"ID":id})
        Produto.update({"Preço Inicial":preco*quantidade})
        calcularimposto(preco,quantidade)
        print("Produto cadastrado com sucesso!!!")
        
def calcularimposto(preco,quantidade):
    imposto=float(preco*0.15)
    total=float(preco+0.15)*quantidade
    Produto.update({"Preco Final": total})
    Produto.update({"Imposto":imposto}) 
    
    return
    
