import json

u_data = {}# The total Data

# Processes the data in each respectful file
with open('resources/easy_LC.json', 'r') as file:
    easy_lc = json.load(file)
    easy_lc = easy_lc['data']['problemsetQuestionList']['questions']
    
    for question in easy_lc:
        if 'easy' in u_data:
            if question['isPaidOnly'] == False:
                u_data['easy'].append([question['frontendQuestionId'], question['title'], question['topicTags'][0]['name'] if len(question['topicTags']) >= 1 else 'none', question['topicTags'][1]['name'] if len(question['topicTags']) >= 2 else 'none', question['titleSlug']])
        else:
            if question['isPaidOnly'] == False:
                u_data['easy'] = [[question['frontendQuestionId'], question['title'], question['topicTags'][0]['name'] if len(question['topicTags']) >= 1 else 'none', question['topicTags'][1]['name'] if len(question['topicTags']) >= 2 else 'none', question['titleSlug']]]
    
    
with open('resources/medium_LC.json', 'r') as file:
    medium_lc = json.load(file)
    medium_lc = medium_lc['data']['problemsetQuestionList']['questions']
    for question in medium_lc:
        if 'medium' in u_data:
            if question['isPaidOnly'] == False:
                u_data['medium'].append([question['frontendQuestionId'], question['title'], question['topicTags'][0]['name'] if len(question['topicTags']) >= 1 else 'none', question['topicTags'][1]['name'] if len(question['topicTags']) >= 2 else 'none', question['titleSlug']])
        else:
            if question['isPaidOnly'] == False:
             u_data['medium'] = [[question['frontendQuestionId'], question['title'], question['topicTags'][0]['name'] if len(question['topicTags']) >= 1 else 'none', question['topicTags'][1]['name'] if len(question['topicTags']) >= 2 else 'none', question['titleSlug']]]

with open('resources/hard_LC.json', 'r') as file:
    hard_lc = json.load(file)
    hard_lc = hard_lc['data']['problemsetQuestionList']['questions']

    for question in hard_lc:
        if 'hard' in u_data:
            if question['isPaidOnly'] == False:
                u_data['hard'].append([question['frontendQuestionId'], question['title'], question['topicTags'][0]['name'] if len(question['topicTags']) >= 1 else 'none', question['topicTags'][1]['name'] if len(question['topicTags']) >= 2 else 'none', question['titleSlug']])
        else:
            if question['isPaidOnly'] == False:
                u_data['hard'] = [[question['frontendQuestionId'], question['title'], question['topicTags'][0]['name'] if len(question['topicTags']) >= 1 else 'none', question['topicTags'][1]['name'] if len(question['topicTags']) >= 2 else 'none', question['titleSlug']]]


with open('resources/unprocessed_data.json', 'w', encoding = 'utf-8') as file:
    json.dump(u_data, file, ensure_ascii=False)