#!/usr/bin/env python3

"""qutebrowser-redirect

This script redirects websites to their more privacy-respecting front-ends.

To use the script, put it in `~/.config/qutebrowser/` and add
`config.source('redirect.py')` in your `config.py` .
"""
import qutebrowser.api.interceptor


def rewrite(request: qutebrowser.api.interceptor.Request):
    """Intercepts requests and redirects them to alternative host"""
    if request.request_url.host() == "www.reddit.com":
        request.request_url.setHost("teddit.net")
        try:
            request.redirect(request.request_url)
        except Exception:
            pass

    if request.request_url.host() == "www.instagram.com":
        request.request_url.setHost("bibliogram.snopyta.org")
        try:
            request.redirect(request.request_url)
        except Exception:
            pass

    if request.request_url.host() == "twitter.com":
        request.request_url.setHost("nitter.eu")
        try:
            request.redirect(request.request_url)
        except Exception:
            pass


qutebrowser.api.interceptor.register(rewrite)
