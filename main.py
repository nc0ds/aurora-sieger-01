# - Temperatura interna (entre 18 a 35)
# - Temperatura externa (entre -5 a 30)
# - Integridade estrutural (0/1)
# - Níveis de energia (%) (entre 5 e 25)
# - Pressão dos tanques (entre 80 e 160)
# - Status dos módulos críticos (0/1)

import time


def contagem_regressiva(tempo, mensagem):
  contagem = tempo

  while(contagem > 0):
    print(f"{contagem} segundos...")
    time.sleep(1)
    contagem -= 1

  print (mensagem)

def painel (temperatura_Interna, temperatura_Externa, integridade_Estrutural, niveis_de_energia, pressao_de_energia, Status_dos_modulos_criticos):
  print (f" Temperatura Interna= { temperatura_Interna}\n Temperatura Externa= {temperatura_Externa}\n Integridade Estrutural= {integridade_Estrutural}\n Niveis de Energia= {niveis_de_energia}\n Pressão de Energia= {pressao_de_energia}\n Status dos Modulos Criticos= {Status_dos_modulos_criticos}\n")   


def main():
  temperaturaInterna = 24
  temperaturaExterna = 800
  integridadeEstrutural = True
  niveisDeEnergia = 50
  pressaoDosTanques = 120
  statusDosModulosCriticos = True
  decolar = True

  if temperaturaInterna < 24 or temperaturaInterna > 24:
    decolar = False
        
  if temperaturaExterna < 800 or temperaturaExterna > 800:
    decolar = False

  if integridadeEstrutural == False:
    decolar = False
        
  if niveisDeEnergia < 50 or niveisDeEnergia > 50:
    decolar = False

  if pressaoDosTanques < 120 or pressaoDosTanques > 120:
    decolar = False
    
  if statusDosModulosCriticos == False:
    decolar = False
    
  if decolar == True:
    contagem_regressiva(5, "DECOLAR")
    print (" Os valores estão de acordo para uma decolagem segura, apertem os cintos!!!")
    painel(24, 800, False, 50, 120, False)
   
  

  else:
    print("Decolagem Abortada!!")
    print("Os valores não estão de acordo!")
   

if __name__ == "__main__":
  main()
