import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

standardMatrixColumns = [
	"Huge OPPORTUNITY", "Big OPPORTUNITY", "Modest OPPORTUNITY", "Huge NECESSITY", "Big NECESSITY", "Modest NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
]

moduleSurvey = {
  "title": "Organization & Culture Module",
  "survey": {
	  "pages": [
		{
			"name": "Recruiting, Training & Development",
			"questions": [
				{
					"name": "Recruiting, Training & Development",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-RTD-1",
							"question": "Improving employee recruiting and/or selection",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTD-2",
							"question": "Improving new employee on-boarding by establishing a clear and defined onboarding process including introductions to stakeholders",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTD-3",
							"question": "Improving training",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTD-4",
							"question": "Improving employee mentoring and/or coaching",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTD-5",
							"question": "Improving the employee appraisal and professional development process",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTD-6",
							"question": "Improving employee and manager succession planning and development",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		{
			"name": "Morale & Buy-in",
			"questions": [
				{
					"name": "Morale & Buy-in",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-MBI-1",
							"question": "Improving employee and/or manager buy-in",
							"answer": "",
						},
						{
							"id": "Org-Culture-MBI-2",
							"question": "Improving employee and/or manager opportunities for advancement",
							"answer": "",
						},
						{
							"id": "Org-Culture-MBI-3",
							"question": "Creating employee retention programs such as rewards, loyalty programs, education reimbursement, membership benefits, etc.",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		{
			"name": "Culture",
			"questions": [
				{
					"name": "Culture",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-CULT-1",
							"question": "Improving the organization's culture",
							"answer": "",
						},
						{
							"id": "Org-Culture-CULT-2",
							"question": "Improving values and ethics",
							"answer": "",
						},
						{
							"id": "Org-Culture-CULT-3",
							"question": "Improving transparency",
							"answer": "",
						},
						{
							"id": "Org-Culture-CULT-4",
							"question": "Improving trust between managers and employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-CULT-5",
							"question": "Improving trust between departments",
							"answer": "",
						},
						{
							"id": "Org-Culture-CULT-6",
							"question": "Improving trust between employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-CULT-7",
							"question": "Improving respect for all employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-CULT-8",
							"question": "Improving social, environment and/or community focus and involvement",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		{
			"name": "Empowerment, Engagement & Teamwork",
			"questions": [
				{
					"name": "Empowerment, Engagement & Teamwork",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-EET-1",
							"question": "Improving employee and/or manager empowerment",
							"answer": "",
						},
						{
							"id": "Org-Culture-EET-2",
							"question": "Improving employee and/or manager engagement",
							"answer": "",
						},
						{
							"id": "Org-Culture-EET-3",
							"question": "Improving teamwork/collaboration",
							"answer": "",
						},
						{
							"id": "Org-Culture-EET-4",
							"question": "Improving cooperation between departments",
							"answer": "",
						},
						{
							"id": "Org-Culture-EET-5",
							"question": "Encouraging more creativity and employee input",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		{
			"name": "Compensation & Benefits",
			"questions": [
				{
					"name": "Compensation & Benefits",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-CNB-1",
							"question": "Improving benefits",
							"answer": "",
						},
						{
							"id": "Org-Culture-CNB-2",
							"question": "Providing mental health support services",
							"answer": "",
						},
						{
							"id": "Org-Culture-CNB-3",
							"question": "Improving the company's PTO policy",
							"answer": "",
						},
						{
							"id": "Org-Culture-CNB-4",
							"question": "Improving incentives",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		{
			"name": "Work Environment",
			"questions": [
				{
					"name": "Work Environment",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-WE-1",
							"question": "Improving work conditions at company facilities",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-2",
							"question": "Treating all employees more fairly and/or consistently",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-3",
							"question": "Improving employee safety",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-4",
							"question": "Protecting employees from all forms of harassment",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-5",
							"question": "Providing employees with better processes and/or tools/resources to be more effective, reduce stress and/or enhance job satisfaction",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-6",
							"question": "Improving amenities or services offered to employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-7",
							"question": "Improving employee wellness and/or work/life balance",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-8",
							"question": "Improving diversity and/or inclusion",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-9",
							"question": "Improving and/or fostering a more flexible work schedule (including remote and/or hybrid work arrangements)",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-10",
							"question": "Increasing employee appreciation and recognition",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-11",
							"question": "Increasing employee respect",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-12",
							"question": "Increasing community involvement",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-13",
							"question": "Increasing commitment to environmental improvement",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-14",
							"question": "Fostering a more cohesive and supportive work environment",
							"answer": "",
						},
						{
							"id": "Org-Culture-WE-15",
							"question": "Creating more fun and/or out-of-office activities",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		{
			"name": "Communications",
			"questions": [
				{
					"name": "Communications",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-COM-1",
							"question": "Improving company communications to employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-COM-2",
							"question": "Improving manager and/or employee written and/or oral communication skills",
							"answer": "",
						},
						{
							"id": "Org-Culture-COM-3",
							"question": "Improving communication of the company mission, vision, goals, progress and results",
							"answer": "",
						},
						{
							"id": "Org-Culture-COM-4",
							"question": "Improving communication of budgets & forecasts - as well as actual results and variances",
							"answer": "",
						},
						{
							"id": "Org-Culture-COM-5",
							"question": "Improving communication of manager and/or expectations, targets and goals",
							"answer": "",
						},
						{
							"id": "Org-Culture-COM-6",
							"question": "Listening more to employees",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		{
			"name": "Organizational Effectiveness",
			"questions": [
				{
					"name": "Organizational Effectiveness",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-OE-1",
							"question": "Measuring and/or reducing employee/manager turnover",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-2",
							"question": "Improving leadership's focus on supplier and service provider relations",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-3",
							"question": "Improving employee and/or manager accountability",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-4",
							"question": "Improving employee and/or manager competence or effectiveness",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-5",
							"question": "Improving processes, procedures, productiivity or efficiency",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-6",
							"question": "Reducing bureaucracy",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-7",
							"question": "Having clearer and/or more effective lines of authority",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		{
			"name": "Leadership",
			"questions": [
				{
					"name": "Leadership",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-LEAD-1",
							"question": "Improving communication of company vision, mission and strategies",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-2",
							"question": "Improving communication of goals and expectations for managers and employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-3",
							"question": "Improving leadership accountability, reliability and dependability",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-4",
							"question": "Improving the effectiveness of leaders holding their direct reports accountable in an effective manner",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-5",
							"question": "Improving leadership's integrity and trustworthiness",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-6",
							"question": "Improving the effectiveness of leaders and managers",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-7",
							"question": "Improving leadership's effectiveness as role models, mentors and coaches",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-8",
							"question": "Improving management accessibility to, and interaction with, employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-9",
							"question": "Improving leadership's effectiveness at managing and resolving conflict",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-10",
							"question": "Improving leadership's ability to successfully create an environment that stimulates and welcomes creativity, ideas and process improvement",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-11",
							"question": "Improving leadership's effectiveness at sound and well-reasoned analysis, investigation and judgment - to facilitate effective decision making",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-12",
							"question": "Improving leadership's ability to blend a focus on investment for the future in a manner that is driven by return on investment",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-13",
							"question": "Improving leadership's focus on employee motivation, satisfaction and success",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-14",
							"question": "Improving leadership's focus on appropriate and effective systems, controls and standard operating procedures",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-15",
							"question": "Improving leaderships's effectiveness in managing priorities and dealing with changing demands",
							"answer": "",
						},
						{
							"id": "Org-Culture-LEAD-16",
							"question": "Improving leadership's focus on effective information systems, including timely Key Performance Indicators and Metrics",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
	]
  }
}
moduleUuid = '5ynpgMoSMz4o2Yl67kfu'
cred = credentials.Certificate('/Users/jnnamchi/go/src/github.com/Jnnamchi/soar-platform-api/src/credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection(u'modules').document(moduleUuid).update(moduleSurvey)