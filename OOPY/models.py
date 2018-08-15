class Perfil():
    def __init__(self,name,cellphone_number,company,tipo):
        self.name=name
        self.cellphone_number=cellphone_number
        self.empresa=company
        self.__likes=0
        self.__tipo=tipo

    def print_perfil(self):
        print 'Nome:%s,  Telefone:%s,  Empresa%s ' %(self.name,self.cellphone_number,self.company)

    def liked(self):
        self.__likes+=1
    
    def get_likes(self):
        return self.__likes
        
  
   

class Perfil_Vip():
    def __init__(self,name,cellphone_number,company,tipo):
        self.name=name
        self.cellphone_number=cellphone_number
        self.empresa=company
        self.__likes=0
        self.__tipo=tipo

    def print_perfil(self):
        print 'Nome:%s,  Telefone:%s,  Empresa%s ' %(self.name,self.cellphone_number,self.company)

    def liked(self):
        self.__likes+=1
    
    def get_likes(self):
        return self.__likes
        
    def get_credites(self):
        return self.__likes*10
