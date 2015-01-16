__author__ = 'Nathan Lamar'

import praw
import pprint

r = praw.Reddit('OAuth Testing by u/pay_the_troll_toll ver 0.1')
r.login("pay_the_troll_toll", "yankees21")
posts = r.get_subreddit("gaming+").get_hot(limit=10)
subids = set()
for subs in posts:
    subids.add(subs.id)
subid = list(subids)

submission = r.get_submission(submission_id=subid[0])
print submission.score


















