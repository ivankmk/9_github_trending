import requests
import json
from datetime import timedelta, date


def get_week_ago_date():
    one_week_age = date.today() - timedelta(days=7)
    return one_week_age


def get_trending_repositories(top_popular, week_ago):

    payload = {
        'q': 'created:>{}'.format(week_ago),
        'sort': 'stars',
        'order': 'desc'
            }
    response = requests.get(
            'https://api.github.com/search/repositories',
            params=payload
            )
    return response.json()['items'][:top_popular]


def get_issues(owner, repo):
    issues = requests.get(
            'https://api.github.com/repos/{}/{}/issues'.
            format(owner, repo)
            )
    return len(issues.json())


def print_top_repositories(all_repos):
    delimiter = '-'*60
    print(delimiter)
    print('\nThis it the TOP repositories who created after {}\n'.
          format(week_ago))
    for rank, repo in enumerate(all_repos, 1):
        print('{}. Repo name: {}'.format(rank, repo['name']))
        print('\tOpened issues: {}'.
              format(get_issues(str(repo['owner']['login']), str(repo['name'])
                                )
                     )
              )
        print('\tLink: {}'.format(repo['html_url']))
    print(delimiter)


if __name__ == '__main__':
    top_repo = 20
    week_ago = get_week_ago_date()
    trending_repos = get_trending_repositories(top_repo, week_ago)
    print_top_repositories(trending_repos)
