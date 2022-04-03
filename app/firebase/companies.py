from ..algos import testGetter

def getModuleAnalysis(companyDict):
	companyDict["answerAnalysis"] = {}
	for answerId in companyDict["moduleAnswers"]:
		companyDict["answerAnalysis"][answerId] = testGetter.getSurveyResultsAnalysis(companyDict["moduleAnswers"][answerId])

def getUserCompanies(db, userId):
	companies = []
	addedCompanies = set()

	companiesDB = db.collection(u'companies').where("admins", "array_contains", userId).get()
	companiesParticipantsDB = db.collection(u'companies').where("participants", "array_contains", userId).get()
	for company in companiesDB + companiesParticipantsDB:
		if company.id not in addedCompanies:
			companyDict = company.to_dict()
			companyDict["uuid"] = company.id
			getModuleAnalysis(companyDict)
			companies.append(companyDict)
			addedCompanies.add(company.id)

	return companies

def addUserCompany(db, userCompany):
	del userCompany["uuid"]
	db.collection(u'companies').add(userCompany)
	return "Success"

def addModuleToCompany(db, companyAndModuleUuids):
	companyUuid = companyAndModuleUuids["companyUuid"]
	moduleUuid = companyAndModuleUuids["moduleUuid"]
	company = db.collection(u'companies').document(companyUuid).get()
	companyDict = company.to_dict()
	companyDict["modules"].append(moduleUuid)
	companyDict["uuid"] = company.id
	db.collection(u'companies').document(companyUuid).update(companyDict)

	return companyDict

def getAllUserIdsInCompany(companiesList):
	userIds = []
	for companyDict in companiesList:
		userIds.extend(companyDict["participants"])
		userIds.extend(companyDict["admins"])
	return list(set(userIds))

def addParticipantsToCompany(db, companyUuid, participantIds):
	company = db.collection(u'companies').document(companyUuid).get()
	companyDict = company.to_dict()
	for participantId in participantIds:
		if participantId not in companyDict["participants"]:
			companyDict["participants"].append(participantId)
	companyDict["uuid"] = company.id
	db.collection(u'companies').document(companyUuid).update(companyDict)
	return companyDict

def updateUserSurveyAnswer(db, companyUuid, moduleUuid, userUuid, answers):
	company = db.collection(u'companies').document(companyUuid).get()
	companyDict = company.to_dict()
	if moduleUuid not in companyDict["moduleAnswers"]:
		companyDict["moduleAnswers"][moduleUuid] = {
			userUuid: answers
		}
	else:
		companyDict["moduleAnswers"][moduleUuid][userUuid] = answers
	db.collection(u'companies').document(companyUuid).update(companyDict)
	return companyDict

def updateCompanyData(db, companyData):
	companyUuid = companyData["uuid"]
	db.collection(u'companies').document(companyUuid).update(companyData)
	return companyData