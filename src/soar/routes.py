from flask import request
from flask import Blueprint

from .firebase import firebase

soar = Blueprint('soar', __name__, url_prefix='/')


# STEP 1: Get all user data
@soar.route('/getAllUserData', methods=['GET'])
def getAllUserData():
	userId = request.args.get('userId')
	if userId == None:
		return {
			"Error": 401,
			"Message": "Must provide user Id"
		}
	return firebase.getAllUserData(userId)


@soar.route('/getAllModules', methods=['GET'])
def index():
	return firebase.getAllModules()


@soar.route('/getUserCompanies', methods=['GET'])
def getUserCompanies():
	userId = request.args.get('userId')
	if userId == None:
		return {
			"Error": 401,
			"Message": "Must provide user Id"
		}
	return firebase.getUserCompanies(userId)


# STEP 2: Add a company
@soar.route('/addUserCompany', methods=['POST'])
def addUserCompany():
	return firebase.addUserCompany(request.get_json())


# STEP 3: Add a module to a company
@soar.route('/addModuleToCompany', methods=['POST'])
def addModuleToCompany():
	return firebase.addModuleToCompany(request.get_json())


# STEP 4: Update company participants: add or remove participants
@soar.route('/updateCompanyParticipants', methods=['POST'])
def updateCompanyParticipants():
	return firebase.updateCompanyParticipants(request.get_json())


# STEP 5: When a particpant completes a survey
@soar.route('/updateUserSurveyAnswer', methods=['POST'])
def updateUserSurveyAnswer():
	return firebase.updateUserSurveyAnswer(request.get_json())


# STEP 6: Start the next virtual workshop for the company
@soar.route('/createNextWorkshop', methods=['POST'])
def createNextWorkshop():
	return firebase.createNextWorkshop(request.get_json())


# STEP 7: When a particpant completes a workshop survey
@soar.route('/updateUserWorkshopAnswers', methods=['POST'])
def updateUserWorkshopAnswers():
	return firebase.updateUserWorkshopAnswers(request.get_json())


# STEP 8: Create & start the in-person workshop for the company
@soar.route('/createInPersonWorkshops', methods=['POST'])
def createInPersonWorkshops():
	return firebase.createInPersonWorkshops(request.get_json())


# STEP 9: Save the data state of the in-person workshop for the company
@soar.route('/saveWorkshopState', methods=['POST'])
def saveWorkshopState():
	return firebase.saveWorkshopState(request.get_json())
