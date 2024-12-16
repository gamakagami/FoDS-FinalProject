import instaloader
import time
import random  # Import the random module
from itertools import islice

# Initialize Instaloader
L = instaloader.Instaloader()

# Attempt to load the session from a file
try:
    L.load_session_from_file("#username")  # Ensure you've saved a session previously
except FileNotFoundError:
    # If the session file doesn't exist, log in to create one
    L.login("#username", "#password")  # Replace with your credentials
    L.save_session_to_file()  # Save the session for future use

# Define the username of the target profile
username = [""]#target account

try:
    # Load the profile
    profile = instaloader.Profile.from_username(L.context, username)

    # Initialize a counter for post numbers
    post_number = 1

    # Initialize a dictionary to accumulate post type counts
    post_type_counts = {
        "Image": 0,
        "Video": 0,
        "Carousel": 0,
        "Reel": 0
    }

    # Loop through the last 50 posts
    for post in islice(profile.get_posts(), 274):
        try:
            print(f"Post Number: {post_number}")  # Print post number
            print(f"Post ID: {post.shortcode}")

            # Determine the post type
            if post.typename == "GraphImage":
                post_type_counts["Image"] += 1
            elif post.typename == "GraphVideo":
                post_type_counts["Video"] += 1
            elif post.typename == "GraphSidecar":
                post_type_counts["Carousel"] += 1
            elif post.is_video and post.video_duration <= 90:
                post_type_counts["Reel"] += 1

            # Introduce a random delay between 2 to 5 seconds
            delay = random.uniform(2, 5)  # Change the range as needed
            print(f"Waiting for {delay:.2f} seconds...")
            time.sleep(delay)

            post_number += 1  # Increment the post number

        except instaloader.exceptions.QueryReturnedBadRequestException as e:
            print(f"Error occurred for post {post.shortcode}: {e}")
            continue  # Skip this post and continue with the next one

    # Print the accumulated counts of each post type
    print("\nPost Type Counts:")
    for post_type, count in post_type_counts.items():
        print(f"{post_type}: {count}")

except instaloader.exceptions.ProfileNotExistsException:
    print("Profile does not exist.")
except instaloader.exceptions.ConnectionException as e:
    print(f"Connection error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

