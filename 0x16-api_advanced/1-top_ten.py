#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Returns the titles of the first 10 hot posts listed for a given subreddit
    """
    if subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    res = requests.get(url, params=params, headers=headers,
                       allow_redirects=False).json()
    dictio = res.get("data", {}).get("children", None)

    if dictio:
        for topic in dictio:
            print(topic.get("data").get("title"))
    else:
        print("None")
