#funcao para verificar se eh primo ou nao
def verif_primo(num):
    
    if num <= 1: #num menores que 2 nao sao primos
        return False
    
    #verificar se num eh / por algum deles
    i = 2
    while i < num:
        if num % i == 0:   #resto zero
            return False
        i += 1
        
    # Se o num não for / por nenhum num entre 2 e num-1 ele eh primo
    return True


primos = []   #Cria uma lista para armazenar os primos


num = 1    #Atribui 1 no num

#loop para verificar todos os num de 1 a 250
while num <= 250:
    # Verifica se o num atual eh primo usando a função verif_primo
    if verif_primo(num):
        
        primos.append(num) # Se o num for primo vai para primos
        
    # Incrementa a variavel do loop
    num += 1

# Abre o arquivo results.txt em modo de escrita e escreve os num primos nele, um por linha
with open('results.txt', 'w') as file:
    for p in primos:
        file.write(str(p) + '\n')

# Exibir
print("Os numeros primos entre 1 e 250 sao: ",primos)
