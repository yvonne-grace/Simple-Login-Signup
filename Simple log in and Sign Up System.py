print('create account now')
username = input('enter username:  ')
password = input('enter password:  ')

print('Your account has been created successfully')
print('log in now!')

username2 = input('enter username:  ')
password2 = input('enter password:  ')

if username == username2 and password == username2:
    print('logged in succesfully')
else:
    print('invalid credentials')