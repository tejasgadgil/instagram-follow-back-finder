# Ensure that you have added your username and password where specified.
# It is recommended that you change your password after using this program.
# Only you are solely responsible for any actions you take.

# Run the below commented line on your cli, then run this program. 
# pip install Instaloader

import instaloader as i_load

# enter username and password here
USERNAME = "<enter username here>"
PASSWORD = "<enter password here>"

# create instance of instaloader
L = i_load.Instaloader()

# 2FA enabled will generate input prompt
try:
    L.login(USERNAME, PASSWORD)
except i_load.TwoFactorAuthRequiredException:
    # Prompt for the 2FA code if needed
    two_factor_code = input("Enter the 2FA code: ")
    L.two_factor_login(two_factor_code)

# getting profile from username username
profile = i_load.Profile.from_username(L.context, USERNAME)

# getting followers and followees --> NodeIterator[Profile]
# converting to set
followers = set(profile.get_followers())
followees = set(profile.get_followees())


# print usernames of all accounts that I follow but they dont follow me back
acc_that_dont_follow_me_back = followees - followers

print("all accounts that I follow, but they dont follow me back")
for account in acc_that_dont_follow_me_back:
    print(account.username)

# print a list of all accounts that follow me, but I dont follow them back
acc_that_i_dont_followback = followers - followees

print("all accounts that follow me, but I dont follow them back")
for account in acc_that_i_dont_followback:
    print(account.username)

# print a list of all accounts that are mutuals with me
mutuals_acc = followers.intersection(followees)

print("accounts that are mutuals with me")
for account in mutuals_acc:
    print(account.username)
