USERS = {
    'dieison': 'senha123',
    'admin': '123456'
}

def validalogin (username,password):
    if username in USERS and USERS[username] == password:
        return True
    return False