from app import app
from flask import request
from flask_cors import CORS

from .firebase import firebase

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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

@app.route('/addUserCompany', methods=['POST'])
def addUserCompany():
	return firebase.addUserCompany(request.get_json())

@app.route('/addModuleToCompany', methods=['POST'])
def addModuleToCompany():
	return firebase.addModuleToCompany(request.get_json())

@app.route('/updateCompanyParticipants', methods=['POST'])
def updateCompanyParticipants():
	return firebase.updateCompanyParticipants(request.get_json())

@app.route('/updateUserSurveyAnswer', methods=['POST'])
def updateUserSurveyAnswer():
	return firebase.updateUserSurveyAnswer(request.get_json())

@app.route('/createNextWorkshop', methods=['POST'])
def createNextWorkshop():
	return firebase.createNextWorkshop(request.get_json())