import json

keys= ["user", "job_title", "job_description", "wage", "hours", "employer_name", "company_name", "neighborhood", "contact_method", "contact_info"
]

answers = {} # curly brackets for dictionaries
print("**************************************************")

for items in range(len(keys)):

        user_answer = input(keys[items])
        answers[keys[items]] = user_answer  #updates the list with one of the keys and the user's input

#all_users.append(answers)
print(answers)

jobs = open("JobInfo.json", "a")

dump = json.dumps(answers)
jobs.write(dump)
jobs.write(",\n")

jobs.close()
