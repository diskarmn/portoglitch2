# import os
# from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template
# import pymongo 

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# MONGODB_URI = os.environ.get("MONGODB_URI")
# DB_NAME =  os.environ.get("DB_NAME")

# client = pymongo.MongoClient(MONGODB_URI)
# db=client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()