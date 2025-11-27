# Reddit Learning Project

A personal, non-commercial Python project to practice using the Reddit API and learn data analysis.

## Purpose (Fully compliant with Reddit's Responsible Builder Policy)
This is a **personal learning and experimentation project** only. I am teaching myself:
- How to use PRAW and OAuth2
- Basic data analysis with pandas
- Working with public Reddit data responsibly

**No commercial use · No AI training · No data resale · No automation beyond reading public posts**

## What the script does (read-only)
- Fetches the newest 100–500 posts from a few public subreddits I enjoy
- Saves only: title, score, number of comments, creation time, subreddit name
- Performs simple statistics (e.g., most active hours, average score)
- All data is stored locally and deleted after analysis

## Subreddits currently used (all public, high-traffic)
- r/AskReddit
- r/explainlikeimfive
- r/dataisbeautiful
- r/todayilearned
(These may change as I explore different topics)

## Technical details
- Python + PRAW
- Read-only OAuth2 scope: identity, history, read
- Rate: maximum 30–40 requests per minute
- User
