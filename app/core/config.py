import os
from dotenv import load_dotenv
load_dotenv()
#secret key for JWTS
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# database cfg
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/bookstore") 