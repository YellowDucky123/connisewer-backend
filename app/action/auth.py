from app.database import users, database
from hashlib import sha256

authUsers = database['authUsers']

# returns true if authentication succeeds
# returns false if authentication fails
def authentication(email, password) -> bool:
    userData = authUsers.find({"email": email})
    hashed_pass = sha256(password.encode('utf-8')).hexdigest()
    if hashed_pass == userData:
        return True
    return False

def addNewUserData(email, password):
    hashed_pass = sha256(password.encode('utf-8')).hexdigest()
    authUsers.insert_one({
        "email": email,
        "password": hashed_pass
    })