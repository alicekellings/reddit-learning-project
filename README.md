# Reddit ModSafe Tool

A fully open-source, non-commercial moderator assistance tool for removing spam and prohibited links.

## Purpose (Fully compliant with Reddit's Responsible Builder Policy)
- Used only in subreddits where I am an active moderator
- Automatically detects and removes posts containing banned domains
- Removes duplicate/repetitive spam posts
- Generates simple daily moderation reports
- **Never** used for AI training, data resale, advertising, voting manipulation, or auto-commenting

## Target subreddits (I have moderator permissions)
- r/yoursubreddit1
- r/yoursubreddit2
(Replace with your actual subreddits)

## Technical details
- Language: Python 3 + PRAW
- Authentication: OAuth2 using my moderator account only
- Expected request rate: ≤ 40 requests/minute (well below 60 rpm limit)
- Logs retained for max 7 days, then permanently deleted
- User-Agent: ModSafeTool/1.0 (by u/yourredditusername; non-commercial moderator tool)

## Privacy & Compliance
- No personal user data is collected or stored
- No long-term retention of post/comment content
- Source code is fully public and available for review at any time
- Strictly follows Reddit API Terms of Use and Responsible Builder Policy

## License
MIT License – free for anyone to use, modify, and distribute

Contact: u/yourredditusername
