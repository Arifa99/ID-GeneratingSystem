from hashlib import sha256
import argparse


def auth(password):
    new_pass = sha256(password.encode('utf-8')).hexdigest()
    with open('password.txt', 'r') as f:
        correct_password = f.readline()
    f.close()
    if correct_password == new_pass:
        return True
    return False


parser = argparse.ArgumentParser()
parser.add_argument("my_pass", help="Enter the password")
parser.add_argument("--name", help="Enter the name", type=str)
parser.add_argument("--course", help="Enter the course", type=str)
parser.add_argument("--enroll", help="Enter the enroll", type=str)
parser.add_argument("--faculty_no", help="Enter the faculty number", type=str)
parser.add_argument("--hall", help="enter the hall name", type=str)
parser.add_argument("--faculty", help="Enter the faculty", type=str)
parser.add_argument("--change_admin_pass", help="Enter the new password", type=str)
args = parser.parse_args()
r = auth(args.my_pass)

if r == 1:
    print("Welcome admin")
    u_list = []
    u_list.append(args.name)
    u_list.append(args.course)
    u_list.append(args.enroll)
    u_list.append(args.faculty_no)
    u_list.append(args.hall)
    u_list.append(args.faculty)

    print("Student Details are:-")
    for x in range(len(u_list)):
        print(u_list[x])

    print("Your change password:")
    print(args.change_admin_pass)

    if args.change_admin_pass != None:
        admin_new_pass = args.change_admin_pass
        hashed_password = sha256(admin_new_pass.encode()).hexdigest()
        print(hashed_password)
        with open('password.txt', 'w') as f:
            f.write(hashed_password)
        f.close()

else:
    print("Incorrect Password!!")
