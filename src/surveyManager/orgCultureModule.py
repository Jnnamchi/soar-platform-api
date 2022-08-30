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
			"name": "Culture",
			"questions": [
				{
					"name": "Vision, Mission, Goals, Strategies and Values",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-VMGSV-1",
							"question": "Improving communication of company vision, mission & strategy",
							"answer": "",
						},
						{
							"id": "Org-Culture-VMGSV-2",
							"question": "Improving communications of goals and expectations for managers and employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-VMGSV-3",
							"question": "Improving the organization's culture ",
							"answer": "",
						},
						{
							"id": "Org-Culture-VMGSV-4",
							"question": "Improving values & ethics ",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
				{
					"name": "Trust and Respect",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-TR-1",
							"question": "Improving transparency",
							"answer": "",
						},
						{
							"id": "Org-Culture-TR-2",
							"question": "Improving leadership's integrity and trustworthiness",
							"answer": "",
						},
						{
							"id": "Org-Culture-TR-3",
							"question": "Improving trust between managers and employees  ",
							"answer": "",
						},
						{
							"id": "Org-Culture-TR-4",
							"question": "Improving trust between departments",
							"answer": "",
						},
						{
							"id": "Org-Culture-TR-5",
							"question": "Improving trust between employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-TR-6",
							"question": "Improving respect for all employees",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				}
			]
		},
		{
			"name": "Leadership",
			"questions": [
				{
					"name": "Guidance and Decision Making",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-GDM-1",
							"question": "Improving leadership's effectiveness as role models, mentors and coaches",
							"answer": "",
						},
						{
							"id": "Org-Culture-GDM-2",
							"question": "Improving leadership's ability to successfully create an environment that stimulates and welcomes creativity, ideas and process improvement",
							"answer": "",
						},
						{
							"id": "Org-Culture-GDM-3",
							"question": "Improving leadership accountability, reliability and dependability",
							"answer": "",
						},
						{
							"id": "Org-Culture-GDM-4",
							"question": "Improving the effectiveness of leaders holding their direct reports accountable in an effective manner",
							"answer": "",
						},
						{
							"id": "Org-Culture-GDM-5",
							"question": "Improving leadership's effectiveness at sound and well-reasoned analysis, investigation and judgment - to facilitate effective decision making",
							"answer": "",
						},
						{
							"id": "Org-Culture-GDM-6",
							"question": "Improving leadership's effectiveness at managing and resolving conflict",
							"answer": "",
						},
						{
							"id": "Org-Culture-GDM-7",
							"question": "Improving leaderships ability to blend a focus on investment for the future in a manner that is driven by return on investment",
							"answer": "",
						},
						{
							"id": "Org-Culture-GDM-8",
							"question": "Improving leaderships's effectiveness in managing priorities and dealing with changing demands",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
				{
					"name": "Focus and Accessibility",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-FA-1",
							"question": "Improving management accessibility to, and interaction with, employees",
							"answer": "",
						},
						{
							"id": "Org-Culture-FA-2",
							"question": "Improving leadership's focus in terms of company PR",
							"answer": "",
						},
						{
							"id": "Org-Culture-FA-3",
							"question": "Improving leadership's focus in terms of supplier and service provider relations",
							"answer": "",
						},
						{
							"id": "Org-Culture-FA-4",
							"question": "Improving leadership's focus on employee motivation, satisfaction and success",
							"answer": "",
						},
						{
							"id": "Org-Culture-FA-5",
							"question": "Improving leadership's focus on economic trends, industry/competitive landscape, new technologies",
							"answer": "",
						},
						{
							"id": "Org-Culture-FA-6",
							"question": "Improving leadership's focus on appropriate and effective systems, controls and standard operating procedures",
							"answer": "",
						},
						{
							"id": "Org-Culture-FA-7",
							"question": "Improving leadership's focus on effective information systems, including timely Key Performance Indicators and Metrics",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				}
			]
		},
		{
			"name": "Work Environment",
			"questions": [
				{
					"name": "Physical & Virtual work Environment",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-PVWE-1",
							"question": "Improving work conditions related to the office space, production areas or other physical spaces",
							"answer": "",
						},
						{
							"id": "Org-Culture-PVWE-2",
							"question": "Improving employee safety",
							"answer": "",
						},
						{
							"id": "Org-Culture-PVWE-3",
							"question": "Improving amenities or services offered to employees - i.e., gym, cafeteria, free snacks, break rooms, activity rooms, etc",
							"answer": "",
						},
						{
							"id": "Org-Culture-PVWE-4",
							"question": "Providing employees with better processes and/or tools/resources to be more effective, reduce stress and/or enhance job satisfaction",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
				{
					"name": "Emotional and Mental Environment",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-EME-1",
							"question": "Treating all employees more fairly and/or consistently",
							"answer": "",
						},
						{
							"id": "Org-Culture-EME-2",
							"question": "Protecting employees from all forms of harassment",
							"answer": "",
						},
						{
							"id": "Org-Culture-EME-3",
							"question": "Improving employee wellness and/or work/life balance",
							"answer": "",
						},
						{
							"id": "Org-Culture-EME-4",
							"question": "Fostering a more cohesive and supportive work environment",
							"answer": "",
						},
						{
							"id": "Org-Culture-EME-5",
							"question": "Improving employee and/or manager flexibility",
							"answer": "",
						},
						{
							"id": "Org-Culture-EME-6",
							"question": "Improving diversity and/or inclusion",
							"answer": "",
						},
						{
							"id": "Org-Culture-EME-7",
							"question": "Providing adequate opportunities and support for remote/hybrid work",
							"answer": "",
						},
						{
							"id": "Org-Culture-EME-8",
							"question": "Providing adequate mental health resources",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
				{
					"name": "External Work Environment",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-EWE-1",
							"question": "Improving social, environment and/or community focus and involvement",
							"answer": "",
						},
						{
							"id": "Org-Culture-EWE-2",
							"question": "Increasing community involvement",
							"answer": "",
						},
						{
							"id": "Org-Culture-EWE-3",
							"question": "Increasing commitment to sustainability and environment",
							"answer": "",
						},
						{
							"id": "Org-Culture-EWE-4",
							"question": "Creating corporate sports teams and joining local/regional games/leagues",
							"answer": "",
						},
						{
							"id": "Org-Culture-EWE-5",
							"question": "Participating in volunteering activities",
							"answer": "",
						},
						{
							"id": "Org-Culture-EWE-6",
							"question": "Creating more fun and/or activities",
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
			"name": "Recruiting, Training & Development",
			"questions": [
				{
					"name": "Recruitment and Onboarding",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-IERSP-1",
							"question": "Improving employee recruitment or selection processes",
							"answer": "",
						},
						{
							"id": "Org-Culture-IERSP-2",
							"question": "Establishing clear process for new employee on-boarding and introductions to stakeholders",
							"answer": "",
						},
						{
							"id": "Org-Culture-IERSP-3",
							"question": "Improving new employee orientation and training",
							"answer": "",
						},
						{
							"id": "Org-Culture-IERSP-4",
							"question": "Creating employee referral programs",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
				{
					"name": "Professional Development",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-PD-1",
							"question": "Improving mentoring and/or coaching",
							"answer": "",
						},
						{
							"id": "Org-Culture-PD-2",
							"question": "Improving employee appraisal & development",
							"answer": "",
						},
						{
							"id": "Org-Culture-PD-3",
							"question": "Encouraging the development of new skills and competencies",
							"answer": "",
						},
						{
							"id": "Org-Culture-PD-4",
							"question": "Establishing Internship programs ",
							"answer": "",
						},
						{
							"id": "Org-Culture-PD-5",
							"question": "Improving employee and manager succession/career planning & training and development",
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
							"question": "Improving teamwork/collaboration and crossfunctional training",
							"answer": "",
						},
						{
							"id": "Org-Culture-EET-4",
							"question": "Improving cooperation between departments",
							"answer": "",
						},
						{
							"id": "Org-Culture-EET-5",
							"question": "Encouraging internal entrepreneurship, creativity and input",
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
							"question": "Improving communication of the company mission, vision, goals and strategies",
							"answer": "",
						},
						{
							"id": "Org-Culture-COM-3",
							"question": "Improving manager and/or employee written and/or oral communication skills",
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
							"question": "Improving employee and/or manager accountability",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-2",
							"question": "Improving employee and/or manager competence or effectiveness",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-3",
							"question": "Improving processes, procedures, productivity or efficiency",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-4",
							"question": "Improving meeting, time management and project/task management skills",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-5",
							"question": "Improving the measures that would help with privacy",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-6",
							"question": "Improving the HR management systems to create an engagement platform",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-7",
							"question": "Supporting the existing organization with part-time consultants, contractors or experts",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-8",
							"question": "Reducing bureaucracy",
							"answer": "",
						},
						{
							"id": "Org-Culture-OE-9",
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
			"name": "Morale & Buy-in",
			"questions": [
				{
					"name": "Morale & Buy-in",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-MBI-1",
							"question": "Improving employee and/or manager morale",
							"answer": "",
						},
						{
							"id": "Org-Culture-MBI-2",
							"question": "Improving employee and/or manager buy-in",
							"answer": "",
						},
						{
							"id": "Org-Culture-MBI-3",
							"question": "Improving employee and/or manager opportunities for advancement",
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
							"question": "Improving compensation",
							"answer": "",
						},
						{
							"id": "Org-Culture-CNB-2",
							"question": "Improving performance bonus structures",
							"answer": "",
						},
						{
							"id": "Org-Culture-CNB-3",
							"question": "Improving benefits",
							"answer": "",
						},
						{
							"id": "Org-Culture-CNB-4",
							"question": "Improving the company's PTO policy",
							"answer": "",
						},
						{
							"id": "Org-Culture-CNB-5",
							"question": "Establishing incentives programs for non financial positions",
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
			"name": "Retention",
			"questions": [
				{
					"name": "Retention",
					"type": "matrix",
					"columns": standardMatrixColumns,
					"rows": [
						{
							"id": "Org-Culture-RTN-1",
							"question": "Measuring and/or reducing employee/manager turnover",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTN-2",
							"question": "Performing compensation and satisfaction surveys on the industry",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTN-3",
							"question": "Increasing employee appreciation and recognition",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTN-4",
							"question": "Imroving Cross-functional training for internal growth",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTN-5",
							"question": "Creating employee retention programs such as rewards, stock option plans, loyalty programs, membership benefits, etc.",
							"answer": "",
						},
						{
							"id": "Org-Culture-RTN-6",
							"question": "Ensuring that internal mobility and career advancement is available for employees",
							"answer": "",
						},
					],
					"answer": [],
					"choices": [],
					"items": []
				},
			]
		},
		# {
		# 	"name": "Details About You",
		# 	"questions": [
		# 		{
		# 			"id": "Growth-Details-Name",
		# 			"name": "What is your first and last name (optional)?",
		# 			"type": "text",
		# 			"columns": [],
		# 			"rows": [],
		# 			"answer": "",
		# 			"choices": [],
		# 			"items": []
		# 		},
		# 		{
		# 			"id": "Growth-Details-Email",
		# 			"name": "What is your work email address (optional)?",
		# 			"type": "text",
		# 			"columns": [],
		# 			"rows": [],
		# 			"answer": "",
		# 			"choices": [],
		# 			"items": []
		# 		},
		# 		{
		# 			"id": "Growth-Details-Department",
		# 			"name": "What department are you in (optional)?",
		# 			"type": "text",
		# 			"columns": [],
		# 			"rows": [],
		# 			"answer": "",
		# 			"choices": [],
		# 			"items": []
		# 		},
		# 		{
		# 			"id": "Growth-Details-Location",
		# 			"name": "What location do you work in (optional)?",
		# 			"type": "text",
		# 			"columns": [],
		# 			"rows": [],
		# 			"answer": "",
		# 			"choices": [],
		# 			"items": []
		# 		},
		# 		{
		# 			"id": "Growth-Details-Title",
		# 			"name": "What is your title (optional)?",
		# 			"type": "text",
		# 			"columns": [],
		# 			"rows": [],
		# 			"answer": "",
		# 			"choices": [],
		# 			"items": []
		# 		},
		# 		{
		# 			"id": "Growth-Details-Tenure",
		# 			"name": "How long have you worked for the company (optional)?",
		# 			"type": "radio",
		# 			"columns": [],
		# 			"rows": [],
		# 			"answer": "",
		# 			"choices": [
		# 				"Less than a year",
		# 				"1 - 2 years",
		# 				"3 - 5 years",
		# 				"6 - 10 years",
		# 				"11 - 20 years",
		# 				"More than 20 years"
		# 			],
		# 			"items": []
		# 		},
		# 		{
		# 			"id": "Growth-Details-Position",
		# 			"name": "Describe the position in the organization that best fits your role (Required)",
		# 			"type": "radio",
		# 			"columns": [],
		# 			"rows": [],
		# 			"answer": "",
		# 			"choices": [
		# 				"C-Suite, including CEO, President, COO, Board Member, Owner",
		# 				"Executive Management, including General Manager, Senior/Executive Vice President",
		# 				"Vice President",
		# 				"Director",
		# 				"Manager",
		# 				"Supervisor",
		# 				"Non-manager - hourly",
		# 				"Non-manager - salary",
		# 				"Other"
		# 			],
		# 			"items": []
		# 		}
		# 	]
		# },
	]
  }
}
moduleUuid = '5ynpgMoSMz4o2Yl67kfu'
cred = credentials.Certificate('/Users/jnnamchi/go/src/github.com/Jnnamchi/soar-platform-api/app/firebase/credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection(u'modules').document(moduleUuid).update(moduleSurvey)