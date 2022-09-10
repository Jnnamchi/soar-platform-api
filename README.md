# Soar Platform API

Requirements:
- python >= 3.9

# Getting started with docker

#### Build docker image:
```bash
docker build -t soar:dev .
```

#### Start container:
Note: .env.example - this file required, it contains zoom's S2S OAuth2 api credentials. You can name it anyhow you want. Or you can pass ENV variables into container with `-e FOO='bar' -e MOO='baz'` options. 
```Bash
docker run --env-file ./.env.example -p 127.0.0.1:5000:5000 soar:dev
```

# Run with docker compose

```bash
docker-compose build
docker-compose up -d
```


# Routes

There are currently 9 route groups that handle the behaviour of the application. They are listed in sequential order. Equivalent code can be found in '/app/routes.py'

**STEP 1: Get all user data**

**STEP 2: Add a company**

**STEP 3: Add a module to a company**

**STEP 4: Update company participants: add or remove participants**

**STEP 5: When a particpant completes a survey**

**STEP 6: Start the next virtual workshop for the company**

**STEP 7: When a particpant completes a workshop survey**

**STEP 8: Create & start the in-person workshop for the company**

**STEP 9: Save the data state of the in-person workshop for the company**

Additional routes should be added with new features, such as "submit payment" and "setup video meeting".


# Database

The database is a cloud firestore non-relational database. The main colleection is the **companies** collection, saved by id. They can be accessed via:

```
# DB is the Firestore Database object (already initialized in the code)
db = firestore.client()

# Get company by ID
companyById = db.collection(u'companies').document(companyId).get()

# Get company by ID Admin or partipants
company = db.collection(u'companies').where("admins", "array_contains", userId).get()
company = db.collection(u'companies').where("participants", "array_contains", userId).get()
```