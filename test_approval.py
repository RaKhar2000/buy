import requests, os
key_data = requests.get("https://github.com/RaKhar2000/R-4/blob/main/key.txt").text
user_key = str(os.getlogin()) + str(os.getuid())
if user_key in key_data:
    print("Your Key Approval")
else:
    print("Your Key Not Approval\n")
    print(f"Your Key: {user_key}")