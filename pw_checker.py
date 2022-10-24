import requests
import hashlib
import sys

ENDPOINT = 'https://api.pwnedpasswords.com/range/'
 
def request_api_data(query):
    url = ENDPOINT+query
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}. {res.text}.'
        +' Please check the API again.')

    return res

def get_password_leaks_count(hash_to_check, response_hashes):
    #divide string returned in response
    hashes = (line.split(':') for line in response_hashes.text.splitlines())
    
    #look for any hash that combine if hash_to_check
    for h, count in hashes:
        if h == hash_to_check:
            return count

    #if hashes don't contains any hash_to_check 
    return 0  

def pw_api_check(password):
    #encoding password because Unicode-objects must be encoded before hashing
    password_encode = password.encode('utf-8')
    
    #hashing password to split the five first char to send to api and separe the tail to compare after the request
    sha1_password = hashlib.sha1(password_encode).hexdigest().upper()
    
    firts5_char, tail = sha1_password[:5], sha1_password[5:]
    
    return get_password_leaks_count(tail, request_api_data(firts5_char))

def main(args):
    for password in args:
        count = pw_api_check(password)
        if count == 0:
            print(f'For [ {password} ] password: Good news! no leaks found! This password wasn\'t found in any of the leaks Passwords.'
            ' That doesn\'t necessarily mean it\'s a good password. Carry on!')
        else:
            print(f'For [ {password} ] password: Bad news! This password has been seen {count} times before. If you\'ve ever used'
            ' it anywhere before, change it!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))