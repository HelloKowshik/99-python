import requests

def create_query(languages, min_stars = 50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query

def get_github_data(user_langs, sort="stars", order="desc"):
    github_api = 'https://api.github.com/search/repositories'
    query = create_query(user_langs)
    # parameters = {"q": "stars:>5000"}
    # parameters = {"q": query, "sort": "stars", "order": "desc"}
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(github_api, parameters)
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An error occured! Status Code: {status_code}")
    else:
        json_data = response.json()['items']
        return json_data


if __name__ == '__main__':
    languages = ["Python", "Javascript", "Ruby"]
    api_data = get_github_data(languages)
    for result in api_data:
        langs = result["language"]
        total_stars = result["stargazers_count"]
        name = result["name"]
        full_name = result["full_name"]
        print(f"=> {full_name} - {name} - {langs} - {total_stars}")

