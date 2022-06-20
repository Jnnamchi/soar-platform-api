from app import app
from flask import request
from flask_cors import CORS

from .firebase import firebase

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# STEP 1: Get all user data
@app.route('/getAllUserData', methods=['GET'])
def getAllUserData():
	userId = request.args.get('userId')
	if userId == None:
		return {
			"Error": 401,
			"Message": "Must provide user Id"
		}
	return firebase.getAllUserData(userId)

@app.route('/getAllModules', methods=['GET'])
def index():
	return firebase.getAllModules()

@app.route('/getUserCompanies', methods=['GET'])
def getUserCompanies():
	userId = request.args.get('userId')
	if userId == None:
		return {
			"Error": 401,
			"Message": "Must provide user Id"
		}
	return firebase.getUserCompanies(userId)

# STEP 2: Add a company
@app.route('/addUserCompany', methods=['POST'])
def addUserCompany():
	return firebase.addUserCompany(request.get_json())

# STEP 3: Add a module to a company
@app.route('/addModuleToCompany', methods=['POST'])
def addModuleToCompany():
	return firebase.addModuleToCompany(request.get_json())

# STEP 4: Update company participants: add or remove participants
@app.route('/updateCompanyParticipants', methods=['POST'])
def updateCompanyParticipants():
	return firebase.updateCompanyParticipants(request.get_json())

# STEP 5: When a particpant completes a survey
@app.route('/updateUserSurveyAnswer', methods=['POST'])
def updateUserSurveyAnswer():
	return firebase.updateUserSurveyAnswer(request.get_json())

# STEP 6: Start the next virtual workshop for the company
@app.route('/createNextWorkshop', methods=['POST'])
def createNextWorkshop():
	return firebase.createNextWorkshop(request.get_json())

# STEP 7: When a particpant completes a workshop survey
@app.route('/updateUserWorkshopAnswers', methods=['POST'])
def updateUserWorkshopAnswers():
	return firebase.updateUserWorkshopAnswers(request.get_json())

# STEP 8: Create & start the in-person workshop for the company
@app.route('/createInPersonWorkshops', methods=['POST'])
def createInPersonWorkshops():
	return firebase.createInPersonWorkshops(request.get_json())

# STEP 9: Save the data state of the in-person workshop for the company
@app.route('/saveWorkshopState', methods=['POST'])
def saveWorkshopState():
	return firebase.saveWorkshopState(request.get_json())

# Add new route here
# @app.route('/scheduleVideoConference', methods=['POST'])
# def scheduleVideoConference():
# 	return firebase.scheduleVideoConference(request.get_json())