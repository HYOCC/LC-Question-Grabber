from selenium import webdriver 
from selenium.webdriver.common.by import By
import json 
import time
import random

driver = webdriver.Chrome()# Starts the scrapping driver

with open('resources/unprocessed_data.json', 'r') as file:
    r_data = json.load(file)

with open('resources/data.json', 'r') as file:
    p_data = json.load(file)

for key, value in r_data.items():
    for i in range(len(value) - 1, 0 , -1):
        try: 
            website = f'https://leetcode.com/problems/{value[i][-1]}/'  
            driver.get(website)
            content = driver.find_element(By.CLASS_NAME, "elfjS")
            text = content.text
            
            value[i].append(text)
            added_value = value.pop()
            p_data[key].append(added_value)
            print(added_value)
            
            sleep_time = random.uniform(1, 4) # Random time to start iteration
            time.sleep(1)
        except:
            with open('resources/unprocessed_data.json', 'w', encoding='utf-8') as file:
                json.dump(r_data, file, ensure_ascii=False)
            
            with open('resources/data.json', 'w', encoding='utf-8') as file:
                json.dump(p_data, file, ensure_ascii=False)
                
            raise Exception(f'error getting the data on {website}')

with open('resources/data.json', 'w', encoding='utf-8') as file:
    json.dump(p_data, file, ensure_ascii=False)
    












