#Programa criado devido a necessidade de geração de XML para importação do sistema Protheus TOTVS
#Importado  acessando um banco Oracle para realizar as geração de XML gravado num campo BLOB
#A Tabela Utilizada foi a SPED050  COM OS CAMPOS NFE_ID (chave da nota fiscal) e XML_SIG (XML Assinado pelo governo)
#com  a utilização de  um banco SQLITE  para registrar  a ultima nota importada.
#Criação 24/04/2020
#Autor Murilo Ramos.

import cx_Oracle
import sqlite3

#Inicia acesso ao Banco SQLlite
conn = sqlite3.connect("Notas.db")  
curso = conn.cursor() #Criação de um cursor  para acesso ao banco  Notas 

sql="SELECT recno FROM Recno"  #SQL para busca do recno, pois so tem um unico campo e o mesmo é  atualizado a cada execução

curso.execute(sql) #Executa a  query no cursor
lastNota=curso.fetchone() #Armazena o resultado

while lastNota:
    lastRecno=lastNota[0] #definindo o ultimo Recno na variavel para executar as Querys a Seguir
    lastNota = curso.fetchone()


connection = cx_Oracle.connect("usr","senha","banco") #cria a conexão  utiizando o modulo Python da Oracle cx_Oracle utilizando essa função cx_Oracle.connect é necessario
#passar como parametros o Usuario do banco, A senha do banco  e  o nome do banco (usr,senha,banco)
cursor = connection.cursor() # cria um cursor para conexão ao banco  onde  esta as notas
lastCurso =connection.cursor() # cria um cursor para conexão ao banco das notas com o objetivo de pegar a ultima nota (Não tive uma ideia melhor de como fazer dada minha inexperiencia programando)

SqlBusca="SELECT NFE_ID, XML_SIG, R_E_C_N_O_ from SPED050 WHERE  MODELO ='55' AND CNPJDEST LIKE '%inicialcnpj%' AND R_E_C_N_O_ >{}".format(lastRecno)
SqlBusca2="SELECT MAX(R_E_C_N_O_)  from SPED050 WHERE  MODELO ='55' AND CNPJDEST LIKE '%inicialcnpj%' AND R_E_C_N_O_ >={}".format(lastRecno)

#Busca as notas fiscais
cursor.execute(SqlBusca)
result = cursor.fetchone()

#Atualiza o Ultimo Recno Executando esse bloco de codigo e  fechando ele atualiza as informações no SQLITE para proxima execução.
lastCurso.execute(SqlBusca2)
lastNota= lastCurso.fetchone()
while lastNota:
    lastRecno=lastNota[0]
    lastNota = lastCurso.fetchone()

print(lastRecno)
sql='''UPDATE Recno set recno={}'''.format(lastRecno)


curso.execute(sql)
conn.commit()
lastCurso.close()


#realiza    a  consulta no resultado do SqlBusca e  a salva em result realizando um laço de repetição para  ler as informações
if result == None: 
    print("Nenhum Resultado")
    exit
else:
    while result:
        chvNF=result[0] #pegando a primeira posição que no caso é o NFE_ID para usar como nome
        teste=result[1] # Pega o campo BLOB  gravado no banco Oracle e coloca na variavel test (Ira fazer uma vez para cada passagem então se tiver 1000 notas ele vai repetir esse laço 1000 vezes)
        nomeXml=chvNF+'.xml'#Concatena o nome do arquivo XML
        superchute=teste.read() # Grava as informações do campo BLOB em uma variavel do tipo BYTE 
        
        arquivo = open('''//destino/nomedapasta/{}'''.format(nomeXml),'w+b') # abre ou cria um arquivo usando o ''w+b'' como paramentro ele vai escrever recebendo informação em BYTE
        arquivo.write(superchute) #screve o apartir da varivael superchute
        arquivo.close() #fecha o arquivo
        
        result = cursor.fetchone()
#Fecha as conexões abertas
cursor.close()
connection.close()
curso.close()
conn.close()
