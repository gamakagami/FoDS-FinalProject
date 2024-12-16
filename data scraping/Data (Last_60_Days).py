import instaloader
from datetime import datetime, timedelta
import time
import random
  
L = instaloader.Instaloader()

def login_and_refresh_session():
    try:
        L.load_session_from_file(#username)
        time.sleep(random.uniform(60, 100))  
    except FileNotFoundError:
        L.login(#username, #password)
        L.save_session_to_file()
        time.sleep(random.uniform(60, 100))

def random_delay2():
    time.sleep(random.uniform(60, 80))

def random_delay():
    time.sleep(random.uniform(38, 40))

# Get Hashtag Dictionary, average hashtags, Follower count, post count (60 Days), and average likes from the last 60 days

sixty_days = timedelta(days=60)
now = datetime.now()
sixty_days_ago = now - sixty_days

usernamess = [#target_usernames]

login_and_refresh_session()

for username in usernamess:

    hashtags_dict = {}
    hashtags_count = 0
    max_pin_count = 0
    posts_count = 0
    total_likes = 0

    profile = instaloader.Profile.from_username(L.context, username) 

    for post in profile.get_posts():

        if posts_count % 20 == 0 and posts_count != 0:
            random_delay2()

        if max_pin_count > 3:
            break
        if post.date_utc < sixty_days_ago:
            max_pin_count += 1
            continue

        total_likes += post.likes
        posts_count += 1
        hashtags = post.caption_hashtags
        hashtags_count += len(hashtags)
        for hashtag in hashtags:
            if hashtag not in hashtags_dict.keys(): 
                hashtags_dict.update({hashtag : 1})
            else:
                hashtags_dict[hashtag] += 1

    try:
        print (f"Username: {username}")
        print(f"Followers: {profile.followers}")
        average_likes = total_likes / posts_count
        print(f"Average Likes: {average_likes}")
        print(f"Posts Count Last 60 Days: {posts_count}")
        average_hashtags = hashtags_count/posts_count
        print(f"Average Hastags : {average_hashtags}, Hashtags Dictionary: {hashtags_dict}")
    except:
        print('Num of hashtags, or posts invalid')
