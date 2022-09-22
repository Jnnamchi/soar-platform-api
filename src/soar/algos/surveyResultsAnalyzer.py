import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

HUGE_OPPORTUNITY = 'Huge OPPORTUNITY'
BIG_OPPORTUNITY = 'Big OPPORTUNITY'
MODEST_OPPORTUNITY = 'Modest OPPORTUNITY'

HUGE_NECESSITY = "Huge NECESSITY"
BIG_NECESSITY = "Big NECESSITY"
MODEST_NECESSITY = 'Modest NECESSITY'

LITTLE_NO_O_N = 'LITTLE OR NO OPPORTUNITY OR NECESSITY'
DONT_KNOW = "Don't Know"
NOT_APPLICABLE = 'NOT APPLICABLE OR RELEVANT'

points = {
	HUGE_OPPORTUNITY: 3,
	BIG_OPPORTUNITY: 2,
	MODEST_OPPORTUNITY: 1,
	HUGE_NECESSITY: 3,
	BIG_NECESSITY: 2,
	MODEST_NECESSITY: 1,
	LITTLE_NO_O_N: 0,
	DONT_KNOW: 0,
	NOT_APPLICABLE: 0,
}

def scoreQuestion(answer):
	if answer in points:
		return points[answer]
	return 0

opportunities = (HUGE_OPPORTUNITY, BIG_OPPORTUNITY, MODEST_OPPORTUNITY)
def addOpportunityScore(answer):
	if answer in opportunities:
		return points[answer]
	return 0

necessities = (HUGE_NECESSITY, BIG_NECESSITY, MODEST_NECESSITY)
def addNecessityScore(answer):
	if answer in necessities:
		return points[answer]
	return 0

def getSurveyResultsAnalysis(surveyAnswers, module):
	answerTally = {}
	for userId, userAnswers in surveyAnswers.items():
		for answerId, answer in userAnswers.items():
			if answerId not in answerTally:
				answerTally[answerId] = {
					"score": 0,
					"opportunityScore": 0,
					"necessityScore": 0
				}
				for point in points:
					answerTally[answerId][point] = 0
			answerTally[answerId]["score"] += scoreQuestion(answer)
			answerTally[answerId]["opportunityScore"] += addOpportunityScore(answer)
			answerTally[answerId]["necessityScore"] += addNecessityScore(answer)
			answerTally[answerId]["questionName"] = getQuestionNameFromId(answerId, module)
			if answer in points:
				answerTally[answerId][answer] += 1
	return answerTally

def getQuestionNameFromId(questionId, module):
	for page in module["survey"]["pages"]:
		for question in page["questions"]:
			if question["type"] == "matrix":
				for matrixQ in question["rows"]:
					if matrixQ["id"] == questionId:
						return matrixQ["question"]
			elif question["id"] == questionId:
				return question["name"]
	return "Could not find question"