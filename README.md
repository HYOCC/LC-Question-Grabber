# LC-Question-Grabber
Grabs estimate of 150 from 'easy' 'medium' and 'hard' and inserts them into a mysql database

# Usage
Open SQL.py, under Must Change, insert the correct information for the SQL db that you want to insert into your MySQL 

# Changing the data to be inserted 
Install the [Postman App](https://www.postman.com/downloads/)

Install the Leetcode SQ Apis under another [user's github](https://github.com/akarsh1995/leetcode-graphql-queries)

Open Postman then import the data that you just repoed from the github link

Under 'problemsetQuestionList' 

Change the 'limit' to the number of question you would like

Change 'filters': {"DIFFICULTY":"HARD} for hard, "MEDIUM" for medium and "EASY" for easy questions

After changing, open Data_load.py run it once

Open LC_Scrapper.py then let it run to gain the information

Lastly run SQL.py to insert data in SQL

# WARNING DO NOT change the following

difficulty

frontendQuestionId: questionFrontendId

title

titleSlug

isPaidOnly

topicTags {name}
