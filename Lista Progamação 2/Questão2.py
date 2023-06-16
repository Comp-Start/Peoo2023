class Disciplina:
  def __init__(self):
    self.__nome = ''
    self.__nota1 = 0
    self.__nota2 = 0
    self.__nota3 = 0
    self.__nota4 = 0
    self.__notaFinal = 0
  def set_nome(self, s):
    self.__nome = s
  def set_nota1(self, n):
    if  0 <= n <= 100: self.__nota1 = n
    else: raise ValueError()  
  def set_nota2(self, n):
    if  0 <= n <= 100: self.__nota2 = n
    else: raise ValueError() 
  def set_nota3(self, n):
    if  0 <= n <= 100: self.__nota3 = n
    else: raise ValueError() 
  def set_nota4(self, n):
    if  0 <= n <= 100: self.__nota4 = n
    else: raise ValueError()   
  def set_nota_final(self, n):
    if  0 <= n <= 100: self.__notaFinal = n
    else: raise ValueError()  
  def get_nome(self):
    return self.__nome
  def get_nota1(self):
    return self.__nota1
  def get_nota2(self):
    return self.__nota2
  def get_nota3(self):
    return self.__nota3
  def get_nota4(self):
    return self.__nota4
  def get_nota_final(self):
    return self.__nota_final
  def calc_media_parcial(self):    
    return (self.__nota1*2+self.__nota2*2+self.__nota3*3+self.__nota4*3)/10
  def calc_media_final(self):
    return (self.calc_media_parcial() + self.__notaFinal)/2
class UI:
  @staticmethod
  def main():
    x = Disciplina()
    x.set_nome(input('Digite o nome da disciplina: \n'))
    x.get_nome()
    x.set_nota1(int(input('Digite a nota 1: \n)))
    x.get_nota1()                      
    x.set_nota2(int(input('Digite a nota 2: \n)))
    x.get_nota2()                   
    x.set_nota3(int(input('Digite a nota 3: \n)))
    x.get_nota3()                      
    x.set_nota4(int(input('Digite a nota 4: \n)))   
    x.get_nota4()
 UI.main()                         
                          
                          
