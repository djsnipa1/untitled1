import json

with open('source-data.json') as access_json:
  read_content  = json.load(access_json)

question_access = read_content['results']


for question_data in question_access:
  print("QUESTION_DATA:")
  print("=============================")
  print(question_data)

replies_access = question_data['replies']

for replies_data in replies_access:
  print(replies_data)

user_name = replies_data['user']['display_name']

pretty = json.dumps(replies_data, indent=2, sort_keys=True)

print(user_name)

def get_user_names():
  question_access = read_content['results']
  for question_data in question_access:
    replies_access = question_data['replies']
    for replies_data in replies_access:
      user_name = replies_data['user']['display_name']
      save_data.append(user_name)


save_data = []


get_user_names()

with open('usernames.json', 'w') as file:
  json.dump(save_data, file)

print(save_data)