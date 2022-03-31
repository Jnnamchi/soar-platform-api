import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

growthModuleSurvey = {
  "title": "Growth Module",
  "survey": {
	  "pages": [
		{
		"name": "Base Business Evolution",
		"questions": [
			{
			"name": "Growing by taking advantage of market conditions & momentum - before pursuing any significant new strategic initiatives.",
			"type": "matrix",
			"columns": [
				"Significant OPPORTUNITY", "Modest OPPORTUNITY", "Significant NECESSITY", "Modest NECESSITY", "LITTLE OR NO OPPORTUNITY OR NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
			],
			"rows": [
				{
				"id": "Growth-BBE-1",
				"question": "Achieving significant sales growth in the next few years by riding the wave of growth in market demand",
				"answer": "",
				},
				{
				"id": "Growth-BBE-2",
				"question": "Achieving significant sales growth in the next few years - because market forces will allow us to raise prices on some or all products/services and/or customers",
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
		"name": "Growing Wallet Share",
		"questions": [
			{
			"name": "Getting a bigger share of existing customer spending dollars.",
			"type": "matrix",
			"columns": [
				"Significant OPPORTUNITY", "Modest OPPORTUNITY", "Significant NECESSITY", "Modest NECESSITY", "LITTLE OR NO OPPORTUNITY OR NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
			],
			"rows": [
				{
				"id": "Growth-GWS-1",
				"question": "Selling more of the same products or services those customers ARE currently buying from us",
				"answer": "",
				},
				{
				"id": "Growth-GWS-2",
				"question": "Selling existing products or services those customers ARE NOT currently buying from us",
				"answer": "",
				},
				{
				"id": "Growth-GWS-3",
				"question": "Expanding our product line to sell products or services we DON'T currently offer to existing customers",
				"answer": "",
				},
				{
				"id": "Growth-GWS-4",
				"question": "Improving focus on up-selling - to encourage customers to expand the size of their purchases",
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
		"name": "Expanding Market Share",
		"questions": [
			{
			"name": "Growing by securing new customers in existing markets.",
			"type": "matrix",
			"columns": [
				"Significant OPPORTUNITY", "Modest OPPORTUNITY", "Significant NECESSITY", "Modest NECESSITY", "LITTLE OR NO OPPORTUNITY OR NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
			],
			"rows": [
				{
				"id": "Growth-EMS-1",
				"question": "Pursuing and selling to new Customersm- in existing markets, segments, geographies and channels",
				"answer": "",
				},
				{
				"id": "Growth-EMS-2",
				"question": "Enhancing the company's Value Proposition - to make it more attractive to new customers",
				"answer": "",
				},
				{
				"id": "Growth-EMS-3",
				"question": "Improving marketing and advertising to increase new customer awareness and perception of the company",
				"answer": "",
				},
				{
				"id": "Growth-EMS-4",
				"question": "Improving sales force effectiveness to increase ability to identify and land new customers",
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
		"name": "Growth From New Products",
		"questions": [
			{
			"name": "Using product development & upgrades to grow sales revenue.",
			"type": "matrix",
			"columns": [
				"Significant OPPORTUNITY", "Modest OPPORTUNITY", "Significant NECESSITY", "Modest NECESSITY", "LITTLE OR NO OPPORTUNITY OR NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
			],
			"rows": [
				{
				"id": "Growth-GFNP-1",
				"question": "Doing product upgrades and/or technological improvements/innovation to facilitate relaunching the product with new & improved features & benefits (Example: Increasing battery power of a mobile phone)",
				"answer": "",
				},
				{
				"id": "Growth-GFNP-2",
				"question": "Developing and/or sourcing new products that are extensions to current product lines (Example: Coke introducing Cherry Coke)",
				"answer": "",
				},
				{
				"id": "Growth-GFNP-3",
				"question": "Developing and/or sourcing new products where the changes are more extensive than product extensions but ARE connected to the core business and/or current product lines (Example: Coke introducing bottled water)",
				"answer": "",
				},
				{
				"id": "Growth-GFNP-4",
				"question": "Developing and/or sourcing new products are where the changes are more extensive than product extensions and are NOT connected to the core business and/or current product lines (completely new) (Example: Amazon offering cloud data storage services in its AWS division)",
				"answer": "",
				},
				{
				"id": "Growth-GFNP-5",
				"question": "Developing or introducing new products - in the form of existing products that are re-positioned to generate growth from new customers or markets (Example: aspirin being used for heart health)",
				"answer": "",
				},
				{
				"id": "Growth-GFNP-6",
				"question": "Developing or introducing new products and/or product lines - that are completely new to the world (Example: 3M's development of Post-It-Notes)",
				"answer": "",
				},
				{
				"id": "Growth-GFNP-7",
				"question": "Changing product technology, delivery mechanism, cost structure or customer experience - to leapfrog or obsolete existing players (Examples: Cell phones, Netflix, Uber, Starbucks, Southwest Airlines)",
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
		"name": "Growth From New Segments, Locations, Geographies, Channels",
		"questions": [
			{
			"name": "Stretching from current comfort zone.",
			"type": "matrix",
			"columns": [
				"Significant OPPORTUNITY", "Modest OPPORTUNITY", "Significant NECESSITY", "Modest NECESSITY", "LITTLE OR NO OPPORTUNITY OR NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
			],
			"rows": [
				{
				"id": "Growth-GFNSLGC-1",
				"question": "Selling into new Market SEGMENTS - using predominantly current products or technologies (perhaps with some modifications to adapt to the new segments)",
				"answer": "",
				},
				{
				"id": "Growth-GFNSLGC-2",
				"question": "Opening new locations - in existing geographies",
				"answer": "",
				},
				{
				"id": "Growth-GFNSLGC-3",
				"question": "Opening new locations in (or selling into) new Geographies - that ARE close to existing geographies",
				"answer": "",
				},
				{
				"id": "Growth-GFNSLGC-4",
				"question": "Opening new locations in (or selling into) new Geographies - that ARE NOT close to existing geographies",
				"answer": "",
				},
				{
				"id": "Growth-GFNSLGC-5",
				"question": "Selling through new Channels of Distribution",
				"answer": "",
				},
				{
				"id": "Growth-GFNSLGC-6",
				"question": "Selling via E- Commerce - via platforms like Amazon",
				"answer": "",
				},
				{
				"id": "Growth-GFNSLGC-7",
				"question": "Selling via E- Commerce - via the portals of retailers like Walmart, Target, Wayfair, etc",
				"answer": "",
				},
				{
				"id": "Growth-GFNSLGC-8",
				"question": "Selling via E- Commerce - direct to consumers via the company's own site",
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
		"name": "Non-Organic Growth",
		"questions": [
			{
			"name": "External Ways to Grow",
			"type": "matrix",
			"columns": [
				"Significant OPPORTUNITY", "Modest OPPORTUNITY", "Significant NECESSITY", "Modest NECESSITY", "LITTLE OR NO OPPORTUNITY OR NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
			],
			"rows": [
				{
				"id": "Growth-EWG-1",
				"question": "Acquiring, or merging with, another business",
				"answer": "",
				},
				{
				"id": "Growth-EWG-2",
				"question": "Acquiring product lines and/or customer lists from another business",
				"answer": "",
				},
				{
				"id": "Growth-EWG-3",
				"question": "Vertical integration - acquire (or develop) supplier or customer's business",
				"answer": "",
				},
				{
				"id": "Growth-EWG-4",
				"question": "Strategic hires - hire one or more people who can bring a significant customer base, unique expertise or access to markets or supply chains",
				"answer": "",
				},
				{
				"id": "Growth-EWG-5",
				"question": "Entering into Joint Ventures or Alliances - to enhance ability to offer new capabilities, technologies, products, - expand ability to penetrate new markets, segments, geographies or channels",
				"answer": "",
				},
				{
				"id": "Growth-EWG-6",
				"question": "Entering into Franchising and/or Licensing Agreements - to enhance ability to offer new capabilities, technologies, products, - expand ability to penetrate new markets, segments, geographies or channels",
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
		"name": "Margins",
		"questions": [
			{
			"name": "Improve Gross Profit Margins",
			"type": "matrix",
			"columns": [
				"Significant OPPORTUNITY", "Modest OPPORTUNITY", "Significant NECESSITY", "Modest NECESSITY", "LITTLE OR NO OPPORTUNITY OR NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
			],
			"rows": [
				{
				"id": "Growth-IGPM-1",
				"question": "Raising prices on some or all products and/or customers",
				"answer": "",
				},
				{
				"id": "Growth-IGPM-2",
				"question": "Reducing discount s and allowances given to customers",
				"answer": "",
				},
				{
				"id": "Growth-IGPM-3",
				"question": "Reducing rebates to customers",
				"answer": "",
				},
				{
				"id": "Growth-IGPM-4",
				"question": "Reducing margin leakage - from customers who buy at prices that are not justified by the volume of purchases or other factors - when compared with other similar customers",
				"answer": "",
				},
				{
				"id": "Growth-IGPM-5",
				"question": "Reducing margin leakage - customers who are given discounts and/or rebates that are not justified by the volume of purchases or other factors - when compared with other similar customers",
				"answer": "",
				},
				{
				"id": "Growth-IGPM-6",
				"question": "Reducing margin leakage - customers who are under charged for freight, shipping and handling or other support or services that are not justified by the volume of purchases or other factors - when compared with other similar customers",
				"answer": "",
				},
				{
				"id": "Growth-IGPM-7",
				"question": "Reducing margin leakage - by quickly passing on supply chain, labor & other cost increases",
				"answer": "",
				},
				{
				"id": "Growth-IGPM-8",
				"question": "Improving analysis of the \"Cost-to- Serve\" customers - and using this information to maximize pricing and true customer profitability after taking Cost-to- Serve into account. (Cost-to-Serve are the costs derived from extra service, service and expenses incurred to serve specific customers - that are not captured in Cost of Goods sold).",
				"answer": "",
				},
			],
			"answer": [],
			"choices": [],
			"items": []
			},
			{
			"name": "Other Ways to Improve Profitability & Gross Profit Margins",
			"type": "matrix",
			"columns": [
				"Significant OPPORTUNITY", "Modest OPPORTUNITY", "Significant NECESSITY", "Modest NECESSITY", "LITTLE OR NO OPPORTUNITY OR NECESSITY", "Don't Know", "NOT APPLICABLE OR RELEVANT"
			],
			"rows": [
				{
				"id": "Growth-OWIPGPM-1",
				"question": "Improve product mix to focus on higher margin products",
				"answer": "",
				},
				{
				"id": "Growth-OWIPGPM-2",
				"question": "Reducing the complexity, inefficiency & cost of estimating, quoting, order entry, picking, staging, fulfilling and shipping orders",
				"answer": "",
				},
				{
				"id": "Growth-OWIPGPM-3",
				"question": "Improve supply chain to reduce costs and improve terms and conditions",
				"answer": "",
				},
				{
				"id": "Growth-OWIPGPM-4",
				"question": "Improve raw material and/or product yields",
				"answer": "",
				},
				{
				"id": "Growth-OWIPGPM-5",
				"question": "Reduce waste, scrap & inventory obsolescence",
				"answer": "",
				},
				{
				"id": "Growth-OWIPGPM-6",
				"question": "Enhance value engineering and/or product redesign to reduce materials, labor or overhead costs or enhance value proposition",
				"answer": "",
				},
				{
				"id": "Growth-OWIPGPM-7",
				"question": "Improve team member engagement, teamwork and morale - to facilitate improvement in productivity, sales growth, profitability and margin improvment",
				"answer": "",
				},
				{
				"id": "Growth-OWIPGPM-8",
				"question": "Improve focus on continuous improvement and/or customer service/satisfaction - to facilitate improvement in productivity, sales growth, profitability and margin improvment",
				"answer": "",
				},
				{
				"id": "Growth-OWIPGPM-9",
				"question": "Improve IT and/or information systems - to facilitate improvement in productivity, sales growth, profitability and margin improvment",
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
		"name": "Details About You",
		"questions": [
			{
			"id": "Growth-Details-Name",
			"name": "What is your first and last name (optional)?",
			"type": "text",
			"columns": [],
			"rows": [],
			"answer": "",
			"choices": [],
			"items": []
			},
			{
			"id": "Growth-Details-Email",
			"name": "What is your work email address (optional)?",
			"type": "text",
			"columns": [],
			"rows": [],
			"answer": "",
			"choices": [],
			"items": []
			},
			{
			"id": "Growth-Details-Department",
			"name": "What department are you in (optional)?",
			"type": "text",
			"columns": [],
			"rows": [],
			"answer": "",
			"choices": [],
			"items": []
			},
			{
			"id": "Growth-Details-Location",
			"name": "What location do you work in (optional)?",
			"type": "text",
			"columns": [],
			"rows": [],
			"answer": "",
			"choices": [],
			"items": []
			},
			{
			"id": "Growth-Details-Title",
			"name": "What is your title (optional)?",
			"type": "text",
			"columns": [],
			"rows": [],
			"answer": "",
			"choices": [],
			"items": []
			},
			{
			"id": "Growth-Details-Tenure",
			"name": "How long have you worked for the company (optional)?",
			"type": "radio",
			"columns": [],
			"rows": [],
			"answer": "",
			"choices": [
				"Less than a year",
				"1 - 2 years",
				"3 - 5 years",
				"6 - 10 years",
				"11 - 20 years",
				"More than 20 years"
			],
			"items": []
			},
			{
			"id": "Growth-Details-Position",
			"name": "Describe the position in the organization that best fits your role (Required)",
			"type": "radio",
			"columns": [],
			"rows": [],
			"answer": "",
			"choices": [
				"C-Suite, including CEO, President, COO, Board Member, Owner",
				"Executive Management, including General Manager, Senior/Executive Vice President",
				"Vice President",
				"Director",
				"Manager",
				"Supervisor",
				"Non-manager - hourly",
				"Non-manager - salary",
				"Other"
			],
			"items": []
			}
		]
		},
	]
  }
}
growthModuleUuid = 'weHvXJGF3i5qgNfjFAN1'
cred = credentials.Certificate('/Users/jnnamchi/go/src/github.com/Jnnamchi/soar-platform-api/app/firebase/credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection(u'modules').document(growthModuleUuid).update(growthModuleSurvey)