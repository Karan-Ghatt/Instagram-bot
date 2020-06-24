from instapy import InstaPy
from instapy.util import smart_run


## Likes x3 images of posters based on given HASHTAG and relationship bounds. ##


insta_username = " "
insta_password = " "

hashtag = ' '

comment1 ="Your gameplay is awesome! If you're looking for some custome, royalty free music hit me up!"
comment2 ='Tired of copywright strike? Check out my profile for some custom, royalty free music!'
comment3 ='This is awesome! I Love your stuff'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    """ Activity flow """
    # settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                 sleepyhead=True, stochastic_flow=True, notify_me=True,
                                 peak_likes_hourly=57,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=21,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)
    session.set_skip_users(skip_private=True, private_percentage=100)


    # actions

    session.set_user_interact(amount=4, randomize=False, percentage=100)
    session.like_by_tags([hashtag], amount=5, interact=True)
    session.set_do_comment(enabled=True, percentage=25)
    session.set_comments([comment1, comment2, comment3])


session.end()

