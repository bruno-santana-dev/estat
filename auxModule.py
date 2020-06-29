class Member:
	def __init__(self, tag, name, points, log, cardsEarned, collBattles, battles, wins):
		self.tag = tag
		self.name = name
		self.points = points
		self.log = log
		self.cardsEarned = cardsEarned
		self.collBattles = collBattles
		self.battles = battles
		self.wins = wins
		
#Metodo para selecionar pontuacao de acordo com a quantidade de cartas ganha na coleta
def collectionPoints(cardsEarned):
    switcher={
        1485:0,
        1401:0,
        1320:0,
        1980:1,
        1869:1,
        1760:1,
        2475:2,
        2337:2,
        2200:2,
        2970:3,
        2805:3,
        2640:3
        }
    return switcher.get(cardsEarned,99)

def printMember(member,exitFile,logFile):
    exitFile.write("\n")
    line = [member.name]
    line.append(str(member.points))
    exitFile.write(";".join(line))
    logFile.write("\n")
    line = [member.tag]
    line.append(member.name)
    line.append(str(member.points))
    line.append(member.log)
    line.append(str(member.cardsEarned))
    line.append(str(member.collBattles))
    line.append(str(member.battles))
    line.append(str(member.wins))
    logFile.write(";".join(line))
	
def printHeader(exitFile, logFile):
	line = ["Nome","Pontos"]
	exitFile.write(";".join(line))
	line = ["Tag","Nome","Pontos","Log","Cartas Ganhas","Batalhas Coleta","Batalhas","Vitorias"]
	logFile.write(";".join(line))

def readInput():
	matrix1 = []
	try:
		with open("input.txt",'r') as reader:
			list1 = reader.read().split("\n")
					
			for item in list1:
				matrix1.append(item.split(";"))
	except IOError:
		pass
	
	return matrix1

def calculateWar():

	listTag = []
	listPoints = []
	listNames = []

	for item in matrixInput:
		try:
			listTag.append(item[0])
			listNames.append(item[1])
			listPoints.append(item[2])
		except IndexError:
			print("Erro de indice")
			print("===Matrix")
			print(matrixInput)
			print("===Item")
			print(item)
			print("Fim do erro")

	#Verifica todos os membros do cla.
	for clanMember in memberList:
	
		#Cria o membro com a sua pontuação da base
		try:
			memberBaseIndex = listTag.index(clanMember['tag'])
		except ValueError:
			memberBaseIndex = -1

		if memberBaseIndex > -1:
			points = int(listPoints[memberBaseIndex])
		else:
			points = 0
		
		createdMember = Member(clanMember['tag'],clanMember['name'],points,"",0,0,0,0)
	
		#Verifica a pontuacao da guerra atual
		for warMember in warMemberList:
			if warMember['tag'] == clanMember['tag']:
				createdMember.cardsEarned = warMember['cardsEarned']
				createdMember.collBattles = warMember['collectionDayBattlesPlayed']
				createdMember.battles = warMember['battlesPlayed']
				createdMember.wins = warMember['wins']
				#Incluir informacoes de pontuação e log de erro nos membros
				if warMember['collectionDayBattlesPlayed'] != 3 or warMember['battlesPlayed'] == 0:
					createdMember.log = "Penalizado"
				else:
					collPoints = collectionPoints(warMember['cardsEarned'])
					if collPoints == 99:
						createdMember.log = "ERRO"
					else:
						if warMember['wins'] > 0:
							points += 3
						createdMember.points = points + collPoints
						createdMember.log = "OK"
				break
						
		#Imprime dados do membro gerado
		printMember(createdMember,exitFile,logFile)	

def calculateFirstWar():
	
	#Verifica a pontuacao da guerra atual
	for warMember in warMemberList:
		points = 0
		createdMember = Member(warMember['tag'],warMember['name'],points,"",warMember['cardsEarned'],warMember['collectionDayBattlesPlayed'],warMember['battlesPlayed'],warMember['wins'])		
		#Incluir informacoes de pontuação e log de erro nos membros
		if warMember['collectionDayBattlesPlayed'] != 3 or warMember['battlesPlayed'] == 0:
			createdMember.log = "Penalizado"
		else:
			collPoints = collectionPoints(warMember['cardsEarned'])
			if collPoints == 99:
				createdMember.log = "ERRO"
			else:
				if warMember['wins'] > 0:
					points += 3
				createdMember.points = points + collPoints
				createdMember.log = "OK"	
						
		#Imprime dados do membro gerado
		printMember(createdMember,exitFile,logFile)