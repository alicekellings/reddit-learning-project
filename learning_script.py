#!/usr/bin/env python3
"""
Personal Reddit Learning Project - Read-only data collection for learning
Fully compliant with Reddit Responsible Builder Policy
Author: u/yourredditusername
"""

import praw
import pandas as pd
from datetime import datetime

reddit = praw.Reddit(
    client_id="PLACEHOLDER",
    client_secret="PLACEHOLDER",
    user_agent="RedditLearningProject/1.0 (by u/yourredditusername; personal learning script)",
)

def collect_sample_data():
    print(f"[{datetime.now()}] Starting data collection for learning...")
    posts = []
    
    for submission in reddit.subreddit("AskReddit+explainlikeimfive+dataisbeautiful").new(limit=200):
        posts.append({
            "title": submission.title,
            "score": submission.score,
            "num_comments": submission.num_comments,
            "created_utc": datetime.fromtimestamp(submission.created_utc),
            "subreddit": submission.subreddit.display_name
        })
    
    df = pd.DataFrame(posts)
    df.to_csv(f"reddit_sample_{datetime.now().strftime('%Y%m%d')}.csv", index=False)
    print(f"Collected {len(posts)} posts for learning and analysis")

if __name__ == "__main__":
    collect_sample_data()