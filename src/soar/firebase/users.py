
import firebase_admin

def getAllUsersInfoFromIDs(auth, userIds):
	usersInfo = []
	for userId in userIds:
		user = auth.get_user(userId)
		usersInfo.append({
			"uuid": userId,
			"email": user.email,
			"name": user.display_name
		})
	return usersInfo

def getUserIdsFromEmail(auth, userList):
	userIds = []
	for user in userList:
		userEmail = user["email"]
		userName = user["name"]
		try:
			user = auth.get_user_by_email(userEmail)
			userIds.append(user.uid)
		except firebase_admin._auth_utils.UserNotFoundError:
			# If user doesn't exist, create a new one
			newUser = auth.create_user(
				email=userEmail,
				email_verified=False,
				display_name=userName,
			)
			userIds.append(newUser.uid)
	return userIds
