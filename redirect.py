#!/usr/bin/env python3

"""qutebrowser-redirect

This script redirects websites to their more privacy-respecting front-ends.

To use the script, put it in `~/.config/qutebrowser/` and add
`config.source('redirect.py')` in your `config.py` .
"""
from random import choice
import qutebrowser.api.interceptor

ALL_HOSTS = [
    [
        {
            "www.youtube.com",
            "youtube.com",
            "youtu.be",
        },
        [
            "invidious.snopyta.org",
            "invidious.namazso.eu",
            "yt.artemislena.eu",
            "invidious.flokinet.to",
            "invidious.weblibre.org",
            "inv.riverside.rocks",
            "y.com.sb",
            "invidious.sethforprivacy.com",
        ],
    ],
    [
        {"www.reddit.com", "reddit.com"},
        [
            "libreddit.privacy.com.de",
            "libredd.it",
            "libreddit.some-things.org",
            "libreddit.nl",
            "leddit.xyz",
        ],
    ],
    [
        {"www.twitter.com", "twitter.com"},
        [
            "nitter.net",
            "nitter.pussthecat.org",
            "nitter.unixfox.eu",
            "nitter.hu",
            "nitter.it",
            "nitter.sethforprivacy.com",
            "nitter.cz",
        ],
    ],
]


def rewrite(request: qutebrowser.api.interceptor.Request):
    """Intercepts requests and redirects them to alternative host"""
    for bad_hosts, alternatives in ALL_HOSTS:
        if request.request_url.host() in bad_hosts:
            request.request_url.setHost(choice(alternatives))
            for _ in range(3):  # Try 3 times, just to make sure.
                try:
                    request.redirect(request.request_url)
                    break
                except Exception:
                    pass
            break


qutebrowser.api.interceptor.register(rewrite)
