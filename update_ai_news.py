import feedparser
import re
import datetime

# 1. Fetch the Google News RSS feed for Artificial Intelligence
RSS_URL = 'https://news.google.com/rss/search?q="Artificial+Intelligence"&hl=en-US&gl=US&ceid=US:en'
feed = feedparser.parse(RSS_URL)

# 2. Format the top 5 articles into a Markdown list
today = datetime.datetime.now().strftime("%B %d, %Y")
news_markdown = f"*(Last updated: {today})*\n\n"

for entry in feed.entries[:5]:
    news_markdown += f"- [{entry.title}]({entry.link})\n"

# 3. Read your current README
with open('README.md', 'r') as f:
    content = f.read()

# 4. Replace the old news with the new news using a regular expression
new_content = re.sub(
    r'.*?',
    f'\n{news_markdown}\n',
    content,
    flags=re.DOTALL
)

# 5. Save the updated README
with open('README.md', 'w') as f:
    f.write(new_content)
