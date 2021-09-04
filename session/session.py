import os, sys

def create_session(username, user_can) -> bool:
    session = open('tmp/session_.txt')
    session.write('live')
    session.close()
    return True

def load_session() -> bool:
    if os.path.exists('tmp/session_.txt'):
        session = open('tmp/session_.txt','r').read()
        if 'live' in session:
            return True
        else:
            return False
    else:
        return False

def delete_session() -> bool:
    os.unlink('tmp/session_.txt')
    return True