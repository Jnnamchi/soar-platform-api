import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth

from . import companies
from . import modules
from . import users

# Use a service account
cred = credentials.Certificate('/Users/jnnamchi/go/src/github.com/Jnnamchi/soar-platform-api/app/firebase/credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def getAllUserData(userId):
	allModules = modules.getAllModules(db)
	userCompanies = companies.getUserCompanies(db, userId)
	userIds = companies.getAllUserIdsInCompany(userCompanies)
	return {
		"modules": allModules,
		"companies": userCompanies,
		"users": users.getAllUsersInfoFromIDs(auth, userIds)
	}

def getAllModules():
	return {
		"data": modules.getAllModules(db)
	}

def getUserCompanies(userId):
	return {
		"companies": companies.getUserCompanies(db, userId)
	}

def addUserCompany(userCompany):
	return companies.addUserCompany(db, userCompany)

def addModuleToCompany(companyAndModuleUuids):
	return companies.addModuleToCompany(db, companyAndModuleUuids)

def updateCompanyParticipants(addParticipantsInstructions):
	# 1. convert to participant ids
	participantsToAddIds = users.getUserIdsFromEmail(auth, addParticipantsInstructions["add"])
	updatedCompany = companies.addParticipantsToCompany(db, addParticipantsInstructions["companyUuid"], participantsToAddIds)
	usersInfo = users.getAllUsersInfoFromIDs(auth, participantsToAddIds)
	return {
		"company": updatedCompany,
		"users": usersInfo
	}








# For random tests on startup
# modules2 = db.collection(u'companies').where("participants", "array_contains", "vYXqTtUPwIfYtQnMu1JazQLtxxK2").get()
# finalModules = []
# for module in modules2:
# 	print(module.id)
# 	finalModules.append(module.to_dict())
# print(finalModules)