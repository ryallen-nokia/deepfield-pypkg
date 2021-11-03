import requests


def org_details(org_slug):
    response = requests.get(f'https://api.github.com/orgs/{org_slug}')
    return response.json()
