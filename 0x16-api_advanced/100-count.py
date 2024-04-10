#!/usr/bin/python3
"""
    A module that queries the Reddit API.
"""
import requests


def count_words(subreddit, word_list, after='', word_counter={}):
    """
        that queries the Reddit API, parses the title of all hot articles,
        and prints a sorted count of given keywords (case-insensitive,
        delimited by spaces. Javascript should count as javascript, but
        java should not).
    """

    if not word_counter:
        for current_word in word_list:
            if current_word.lower() not in word_counter:
                word_counter[current_word.lower()] = 0

    if after is None:
        sorted_words = sorted(word_counter.items(),
                              key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count:
                print('{}: {}'.format(word, count))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'danazil1263 query'}
    params = {'limit': 100, 'after': after}
    api_response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

    if api_response.status_code != 200:
        return None

    try:
        posts_ht = api_response.json()['data']['children']
        after_token = api_response.json()['data']['after']
        for post in posts_ht:
            title = post['data']['title']
            title_words = [word.lower() for word in title.split(' ')]
            for current_word in word_counter.keys():
                word_counter[current_word] += title_words.count(current_word)
    except Exception:
        return None

    count_words(subreddit, word_list, after_token, word_counter)
