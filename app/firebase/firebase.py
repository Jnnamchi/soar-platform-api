import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth

from . import companies
from . import modules
from . import users
from . import workshopManager
from . import inPersonWorkshopManager

# Use a service account
# cred = credentials.Certificate('/home/jnnamchi/soar-platform-api/app/firebase/credentials.json')
cred = credentials.Certificate('/Users/jnnamchi/go/src/github.com/Jnnamchi/soar-platform-api/app/firebase/credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# STEP 1: Get all user data
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

# STEP 2: Add a company
def addUserCompany(userCompany):
	return companies.addUserCompany(db, userCompany)

# STEP 3: Add a module to a company
def addModuleToCompany(companyAndModuleUuids):
	return companies.addModuleToCompany(db, companyAndModuleUuids)

# STEP 4: Update company participants: add or remove participants
def updateCompanyParticipants(addParticipantsInstructions):
	# 1. convert to participant ids
	participantsToAddIds = users.getUserIdsFromEmail(auth, addParticipantsInstructions["add"])
	updatedCompany = companies.addParticipantsToCompany(db, addParticipantsInstructions["companyUuid"], participantsToAddIds)
	usersInfo = users.getAllUsersInfoFromIDs(auth, participantsToAddIds)
	return {
		"company": updatedCompany,
		"users": usersInfo
	}

# STEP 4: When a particpant completes a survey
def updateUserSurveyAnswer(updateData):
	return {
		"company": companies.updateUserSurveyAnswer(db, updateData["companyUuid"], updateData["moduleUuid"], updateData["uuid"], updateData["answers"])
	}

# STEP 5: Start the next virtual workshop for the company
def createNextWorkshop(data):
	updatedCompany = workshopManager.addNextWorkshopToCompany(data["company"], data["moduleId"])
	companies.updateCompanyData(db, updatedCompany)
	return updatedCompany

# STEP 6: When a particpant completes a workshop survey
def updateUserWorkshopAnswers(data):
	return companies.updateUserWorkshopAnswers(db, data["userId"], data["companyUuid"], data["moduleUuid"], data["answers"])

# STEP 7: Create & start the in-person workshop for the company
def createInPersonWorkshops(data):
	module = modules.getModuleById(db, data["moduleId"])
	updatedCompany = inPersonWorkshopManager.addModuleInPersonWorkshops(data["company"], data["moduleId"], module)
	companies.updateCompanyData(db, updatedCompany)
	return updatedCompany

# STEP 8: Save the data state of the in-person workshop for the company
def saveWorkshopState(data):
	updatedCompany = companies.getCompanyById(db, data["companyId"])
	updatedCompany = inPersonWorkshopManager.saveWorkshopState(updatedCompany, data["moduleId"], data["workshops"])
	companies.updateCompanyData(db, updatedCompany)
	return updatedCompany

# For random tests on startup
# modules2 = db.collection(u'companies').where("participants", "array_contains", "vYXqTtUPwIfYtQnMu1JazQLtxxK2").get()
# finalModules = []
# for module in modules2:
# 	print(module.id)
# 	finalModules.append(module.to_dict())
# print(finalModules)