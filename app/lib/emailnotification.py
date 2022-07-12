# Implement the email notification system file here, exposes x functions:

# 1. On startup:
# Initialize email agent by logging in with valid credentials
# Use a test gmail account for now

# 2. Email templates
# Have a series of email templates that are compatible with the body of an email:
emailTemplates = {
	"Greeting": "Hello! Welcome to Soarline!",
	"Registration Email": "Congratulations! You have registered for the soarline growth module"
}

# The functions that should be exposed are:

# 1. Send Email
# Given a: (1) list of recipients, (2) a template email name (e.g. "Greeting")
# Send the email individually to each recipient

# 2. Set reminder
# Given a (1) list of recipients, (2) a template email name, (3) date to send email
# Store in the database "emails" collection fields (1) (2) and (3)

# 3. Send reminder email
# -> A separate process will look into the database and call this service to trigger this function (could be a cron job or other)
# When this function is called, check if a reminder email entry exists in the database for today's date
# If so, send the templated email to all recipients individually
# Remove the entry from the database