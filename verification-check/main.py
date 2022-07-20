import requests
import os

print(os.environ['WORKFLOWS_TOKEN'])

merged_prs = requests.get('https://api.github.com/search/issues', params={'q': 'is:pull-request'}, headers={'Authorization': f'Token {WORKFLOWS_TOKEN}'})
print(merged_prs)
