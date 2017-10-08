import subprocess

import json
import DicPrint as dp
import urllib






def login(username, password):
    command = 'curl -v https://api.robinhood.com/api-token-auth/ -H "Accept: application/json" -d "username='+username+'&password='+password+'"'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    out, err = p.communicate()
    if len(out) < 1:
        print ('Error connecting to server:')
        print (err)
    else:
        print ('Connection successful.')
    return out

def logout(token):
    command = 'curl -v https://api.robinhood.com/api-token-logout/ -H "Accept: application/json" -H "Authorization: Token '+token+'" -d ""'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    out, err = p.communicate()


def accountInfo(token):
    command = 'curl -v https://api.robinhood.com/accounts/ -H "Accept: application/json" -H "Authorization: Token '+token+'"'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    out, err = p.communicate()
    return out


def Stock(stock):
    command = 'curl -v https://api.robinhood.com/fundamentals/'+stock+'/  -H "Accept: application/json" '
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out




def main():
    print ('Logging in...')
    token = login('superjosue@gmail.com', 'ScorpionRojo1984')

    print (token)
    token = token[10:-2]
    print ('token: ', token)
    print ('Grabbing account information...')
    account_info = accountInfo(token)
    print(account_info)
    #json1_data = json.loads(account_info)
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(json1_data["results"])
    print('MSFT')

    url = "https://api.robinhood.com/"
    response = urllib.urlopen(url)
    data = json.loads(response.read())



    A= dp.DicPrint(data)


    print ('Logging out...')
    logout(token)

main()