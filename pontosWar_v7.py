#import requests
#import json
import auxModule as aux
import dbModule as db
'''
#myKey - Chave gerada no site da API especifica por usuario e IP.
myKey ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRlMDMwNjgyLTk3MGQtNDIwMS05MmY1LTc5NmEyOGY2MThhYSIsImlhdCI6MTU4MTUyNTYxMCwic3ViIjoiZGV2ZWxvcGVyLzdhMjFmMTQ3LWM5NzUtMDg0My01NDI1LWQ4NGI0YjBlYzFlNCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzcuMTg4LjMyLjIyMSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.494FFAFfX5vhwSrYO2lvFWcQyZgrAfNUPVQ0geAXO6HCcB4DJtWw_tFp_dxWa02KTETAE5KLblcl-N0xAyR8gg"

#arquivo de saida
exitFile = open("saida.csv",'w', encoding='utf-8-sig')

#arquivo de log
logFile = open("log.csv",'w',encoding='utf-8-sig') 

#URL utilizada para trazer informações do clã #Y8UL8YOG(Fogueteiros).
clanURL = "https://api.clashroyale.com/v1/clans/%23Y8UL8Y0G"

#Solicitação para trazer informações do clã.
reqClan = requests.get(clanURL, headers={"Accept":"application/json", "authorization":"Bearer "+myKey})

#Objeto Json com as informações do clã.
clanJson = reqClan.json()

#Lista de membros do clã
memberList = clanJson['memberList']

#URL utilizada para trazer log de guerra do cla #Y8UL8YOG(Fogueteiros).
clanWarLogURL = "https://api.clashroyale.com/v1/clans/%23Y8UL8Y0G/warlog?limit=1"

#Solicitacao para trazer log de guerra do cla
reqWarLog = requests.get(clanWarLogURL, headers={"Accept":"application/json", "authorization":"Bearer "+myKey})

#Objeto Json com as informacoes do log de guerra do cla.
warLogJson = reqWarLog.json()

#Lista de membros participantes da ultima guerra
warMemberList = warLogJson['items'][0]['participants']

#Matrix com os dados de entrada(Dados acumulados)
matrixInput = readInput()

#Imprime cabecalho
printHeader(exitFile,logFile)

#Verifica se e primeira guerra da temporada.
if len(matrixInput) == 0:
	calculateFirstWar()
else:
	calculateWar()
	
exitFile.close()
logFile.close()
print("FIM")
'''
#if __name__ == '__main__':
db.create_connection(r"db\pythonsqlite.db")
