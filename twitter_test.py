import argparse
import json
import requests

import credentials as creds
from utils import ConsoleTimer

# Constants
VERSION = 1.1
API_URL = f'https://api.twitter.com/{VERSION}'
DEFAULT_USERNAME = creds.USERNAME
DEFAULT_PASSWORD = creds.PASSWORD

def main():
    """
    Main method.
    """

    with ConsoleTimer("Getting followers."):
        followers = get_followers(username='thatswatsyisaid')
    
    with ConsoleTimer("Getting following."):
        following = get_following(username='thatswatsyisaid')

    with ConsoleTimer("Get Unfollowers."):
        get_unfollowers(followers=followers, following=following)

def get_followers(username: str=DEFAULT_USERNAME, password: str=DEFAULT_PASSWORD):
    """Returns a user's followers.
    
    Keyword Arguments:
        username {str} -- The user's username (default: {DEFAULT_USERNAME})
        password {str} -- The user's password (default: {DEFAULT_PASSWORD})
    
    Returns:
        The user's followers.
    """
    
    return requests.get(f'{API_URL}/followers/ids.json?screen_name={username}', auth=(username, password))

def get_following(username: str=DEFAULT_USERNAME, password: str=DEFAULT_PASSWORD):
    """Returns a user's following.
    
    Keyword Arguments:
        username {str} -- The user's username (default: {DEFAULT_USERNAME})
        password {str} -- The user's password (default: {DEFAULT_PASSWORD})
    
    Returns:
        The user's following.
    """

    return requests.get(f'{API_URL}/friends/ids.json?screen_name={username}')

def get_unfollowers(followers: list, following: list):
    """Prints a user's unfollowing.
    
    Keyword Arguments:
        followers {list} -- The user's followers
        following {list} -- The user's following
    """

    print (f'Followers: \n{followers}')
    print (f'Following: \n{following}')

# Execute the main method.
if __name__ == '__main__':
    main()
