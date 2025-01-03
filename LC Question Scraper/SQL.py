import mysql.connector
import json
import time

# Gets the data from data.json
import os

data_file_path = 'resources/data.json'
if not os.path.exists(data_file_path):
    raise FileNotFoundError(f"The file {data_file_path} does not exist.")

with open(data_file_path, 'r', encoding="utf-8") as file:
    data = json.load(file)

'''
Must Change
'''
# Establish the connection
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='INSERT USER FOR MYSQL', # Must change
        password='INSERT PASSWORD FOR USER', # Must change
        database='INSERT WHICH DATABASE' # Must change
    )
except:
    raise Exception('MySQL Database error')

# Create a cursor object
cursor = conn.cursor()

# Adds question into database
def add_question(data: dict): # {'easy':[[question_num, title, category1 category2, question itself]],s 'medium': [[question_num, title, question itself]], .....}
    
    try:
        for key, value in data.items():

            question_data_list = [(data[0], data[1], data[-1], data[2], data[3] ) for data in value]

            
            if key == 'easy':
                table = 'easy_questions'
            elif key == 'medium':
                table = 'medium_questions'
            elif key == 'hard':
                table = 'hard_questions'
            else:
                raise Exception("Invalid difficulty value | Valid value: \'easy\', \'medium\', \'hard\' | add_question")

                

            query = f'INSERT INTO {table} (Question_num, Title, Question, Category1, Category2) VALUES (%s, %s, %s, %s, %s)'

            cursor.executemany(query, question_data_list)
        
        conn.commit()
        conn.close()
    except:
        raise Exception('Wrong Data inputted | add_question')# Log

add_question(data)
    
    
