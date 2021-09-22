from pprint import pprint
import requests

API_BASE_URL = 'https://api.stackexchange.com/2.3/questions?fromdate=1632096000&todate=1632268800&order=desc&sort=activity&tagged=Python&site=stackoverflow'

resp = requests.get(API_BASE_URL)
question_count = len(resp.json()['items'])

print(f'С тегом Python {question_count} вопросов за последние 2 дня.')

print(resp)
pprint(resp.json())
