from pprint import pprint
import requests

def get_files_list():
    files_url = "https://api.stackexchange.com/2.3/questions"
    params = {"fromdate":"1634860800", "todate":"1635033600", "order":"desc", "sort":"activity", "tagged":"Python", "site":"stackoverflow"}
    response = requests.get(files_url, headers={"Accept": "application/json"}, params=params)
    return response.json()

pprint(get_files_list())
