import requests
import json
from datetime import timedelta, date


TOP_POPULAR = 20


def get_week_ago_date():
    one_week_age = date.today() - timedelta(days=7)
    return one_week_age


def get_trending_repositories():
    payload = {
                    'q': 'created:>{}'.format(get_week_ago_date()),
                    'sort': 'stars',
                    'order': 'desc'
                 }
    all_repos = requests.get('https://api.github.com/search/repositories',
                             params=payload)
    return all_repos.json()['items'][:TOP_POPULAR]


def print_top_repositories(all_repos):
    rank = 1
    print('-----------------------------------------------------------')
    print('\nThis it the TOP {} repositories who created after {}\n'.
          format(TOP_POPULAR, get_week_ago_date()))
    for repo in all_repos:
        print('{}. Repo name: {}'.format(rank, repo['name']))
        print('         Opened issues: {}'.format(repo['open_issues_count']))
        print('         Link: {}'.format(repo['html_url']))
        rank += 1
    print('-----------------------------------------------------------')

if __name__ == '__main__':
    trending_repos = get_trending_repositories()
    print_top_repositories(trending_repos)
