def getAllModules(db):
	modules = db.collection(u'modules').get()

	finalModules = []
	for module in modules:
		moduleDict = module.to_dict()
		moduleDict["uuid"] = module.id
		finalModules.append(moduleDict)

	return finalModules

def getModuleById(db, moduleId):
	module = db.collection(u'modules').document(moduleId).get()
	return module.to_dict()

def addAnswerKeysToModule(module):
	for page in module["survey"]["pages"]:
		for question in page["questions"]:
			question["answer"] = []
			question["choices"] = []
			question["items"] = []
	return module