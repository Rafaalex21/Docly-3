import os
#caminho onde está salvo a pasta da tarefa
path = "C:/Users/Rafael/Desktop/tarefa-3"
dir_list = os.listdir(path)
print("Arquivos e diretórios em", path,":")
#printa os arquivos da pasta
print(dir_list)


#O código abaixo irá escrever um novo arquivo e o conteúdo dentro dele será o conteúdo da pasta
a = open("arquivo-1", "a")

for path, subdirs, files in os.walk(r'/Users/Rafael/Desktop/tarefa-3'):
    for filename in files:
        a.write(filename + os.linesep)

#Creio que tenha feito o que a tarefa pediu, ficou meio confuso para mim a descrição do que foi pedido