
def getUserCompanies(db, userId):
	companies = []

	companiesDB = db.collection(u'companies').where("admins", "array_contains", userId).get()
	for company in companiesDB:
		companyDict = company.to_dict()
		companyDict["uuid"] = company.id
		companies.append(companyDict)

	companiesParticipantsDB = db.collection(u'companies').where("participants", "array_contains", userId).get()
	for company in companiesParticipantsDB:
		companyDict = company.to_dict()
		companyDict["uuid"] = company.id
		companies.append(companyDict)

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