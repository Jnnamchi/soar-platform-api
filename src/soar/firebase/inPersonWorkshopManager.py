import copy
from ..algos import surveyResultsAnalyzer

companyDescription = {
	"title": "Company Description",
	"subtitle": "(If appropriate, revise description to company's specific situation, business or industry)",
	"type": "textarea",
	"options": []
}
rationale = {
	"title": "Rationale",
	"subtitle": "",
	"type": "textarea",
	"options": []
}
estimatedCostToImplement = {
	"title": "Estimated Cost to Implement",
	"subtitle": "",
	"type": "text",
	"options": []
}
estimatedStartDate = {
	"title": "Estimated Start Date",
	"subtitle": "",
	"type": "date",
	"options": []
}
estimatedCompletionDate = {
	"title": "Estimated Completion Date",
	"subtitle": "",
	"type": "date",
	"options": []
}
champion = {
	"title": "Champion",
	"subtitle": "",
	"type": "text",
	"options": []
}
teamMembers = {
	"title": "Team Members",
	"subtitle": "",
	"type": "textarea",
	"options": []
}
majorActionItemsNext30Days = {
	"title": "Major Action Items",
	"subtitle": "Next 30 Days",
	"type": "textarea",
	"options": []
}
majorActionItemsDay31To90 = {
	"title": "Major Action Items",
	"subtitle": "Day 31 to 90",
	"type": "textarea",
	"options": []
}
majorActionItemsBeyond90Days = {
	"title": "Major Action Items",
	"subtitle": "Beyond 90 Days",
	"type": "textarea",
	"options": []
}
biggestObstaclesToSuccess = {
	"title": "Biggest Obstacles to Success",
	"subtitle": "",
	"type": "textarea",
	"options": []
}
status = {
	"title": "Status",
	"subtitle": "(Select Drop Down Item)",
	"type": "dropdown",
	"options": [ "Not Started", "Delayed", "On Schedule", "Behind Schedule", "On Hold - Short Term", "On Hold - Medium Term", "On Hold - Long Term", "Completed", "No Longer Applicable", "Other" ]
}
revenueEnhancementOrCostReductionPotentialFirstYear = {
	"title": "Revenue Enhancement Or Cost Reduction Potential",
	"subtitle": "First Year",
	"type": "text",
	"options": []
}
revenueEnhancementOrCostReductionPotentialThirdYear = {
	"title": "Revenue Enhancement Or Cost Reduction Potential",
	"subtitle": "Third Year",
	"type": "text",
	"options": []
}
revenueEnhancementOrCostReductionPotentialFifthYear = {
	"title": "Revenue Enhancement Or Cost Reduction Potential",
	"subtitle": "Fifth Year",
	"type": "text",
	"options": []
}
grossProfitPotential = {
	"title": "Gross Profit % Potential",
	"subtitle": "",
	"type": "text",
	"options": []
}
valueEnhancementPotential = {
	"title": "Value Enhancement Potential",
	"subtitle": "",
	"type": "text",
	"options": []
}

inPersonWorkshopSettings = [
	{	"name": "Opportunities In Person Workshop",
		"takesAnswersFrom": "1",
		"columns": [
			companyDescription,
			# {
			# 	"title": "Type of Opportunity",
			# 	"subtitle": "(Select from dropdown box)",
			# 	"type": "dropdown",
			# 	"options": [ "Sales & Margin Growth", "Productivity & Efficiency", "Cost Reduction", "Customer Satisfaction & Retention", "Organization, Culture, Leadership", "Accounting, Analytics, Finance, IT", "Operations & Supply Chain", "Processes, Systems, Controls, Safety, Quality", "Other" ]
			# },
			rationale,
			status,
			revenueEnhancementOrCostReductionPotentialFirstYear,
			revenueEnhancementOrCostReductionPotentialThirdYear,
			revenueEnhancementOrCostReductionPotentialFifthYear,
			grossProfitPotential,
			estimatedCostToImplement,
			valueEnhancementPotential,
			estimatedStartDate,
			estimatedCompletionDate,
			champion,
			teamMembers,
			majorActionItemsNext30Days,
			majorActionItemsDay31To90,
			majorActionItemsBeyond90Days,
			biggestObstaclesToSuccess,
		]
	},
	{
		"name": "Necessities In Person Workshop",
		"takesAnswersFrom": "1",
		"columns": [
			companyDescription,
			# {
			# 	"title": "Type of Necessity",
			# 	"subtitle": "(Select from dropdown box)",
			# 	"type": "dropdown",
			# 	"options": [ "Sales & Margin Growth", "Productivity & Efficiency", "Cost Reduction", "Customer Satisfaction & Retention", "Organization, Culture, Leadership", "Accounting, Analytics, Finance, IT", "Operations & Supply Chain", "Processes, Systems, Controls, Safety, Quality", "Other" ]
			# },
			rationale,
			status,
			estimatedCostToImplement,
			estimatedStartDate,
			estimatedCompletionDate,
			champion,
			teamMembers,
			majorActionItemsNext30Days,
			majorActionItemsDay31To90,
			majorActionItemsBeyond90Days,
			biggestObstaclesToSuccess,
		]
	}
]

def addModuleInPersonWorkshops (companyData, moduleId, module):
	# Add the TLK if its not there yet
	if "inPersonWorkshops" not in companyData:
		companyData["inPersonWorkshops"] = {}
	moduleVirtualWorkshops = companyData["virtualWorkshops"][moduleId]

	# Build the in person workshop
	moduleInPersonWorkshop = {
		"reRanking": {
			"unassigned": [],
			"opportunities": [],
			"necessities": []
		},
		"actionPlan": {}
	}
	for inPersonWorkshopSetting in inPersonWorkshopSettings:
		workshopSettings = {
			"name": inPersonWorkshopSetting["name"],
			"columns": inPersonWorkshopSetting["columns"],
			"rows": [],
		}
		moduleInPersonWorkshop["actionPlan"][inPersonWorkshopSetting["name"]] = workshopSettings

	moduleAnswers = moduleVirtualWorkshops[inPersonWorkshopSetting["takesAnswersFrom"]]
	for answerId, answerDetails in moduleAnswers["answerAnalysis"].items():
		questionName = surveyResultsAnalyzer.getQuestionNameFromId(answerId, module)
		moduleInPersonWorkshop["reRanking"]["unassigned"].append({
			"id": answerId,
			"questionName": questionName,
			"answerDetails": answerDetails,
			"oppOrNec": "Unselected",
			"answers": [""] * len(inPersonWorkshopSetting["columns"])
		})

	# Module ID should not be in the inPersonWorkshops at this point as we are just adding it now
	companyData["inPersonWorkshops"][moduleId] = moduleInPersonWorkshop
	return companyData

def buildAnswerList(inPersonWorkshopSetting):
	answerList = []
	for column in inPersonWorkshopSetting["columns"]:
		if column["type"] == "date":
			answerList.append("Dec 1 2022")
		elif column["type"] == "dropdown":
			answerList.append(column["options"][0])
		elif column["type"] == "text" or column["type"] == "textarea":
			answerList.append("")
		else:
			answerList.append("")
	return answerList

def saveWorkshopState(companyToUpdate, moduleId, workshops):
	if "inPersonWorkshops" in companyToUpdate:
		if moduleId in companyToUpdate["inPersonWorkshops"]:
			companyToUpdate["inPersonWorkshops"][moduleId] = workshops
	return companyToUpdate