#!/usr/bin/env python
import praw
import argparse
try:
    input = raw_input
except NameError:
    pass

subreddit = input('What subreddit would you like to search modmail of: ')
username = input('Which username would you like to find modmail from: ')
r = praw.Reddit('User specific modmail grabber by /u/Decency')
print("Please login with your moderator credentials...")
r.login(disable_warning=True)
for m in r.get_subreddit(subreddit).get_mod_mail(limit=10000):
    if m.author and m.author.name.lower() == username.lower():
        print('https://www.reddit.com/message/messages/%s' % m.id)
print('\nCompleted searching /r/%s for modmail from %s!\n' % (subreddit, username))
