#!/usr/bin/python3
""" A module that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """
        A recursive function that queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit. If no
        results are found for the given subreddit, the function should return
        None.
    """
    url = 'https://api.reddit.com/r/{}/hot.json'.format(subreddit)
    if after != "tmp":
        url = url + "?after={}".format(after)

    headers = {
        'User-Agent': 'D Azil AdvancedAPI/1.0 (by /u/Daniel_Azil)'
    }

    res = requests.get(url, headers=headers, allow_redirects=False)
    response = res.json().get('data', {}).get('children', [])

    if not response:
        return hot_list

    for post in response:
        hot_list.append(post['data']['title'])

    after = res.json().get('data').get('after')
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
