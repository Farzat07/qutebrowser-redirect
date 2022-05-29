# redirect.py

## Used for redirecting website(s) X to one of website(s) Y in qutebrowser

Let us say, for example, that you want to redirect to a random invidious
instance each time you visit youtube.

First you create a list of possible youtube domains, for example `youtu.be`,
`youtube.com`, and `www.youtube.com`.

Then you create a list of invidious instances you want to use, for example
`invidious.namazso.eu`, `yt.artemislena.eu`, `invidious.flokinet.to`, and
`invidious.weblibre.org`.

Then you create a list item like the following, and add it to the list
ALL_HOSTS:

```python
[
    {
        "www.youtube.com",
        "youtube.com",
        "youtu.be",
    },
    [
        "invidious.namazso.eu",
        "yt.artemislena.eu",
        "invidious.flokinet.to",
        "invidious.weblibre.org",
    ],
]
```

The script already has redirects from youtube, reddit, and twitter to invidious,
libreddit, and nitter respectively.

To use the script, put it in `~/.config/qutebrowser/` and add
`config.source('redirect.py')` in your `config.py` .
