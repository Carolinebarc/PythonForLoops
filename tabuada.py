i = 1 

m = int(input("Digite a tabuada: ")) 

resp = 's' 

while resp == 's': 

  while i<=10: 

    print(m, "x",i,"=",m*i) 

    i=i+1 #incremento 

  resp= input("Deseja uma nova Tabuada? [s]im ou [n]ão: ") 

  i=1 

  print("-"*40) 