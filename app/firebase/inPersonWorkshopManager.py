
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
	"options": [ "Not Started", "Delayed", "On Schedule", "Behind Schedule", "Completed", "Other" ]
}
revenueEnhancementOrCostReductionPotentialFirstYear = {
	"title": "Revenue Enhancement Or Cost Reduction Potential",
	"subtitle": "First Year",
	"type": "text",
	"options": []
}
revenueEnhancementOrCostReductionPotentialThirdYear = {
	"title": "Revenue Enhancement Or Cost Reduction Potential",
	"subtitle": "First Year",
	"type": "text",
	"options": []
}
revenueEnhancementOrCostReductionPotentialFifthYear = {
	"title": "Revenue Enhancement Or Cost Reduction Potential",
	"subtitle": "First Year",
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

inPersonWorkshops = {
	"Opportunities In Person Workshop": {
		"takesAnswersFrom": "round-2",
		"columns": [
			companyDescription,
			# {
			# 	"title": "Type of Opportunity",
			# 	"subtitle": "(Select from dropdown box)",
			# 	"type": "dropdown",
			# 	"options": [ "Sales & Margin Growth", "Productivity & Efficiency", "Cost Reduction", "Customer Satisfaction & Retention", "Organization, Culture, Leadership", "Accounting, Analytics, Finance, IT", "Operations & Supply Chain", "Processes, Systems, Controls, Safety, Quality", "Other" ]
			# },
			rationale,
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
			status,
		]
	},
	"Necessities In Person Workshop": {
		"takesAnswersFrom": "round-2",
		"columns": [
			companyDescription,
			# {
			# 	"title": "Type of Necessity",
			# 	"subtitle": "(Select from dropdown box)",
			# 	"type": "dropdown",
			# 	"options": [ "Sales & Margin Growth", "Productivity & Efficiency", "Cost Reduction", "Customer Satisfaction & Retention", "Organization, Culture, Leadership", "Accounting, Analytics, Finance, IT", "Operations & Supply Chain", "Processes, Systems, Controls, Safety, Quality", "Other" ]
			# },
			rationale,
			estimatedCostToImplement,
			estimatedStartDate,
			estimatedCompletionDate,
			champion,
			teamMembers,
			majorActionItemsNext30Days,
			majorActionItemsDay31To90,
			majorActionItemsBeyond90Days,
			biggestObstaclesToSuccess,
			status,
		]
	}
}
