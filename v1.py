class Boletin:
  def __init__(self, Nome_do_aluno, Historia, Geografia, Matematica, Fisica, Ingles):
    self.Nome_do_aluno = Nome_do_aluno
    self.Historia = Historia 
    self.Geografia = Geografia
    self.Matematica = Matematica 
    self.Fisica = Fisica 
    self.Ingles = Ingles
 
  def Ver_Resultado_H(self):
    if self.Historia > 7:
      print("Você passou: ")
    else:
      print(f"Você reprovou: ") 

  def Ver_Resultado_G(self):
    if self.Geografia > 7:
      print(f"Você passou: ")
    else:
      print(f"Você reprovou: ")

  def Ver_Resultado_M(self): 
    if self.Matematica > 7: 
      print(f"Você passou: ")
    else:
      print(f"Você reprovou: ") 

  def Ver_Resultado_F(self):
    if self.Fisica > 7:
      print(f"Você passou: ")
    else:
      print(f"Você reprovou: ")
       
  def Ver_Resultado_I(self):
    if self.Ingles > 7:
      print(f"Você passou: ")
    else:
      print(f"Você reprovou: ")

def main():
     Nome_do_aluno = input("Insira seu Nome: ")
     Historia = float(input(f"Insira a nota de {Nome_do_aluno} na disciplina de Historia: "))
     Geografia = float(input(f"Insira a nota de {Nome_do_aluno} na disciplina de Geografia: "))
     Matematica = float(input(f"Insira a nota de {Nome_do_aluno} na disciplina de Matematica: "))
     Fisica = float(input(f"Insira a nota de {Nome_do_aluno} na disciplina de Fisica: "))
     Ingles= float(input(f"Insira a nota de {Nome_do_aluno} na disciplina de Ingles: "))

     boletim1 = Boletin(Nome_do_aluno,Historia,Geografia,Matematica,Fisica,Ingles)
     boletim1.Ver_Resultado_H()
     boletim1.Ver_Resultado_G()
     boletim1.Ver_Resultado_M()
     boletim1.Ver_Resultado_F()
     boletim1.Ver_Resultado_I()

if __name__ == "__main__":
     main()      

          
  
