GREATER_THAN_TEN_PERCENT = 'Greater than 10%'
SEVEN_TO_TEN_PERCENT = '7.5 - 10%'
FIVE_TO_SEVEN_PERCENT = '5 - 7.5%'
TWO_TO_FIVE_PERCENT = '2.5 - 5%'
ONE_TO_TWO_PERCENT = '1 - 2.5%'
HUGE = "Huge"
VERY_BIG = "Very Big"
BIG = "Big"
MODEST = "Modest"
LITTLE_OR_NONE = "Little or None"

points = {
	GREATER_THAN_TEN_PERCENT: 5,
	SEVEN_TO_TEN_PERCENT: 4,
	FIVE_TO_SEVEN_PERCENT: 3,
	TWO_TO_FIVE_PERCENT: 2,
	ONE_TO_TWO_PERCENT: 1,
	HUGE: 5,
	VERY_BIG: 4,
	BIG: 3,
	MODEST: 2,
	LITTLE_OR_NONE: 1,
}

workshopRounds = {
	"round-1": {
		"name": "Virtual Workshop #1",
		"description": "Size of Opportunity",
		"takeAnswersFrom": "answerAnalysis",
		"sortKeyName": "opportunityScore",
		"takeTopN": 15,
		"questions": [{
			"name": "Opporutnity to grow annual Sales Revenue in 2-3 years (measured as a % of current annual sales)",
			"type": "matrix",
			"columns": [ GREATER_THAN_TEN_PERCENT, SEVEN_TO_TEN_PERCENT, FIVE_TO_SEVEN_PERCENT, TWO_TO_FIVE_PERCENT, ONE_TO_TWO_PERCENT ],
		},{
			"name": "Opporutnity to grow Gross Margin % in 2-3 years (measured by comparison to current average Gross Margin %)",
			"type": "matrix",
			"columns": [ GREATER_THAN_TEN_PERCENT, SEVEN_TO_TEN_PERCENT, FIVE_TO_SEVEN_PERCENT, TWO_TO_FIVE_PERCENT, ONE_TO_TWO_PERCENT ],
		},{
			"name": "Impact on company's Differentiation and Competitive Advantage",
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
		}],
		"points": {
			GREATER_THAN_TEN_PERCENT: 5,
			SEVEN_TO_TEN_PERCENT: 4,
			FIVE_TO_SEVEN_PERCENT: 3,
			TWO_TO_FIVE_PERCENT: 2,
			ONE_TO_TWO_PERCENT: 1,
			HUGE: 5,
			VERY_BIG: 4,
			BIG: 3,
			MODEST: 2,
			LITTLE_OR_NONE: 1,
		},
		"next-round": "round-2"
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
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
		},{
			"name": "Cost to implement",
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
		},{
			"name": "Timeframe to achieve Scale & Profitability",
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
		# "next-round": "round-2"
	}
	# TODO: Round 3 with necessities only
}

def createNewQuestion():
	return {
		"name": "",
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
	return topAnswers[:workshopRounds[nextWorkshopRound]["takeTopN"]]

def addNextWorkshopToCompany(companyData, moduleId):

	if moduleId not in companyData["virtualWorkshops"]:
		companyData["virtualWorkshops"][moduleId] = {}
	nextWorkshopRound = len(companyData["virtualWorkshops"][moduleId].keys()) + 1
	nextWorkshopRoundName = "round-" + str(nextWorkshopRound)
	# TODO: else when virtualWorkshops already in company data
	workshopNumber = str(len(companyData["virtualWorkshops"][moduleId].keys()) + 1)
	# companyData["virtualWorkshops"][moduleId][workshopNumber] = createVirtualWorkshop(nextWorkshopRoundName, companyData["topAnswers"])
	companyData["virtualWorkshops"][moduleId][workshopNumber] = createVirtualWorkshop(nextWorkshopRoundName, getAnswersUsedForNextWorkshop(companyData, moduleId, nextWorkshopRoundName))

	return companyData

def addWorkshopAnalysis(companyData):
	for moduleId, virtualWorkshopStages in companyData["virtualWorkshops"].items():
		for stageNumber, virtualWorkshopStage in virtualWorkshopStages.items():
			virtualWorkshopStage["answerAnalysis"] = runWorkshopAnswerAnalysis(virtualWorkshopStage["moduleAnswers"], stageNumber)

def runWorkshopAnswerAnalysis(moduleAnswers, stageNumber):
	answerTally = {}
	for userId, userAnswers in moduleAnswers.items():
		for questionNumber, answers in userAnswers.items():
			for initiativeId, answer in answers.items():
				if initiativeId not in answerTally:
					answerTally[initiativeId] = {
						"score": 0
					}
				if answer in workshopRounds["round-" + str(stageNumber)]["points"]:
					if answer not in answerTally[initiativeId]:
						answerTally[initiativeId][answer] = 0
					answerTally[initiativeId][answer] += 1
					answerTally[initiativeId]["score"] += workshopRounds["round-" + str(stageNumber)]["points"][answer]
	return answerTally