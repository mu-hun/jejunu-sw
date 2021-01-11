import requests


def run_query(endpoint: str, query: str, variables: dict):
    request = requests.post(
        endpoint, json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))
