LOGO = """
   ____   
  / __ \  
 | |  | | 
 | |  | |
 | |__| |
  \____/  

"""


from hashlib import sha256
hashed_password = sha256(b'arifa').hexdigest()
with open('password.txt', 'w') as f:
    f.write(hashed_password)

# function to take input
def myinput():
    from getpass import getpass
    password = getpass("Enter your password")
    return password

# function to verify password
def auth(password):
    newpass = sha256(password.encode('utf-8')).hexdigest()
    with open('password.txt', 'r') as f:
        correct_password = f.readline()
    if correct_password == newpass:
        return True
    return False

password = myinput()
a = auth(password)
def get_input():
    u_list = []
    u_list.append(input("Enter user name:"))
    u_list.append(input("Enter Course:"))
    u_list.append(input("Enter Enroll:"))
    u_list.append(input("Enter the Faculty Number:"))
    u_list.append(input("Enter Hall Name:"))
    u_list.append(input("Enter Faculty:"))
    return u_list

if a==True:
    user = get_input()
    print('\x1b[1;42;37m'+ "  ALIGARH MUSLIM UNIVERSITY " + '\x1b[0m')
    print(f"{LOGO}")
    print("\t" +user[0].capitalize())
    print("\t" +user[1].capitalize())
    print("\t" +user[2].capitalize()+"/" + user[3].capitalize())
    print("\t" +user[4].capitalize())
    print('\x1b[1;41;37m'+ user[5] + '\[0m' )



	
