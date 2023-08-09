#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """ Returns the number of subreddit subscribers """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = get(url, headers=headers, allow_redirects=False).json()
    subscribers = res.get('data', {}).get('subscribers', 0)
    return subscribers
