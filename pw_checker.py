import requests
import getpass
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
    
    firts5_sha1, rest_sha1 = sha1_password[:5], sha1_password[5:]
    
    if __name__ == '__main__':
        print(f'SHA1: FIRSTS5_CHARS | REST_CHARS')
        print(f'{firts5_sha1} | {rest_sha1}\n')

    return get_password_leaks_count(rest_sha1, request_api_data(firts5_sha1))

def encrypt_password(password):
    size_pw = len(password)
    char_encrypt = ""
    if size_pw > 8:
        start_pw = password[:2]
        end_pw = password[-2:]
        aux_size = size_pw-4
    elif size_pw > 3:
        start_pw = password[:1]
        end_pw = password[-1:]
        aux_size = size_pw-2
    else: 
        start_pw = end_pw = ''
        aux_size = size_pw  

    i = 0
    while i < aux_size:
        char_encrypt += "*"
        i = i+1
    
    return start_pw+char_encrypt+end_pw
    
def main():
    password = getpass.getpass()    
    count = pw_api_check(password)
    encrypt = encrypt_password(password)
    print(f'FOR PASSWORD: {encrypt}')
    if count == 0:
        print(f'Good news! no leaks found. Carry on!')
    else:
        print(f'Bad news! This password has been seen {count} times before. If you\'ve ever used it anywhere before, change it!')
    

if __name__ == '__main__':
    sys.exit(main())