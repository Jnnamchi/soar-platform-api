import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

SIGNIFICANT_OPPORUTNITY = 'Significant OPPORTUNITY'
MODEST_OPPORTUNITY = 'Modest OPPORTUNITY'
SIGNIFICANT_NECESSITY = 'Significant NECESSITY'
MODEST_NECESSITY = 'Modest NECESSITY'
LITTLE_NO_O_N = 'LITTLE OR NO OPPORTUNITY OR NECESSITY'
DONT_KNOW = "Don't Know"
NOT_APPLICABLE = 'NOT APPLICABLE OR RELEVANT'

points = {
	SIGNIFICANT_OPPORUTNITY: 3,
	MODEST_OPPORTUNITY: 2,
	SIGNIFICANT_NECESSITY: 3,
	MODEST_NECESSITY: 2,
	LITTLE_NO_O_N: 0,
	DONT_KNOW: 0,
	NOT_APPLICABLE: 0,
}

def scoreQuestion(answer):
	if answer in points:
		return points[answer]
	return 0

# growthModuleUuid = 'weHvXJGF3i5qgNfjFAN1'
# cred = credentials.Certificate('/Users/jnnamchi/go/src/github.com/Jnnamchi/soar-platform-api/app/firebase/credentials.json')
# firebase_admin.initialize_app(cred)

# db = firestore.client()
# uuid = 'ZbtlBnNWl0tsJ3KqzxN6'
# company = db.collection(u'companies').document(uuid).get().to_dict()

def getSurveyResultsAnalysis(surveyAnswers):
	answerTally = {}
	for userId, userAnswers in surveyAnswers.items():
		for answerId, answer in userAnswers.items():
			if answerId not in answerTally:
				answerTally[answerId] = {
					"score": 0
				}
				for point in points:
					answerTally[answerId][point] = 0
			answerTally[answerId]["score"] += scoreQuestion(answer)
			if answer in points:
				answerTally[answerId][answer] += 1
	return answerTally

# for moduleId in company["moduleAnswers"]:
# 	module = company["moduleAnswers"][moduleId]
# 	results = getSurveyResultsAnalysis(module)
