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


workshopRounds = {
	"round-1": {
		"name": "Virtual Workshop #1",
		"questions": [{
			"name": "Opporutnity to grow annual Sales Revenue in 2-3 years (measured as a % of current annual sales)",
			"type": "matrix",
			"columns": [ GREATER_THAN_TEN_PERCENT, SEVEN_TO_TEN_PERCENT, FIVE_TO_SEVEN_PERCENT, TWO_TO_FIVE_PERCENT, ONE_TO_TWO_PERCENT ],
			"points": {
				GREATER_THAN_TEN_PERCENT: 5,
				SEVEN_TO_TEN_PERCENT: 4,
				FIVE_TO_SEVEN_PERCENT: 3,
				TWO_TO_FIVE_PERCENT: 2,
				ONE_TO_TWO_PERCENT: 1
			}
		},{
			"name": "Opporutnity to grow Gross Margin % in 2-3 years (measured by comparison to current average Gross Margin %)",
			"type": "matrix",
			"columns": [ GREATER_THAN_TEN_PERCENT, SEVEN_TO_TEN_PERCENT, FIVE_TO_SEVEN_PERCENT, TWO_TO_FIVE_PERCENT, ONE_TO_TWO_PERCENT ],
			"points": {
				GREATER_THAN_TEN_PERCENT: 5,
				SEVEN_TO_TEN_PERCENT: 4,
				FIVE_TO_SEVEN_PERCENT: 3,
				TWO_TO_FIVE_PERCENT: 2,
				ONE_TO_TWO_PERCENT: 1
			}
		},{
			"name": "Impact on company's Differentiation and Competitive Advantage",
			"type": "matrix",
			"columns": [ HUGE, VERY_BIG, BIG, MODEST, LITTLE_OR_NONE ],
			"points": {
				HUGE: 5,
				VERY_BIG: 4,
				BIG: 3,
				MODEST: 2,
				LITTLE_OR_NONE: 1
			}
		}],
		"next-round": "round-2"
	}
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
				"id": answer["id"] + "-" + workshopRoundName,
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
		"moduleAnswers": {}
	}

def addNextWorkshopToCompany(companyData, moduleId):
	if moduleId not in companyData["virtualWorkshops"]:
		companyData["virtualWorkshops"][moduleId] = {}
		nextWorkshopRound = "round-1"
	# TODO: else when virtualWorkshops already in company data
	workshopNumber = str(len(companyData["virtualWorkshops"][moduleId].keys()) + 1)
	companyData["virtualWorkshops"][moduleId][workshopNumber] = createVirtualWorkshop(nextWorkshopRound, companyData["topAnswers"])

	return companyData