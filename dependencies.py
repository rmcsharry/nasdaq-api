from database import sess

def get_db():
    db = sess()
    try:
        yield db
    finally:
        db.close()