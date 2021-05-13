import requests
import json
from bs4 import BeautifulSoup

def scrape_questions(tag, questions_count):
    number_of_pages = int( questions_count / 50.0 )
    questions_dict = {
                        "questions" : []
                     }
    count = 0

    for page in range(1, number_of_pages + 1):
        url = f"https://stackoverflow.com/questions/tagged/{tag}?tab=newest&page={page}&pagesize=50"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        questions = soup.select(".question-summary")

        for question in questions:
            count += 1
            views_count = (question.select_one('.views').attrs['title']).split()[0]
            votes_count = vote_count = question.select_one('.vote-count-post').getText()
            question_title = question.select_one('.question-hyperlink').getText()
            question_link = "https://stackoverflow.com" + question.select_one('.question-hyperlink').attrs['href']

            questions_dict['questions'].append({
                        "index" : count,
                        "views" : views_count,
                        "votes" : votes_count,
                        "question" : question_title,
                        "link" : question_link
                  })

    data = json.dumps(questions_dict)
    return questions_dict['questions']

def scrape_users(username):
    url = f"https://api.stackexchange.com/2.2/users?order=desc&sort=reputation&inname={username}&site=stackoverflow"

    response = (requests.get(url)).json()

    count_users = len(response['items'])

    information_dict = {
                         "user_info" : []
                       }

    for count in range(count_users):
        data = response['items'][count]

        profile_name = data['display_name']
        profile_url = data['link']
        badge_details = data['badge_counts']
        reputation = data['reputation']
        try:
            location = data['location']
        except:
            location = 'Not available'

        information_dict['user_info'].append({
                        "display_name" : profile_name,
                        "link" : profile_url,
                        "badge_counts" : badge_details,
                        "reputation" : reputation,
                        "location" : location
                   })


    json_data = json.dumps(information_dict)
    return information_dict['user_info'], count_users
