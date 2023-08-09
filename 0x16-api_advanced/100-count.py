#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces)
"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """
    Prints a sorted count of given keywords in title of all hot
    Reddit articles
    """

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for a in range(len(word_list)):
                    if word_list[a].lower() == word.lower():
                        count[a] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for a in range(len(word_list)):
                for b in range(a + 1, len(word_list)):
                    if word_list[a].lower() == word_list[b].lower():
                        save.append(b)
                        count[a] += count[b]

            for a in range(len(word_list)):
                for b in range(a, len(word_list)):
                    if (count[b] > count[a] or
                            (word_list[a] > word_list[b] and
                             count[b] == count[a])):
                        aux = count[a]
                        count[a] = count[b]
                        count[b] = aux
                        aux = word_list[a]
                        word_list[a] = word_list[b]
                        word_list[b] = aux

            for a in range(len(word_list)):
                if (count[a] > 0) and a not in save:
                    print("{}: {}".format(word_list[a].lower(), count[a]))
        else:
            count_words(subreddit, word_list, after, count)
