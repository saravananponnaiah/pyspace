from dotenv import load_dotenv
import os

load_dotenv()
host_url = os.getenv('HOST_URL')
secret_key = os.getenv('SECRET_KEY_NAME')
database_name = os.getenv('DATABASE_NAME')

print(f"""
HOST: {host_url}
SECRET_KEY: {secret_key}
DATABASE: {database_name}
""")