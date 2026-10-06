from tokenize import String
import bcrypt 

def generate_password(password : str):
    passs_to_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(passs_to_bytes, salt)
    return password.decode();




password = generate_password("nitish");
print(password);




def check_password(password : str, hashed_password : str):
    passs_to_bytes = password.encode('utf-8')
    hashed_password_to_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(passs_to_bytes, hashed_password_to_bytes);


print(check_password("nitish", password));