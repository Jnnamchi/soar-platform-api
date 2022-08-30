GREATER_THAN_TEN_PERCENT = 'Greater than 10%'
SEVEN_TO_TEN_PERCENT = '7.5 - 10%'
FIVE_TO_SEVEN_PERCENT = '5 - 7.5%'
TWO_TO_FIVE_PERCENT = '2.5 - 5%'
ONE_TO_TWO_PERCENT = '1 - 2.5%'
HUGE = 'Huge'
VERY_BIG = 'Very Big'
BIG = 'Big'
MODEST = 'Modest'
SMALL = 'Small'
LITTLE_OR_NONE = 'Little or None'
DONT_KNOW_N_A = "Don't Know or N/A"

EXTREMELY_NECESSARY = 'Extremely Necessary'
VERY_NECESSARY = 'Very Necessary'
MODERATELY_NECESSARY = 'Moderately Necessary'
SLIGHTLY_NECESSARY = 'Slightly Necessary'
CAN_WAIT = 'Can Wait'

points = {
	GREATER_THAN_TEN_PERCENT: 5,
	SEVEN_TO_TEN_PERCENT: 4,
	FIVE_TO_SEVEN_PERCENT: 3,
	TWO_TO_FIVE_PERCENT: 2,
	ONE_TO_TWO_PERCENT: 1,
	HUGE: 5,
	VERY_BIG: 4,
	BIG: 4,
	MODEST: 3,
	SMALL: 2,
	LITTLE_OR_NONE: 1,
	DONT_KNOW_N_A: 0,
}

pointsOverrideIds = ('VW1-DDCI', 'VW1-CTI', 'VW1-TTI')
pointsOverrides = {
	HUGE: 1,
	BIG: 2,
	MODEST: 3,
	SMALL: 4,
	LITTLE_OR_NONE: 5,
	DONT_KNOW_N_A: 0
}

workshopRounds = {
	"round-1": {
		"name": "Virtual Workshop #1",
		"description": "Size of Opportunity",
		"takeAnswersFrom": "answerAnalysis",
		"sortKeyName": "opportunityScore",
		"takeTopN": 15,
		"questions": [{
			"name": "Potential to improve Profitability - via increased Sales Revenue or Gross Profit Margins and/or reduction of Operating Expenses or Cost of Goods Sold",
			"id": "VW1-PIPISRGPM",
			"type": "matrix",
			"columns": [ HUGE, BIG, MODEST, SMALL, LITTLE_OR_NONE, DONT_KNOW_N_A ],
		},{
			"name": "Potential to improve Business Effectiveness - by improving Culture, Morale, Productivity, Organizational Effectiveness, Information Systems, Quality, Controls, Brand Name, Market Differentiation or Competitive Advantage",
			"id": "VW1-PIBEICMPOE",
			"type": "matrix",
			"columns": [ HUGE, BIG, MODEST, SMALL, LITTLE_OR_NONE, DONT_KNOW_N_A ],
		},{
			"name": "Degree of Difficulty and/or Complexity to implement",
			"id": "VW1-DDCI",
			"type": "matrix",
			"columns": [ HUGE, BIG, MODEST, SMALL, LITTLE_OR_NONE, DONT_KNOW_N_A ],
		},{
			"name": "Cost to implement",
			"id": "VW1-CTI",
			"type": "matrix",
			"columns": [ HUGE, BIG, MODEST, SMALL, LITTLE_OR_NONE, DONT_KNOW_N_A ],
		},{
			"name": "Timeframe to implement",
			"id": "VW1-TTI",
			"type": "matrix",
			"columns": [ HUGE, BIG, MODEST, SMALL, LITTLE_OR_NONE, DONT_KNOW_N_A ],
		},{
			"name": "Degree of Urgency to implement",
			"id": "VW1-DUI",
			"type": "matrix",
			"columns": [ HUGE, BIG, MODEST, SMALL, LITTLE_OR_NONE, DONT_KNOW_N_A ],
		},{
			"name": "Degree of downside Risk if not implemented",
			"id": "VW1-DDRINI",
			"type": "matrix",
			"columns": [ HUGE, BIG, MODEST, SMALL, LITTLE_OR_NONE, DONT_KNOW_N_A ],
		}],
		"points": {
			GREATER_THAN_TEN_PERCENT: 5,
			SEVEN_TO_TEN_PERCENT: 4,
			FIVE_TO_SEVEN_PERCENT: 3,
			TWO_TO_FIVE_PERCENT: 2,
			ONE_TO_TWO_PERCENT: 1,
			HUGE: 5,
			VERY_BIG: 4,
			BIG: 4,
			MODEST: 3,
			SMALL: 2,
			LITTLE_OR_NONE: 1,
			DONT_KNOW_N_A: 0
		},
		# "next-round": "round-2"
	},
	"round-2": {
		"name": "Virtual Workshop #2",
		"description": "Opportunity Implementation Challenges",
		"takeAnswersFrom": "virtualWorkshops",
		"takeVirtualWorkshop": "1",
		"sortKeyName": "score",
		"takeTopN": 15,
		"questions": [{
			"name": "Degree of Difficulty, Complexity, Learning Curve to implement",
			"id": "VW2-DDCLCI",
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
		},{
			"name": "Cost to implement",
			"id": "VW2-CTI",
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
		},{
			"name": "Timeframe to achieve Scale & Profitability",
			"id": "VW2-TASP",
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
		}],
		"points": {
			HUGE: 1,
			VERY_BIG: 2,
			BIG: 3,
			MODEST: 4,
			LITTLE_OR_NONE: 5,
		},
		"next-round": "round-3"
	},
	"round-3": {
		"name": "Virtual Workshop #3",
		"description": "Necessities",
		"takeAnswersFrom": "answerAnalysis",
		"sortKeyName": "necessityScore",
		"takeTopN": 15,
		"questions": [{
			"name": "Extent of Necessity",
			"id": "VW3-EON",
			"type": "matrix",
			"columns": [ EXTREMELY_NECESSARY, VERY_NECESSARY, MODERATELY_NECESSARY, SLIGHTLY_NECESSARY, CAN_WAIT ],
		},{
			"name": "Degree of Difficulty, Complexity to Implement Necessity",
			"id": "VW3-DDCIN",
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
		},{
			"name": "Cost to Implement Necessity",
			"id": "VW2-TASP",
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
		}],
		"points": {
			EXTREMELY_NECESSARY: 5,
			VERY_NECESSARY: 4,
			MODERATELY_NECESSARY: 3,
			SLIGHTLY_NECESSARY: 2,
			CAN_WAIT: 1,
			HUGE: 1,
			VERY_BIG: 2,
			BIG: 3,
			MODEST: 4,
			LITTLE_OR_NONE: 5,
		},
		# "next-round": "round-3"
	}
}

def createNewQuestion():
	return {
		"name": "",
		"id": "",
		"type": "",
		"columns": [],
		"rows": [],
		"answer": [],
		"choices": [],
		"items": []
	}

def createVirtualWorkshop(workshopRoundName, topAnswers):
	workshopRound = workshopRounds[workshopRoundName]
	surveyPages = []
	for question in workshopRound["questions"]:
		newQuestion = createNewQuestion()
		newQuestion["name"] = question["name"]
		newQuestion["id"] = question["id"]
		newQuestion["type"] = question["type"]
		newQuestion["columns"] = question["columns"]
		for answer in topAnswers:
			newQuestion["rows"].append({
				"id": answer["id"],
				"question": answer["questionName"],
				"answer": "",
			})
		page = {
			"name": "Workshop Question",
			"questions": [
				newQuestion
			]
		}
		surveyPages.append(page)
	return {
		"title": workshopRound["name"],
		"survey": {
			"title": workshopRound["name"],
			"pages": surveyPages
		},
		"moduleAnswers": {},
		"answerAnalysis": {},
		"hasNextWorkshop": "next-round" in workshopRound
	}

def getAnswersUsedForNextWorkshop (companyData, moduleId, nextWorkshopRound):
	answers = []
	takeAnswersFrom = workshopRounds[nextWorkshopRound]["takeAnswersFrom"]
	companyAnswers = companyData[takeAnswersFrom][moduleId]
	if takeAnswersFrom == "virtualWorkshops":
		workshopRoundToTake = workshopRounds[nextWorkshopRound]["takeVirtualWorkshop"]
		companyAnswers = companyAnswers[workshopRoundToTake]["answerAnalysis"]
	for answerId, answer in companyAnswers.items():
		if answer["score"] > 0:
			answers.append({"id": answerId} | answer) # Merge dictionaries
	topAnswers = sorted(answers, key=lambda answer: answer[workshopRounds[nextWorkshopRound]["sortKeyName"]], reverse=True)
	finalAnswers = []
	for i in range(workshopRounds[nextWorkshopRound]["takeTopN"]):
		finalAnswer = topAnswers[i]
		if finalAnswer[workshopRounds[nextWorkshopRound]["sortKeyName"]] > 0:
			finalAnswers.append(finalAnswer)
	return finalAnswers

def addNextWorkshopToCompany(companyData, moduleId):

	if moduleId not in companyData["virtualWorkshops"]:
		companyData["virtualWorkshops"][moduleId] = {}
	nextWorkshopRound = len(companyData["virtualWorkshops"][moduleId].keys()) + 1
	nextWorkshopRoundName = "round-" + str(nextWorkshopRound)
	# TODO: else when virtualWorkshops already in company data
	workshopNumber = str(len(companyData["virtualWorkshops"][moduleId].keys()) + 1)
	companyData["virtualWorkshops"][moduleId][workshopNumber] = createVirtualWorkshop(nextWorkshopRoundName, getAnswersUsedForNextWorkshop(companyData, moduleId, nextWorkshopRoundName))

	return companyData

def addWorkshopAnalysis(companyData):
	for moduleId, virtualWorkshopStages in companyData["virtualWorkshops"].items():
		for stageNumber, virtualWorkshopStage in virtualWorkshopStages.items():
			virtualWorkshopStage["answerAnalysis"] = runWorkshopAnswerAnalysis(virtualWorkshopStages, virtualWorkshopStage["moduleAnswers"], stageNumber, companyData["answerAnalysis"][moduleId])

def getPreviousWorkshopInitiativeScore(virtualWorkshopStages, stageNumber, companyIntialAnswerAnalysis, initiativeId):
	stageNumberInt = int(stageNumber)
	workshopRoundSettings = workshopRounds["round-" + stageNumber]
	takeAnswersFrom = workshopRoundSettings["takeAnswersFrom"]
	if takeAnswersFrom == "virtualWorkshops":
		if initiativeId in virtualWorkshopStages[str(stageNumberInt - 1)]["answerAnalysis"]:
			return virtualWorkshopStages[str(stageNumberInt - 1)]["answerAnalysis"][initiativeId]["score"]
	else:
		return companyIntialAnswerAnalysis[initiativeId]["score"]
	return 0

def runWorkshopAnswerAnalysis(virtualWorkshopStages, moduleAnswers, stageNumber, companyIntialAnswerAnalysis):
	stageNumberInt = int(stageNumber)
	answerTally = {}
	for userId, userAnswers in moduleAnswers.items():
		for questionId, answers in userAnswers.items():
			for initiativeId, answer in answers.items():
				if initiativeId not in answerTally:
					previousScore = getPreviousWorkshopInitiativeScore(virtualWorkshopStages, stageNumber, companyIntialAnswerAnalysis, initiativeId)
					answerTally[initiativeId] = {
						"score": previousScore
					}
				if questionId not in answerTally[initiativeId]:
					answerTally[initiativeId][questionId] = {}
				if answer in workshopRounds["round-" + str(stageNumber)]["points"]:
					if answer not in answerTally[initiativeId][questionId]:
						answerTally[initiativeId][questionId][answer] = 0
					answerTally[initiativeId][questionId][answer] += 1 # Count how many times the specific answer was given for a particular initiative
					if initiativeId in pointsOverrideIds:
						answerTally[initiativeId]["score"] += pointsOverrides[answer]
					else:
						answerTally[initiativeId]["score"] += workshopRounds["round-" + str(stageNumber)]["points"][answer]
	return answerTally