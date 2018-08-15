class Perfil():
    def __init__(self,nome,telefone,empresa):
        self.nome=nome
        self.telefone=telefone
        self.empresa=empresa

    def print_perfil(self):
        print 'Nome:%s,  Telefone:%s,  Empresa%s ' %(self.nome,self.telefone,self.empresa)