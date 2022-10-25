![banner](https://github.com/luanjesus/password_checker/blob/main/meta/banner.png?raw=true)


This a small programme that verify if the password informed has been leaked using 
Pwned Passwords v2 API. The data is [K-anonymized](https://en.wikipedia.org/wiki/K-anonymity) before sending to the API, so plaintext 
passwords never leave your computer.

- Code below will ask you for a password. 
- The input will be collected using [`getpass`](https://docs.python.org/3/library/getpass.html)
- Then the data will be hashed using SHA1 
- The first five characters of hash will be sending to [pwnedpassword.com](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/)
- API will return the number of times the information was leaked or if never was.

## PWNED PASSWORD API
`https://api.pwnedpasswords.com/range/{hashed_password}`

If the password is *testpassword123* the programme will convert the string to:
```sh
SHA1 
FIRSTS5_CHARS | REST_CHARS
C1800 | 6FC138809314751CD1991F1E0B820FABD37
```
And the API will receive only the first five character *C1800*. Then it will return a list with all results that were found and the number of times that the information was leaked.
![img_ex1](https://github.com/luanjesus/password_checker/blob/main/meta/api_ex1.png?raw=true)

In this exemple the REST_CHARS (*6FC138809314751CD1991F1E0B820FABD37*) was found if 36 occurrences.
![img_ex2](https://github.com/luanjesus/password_checker/blob/main/meta/api_ex_2.png?raw=true)


## HOW TO USE

### To run the file
```sh
$python pw_checker.py
```

#### Exemple of leaked password
*Input: testpassword123*
```sh
$python pw_checker.py
Password: 
```
Obs: Password won`t apper to user when digits because getpass
#### Output if use:

```sh
FOR PASSWORD: te***********23
    Bad news! This password has been seen 36 times before. If you`ve ever used it anywhere before, change it!
```

#### Exemple of that never was leaked
*Input: pythonisthebest*

#### Output if use:

```sh
    FOR PASSWORD: py***********st
    Good news! no leaks found. Carry on!
```


## License

MIT

**Free Software, Hell Yeah!**

### Author: 
Luan Leone

## References:
  - [Troy Hunt](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/)
  - [pwnedpasswords](https://github.com/lionheart/pwnedpasswords)