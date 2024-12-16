import instaloader
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


# Get Average Likes

usernamess = [#Target_Usernames]  

for username in usernamess:

    login_and_refresh_session()

    total_likes = 0
    average_likes = 0
    posts_count = 0
    profile = instaloader.Profile.from_username(L.context, username)

    time.sleep(random.uniform(10, 30))

    for post in profile.get_posts():

        total_likes += post.likes
        posts_count += 1
        
        if posts_count % 10  == 0:
            random_delay2()

        if posts_count % 1000 == 0 and posts_count != 0:
            time.sleep(random.uniform(100, 200))
            continue
        
        if posts_count %  500 == 0 and posts_count != 0:
            time.sleep(random.uniform(40, 60))
            continue

    average_likes = total_likes / posts_count

    print(f"Username: {username}, Average likes: {average_likes}, Total likes: {total_likes}, Posts Count: {posts_count}")
