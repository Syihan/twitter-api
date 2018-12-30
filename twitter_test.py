import argparse
import json
import requests
from performance.consoletimer import consoletimer


# constants
VERSION = 1.1
API_URL = 'https://api.twitter.com/%s' % VERSION
DEFAULT_USERNAME = 'thatswatsyisaid'


# main method
def main():
    followers = get_followers(username='thatswatsyisaid')
    following = get_following(username='thatswatsyisaid')
    print(get_unfollowers(followers=followers, following=following))


# get followers
def get_followers(username=DEFAULT_USERNAME):
    # return requests.get(API_URL + '/followers/ids.json?screen_name=%s' % username)
    return requests.get('https://api.twitter.com/1.1/followers/ids.json?screen_name=twitterdev')


# get following
def get_following(username=DEFAULT_USERNAME):
    return requests.get(API_URL + '/friends/ids.json?screen_name=%s' % username)


# get unfollowers
def get_unfollowers(followers=[], following=[]):
    print ('Followers: \n%s' % followers)
    print ('Following: \n%s' % following)


# executes main
if __name__ == '__main__':
    main()
