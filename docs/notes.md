# Notes
### Tue May 2
#### 02:47 PM
- [Possible format for meta-data](https://github.com/4m4n5/the-seinfeld-chronicles/blob/master/episode_info.csv)
    - csv file with entries that log the following:
        - season
        - episode number
        - title
        - air date
        - writers (probably don't need this)
        - director
        - SEID
            - ex: "S01E01"
    - From [the-seinfeld-chronicles](https://github.com/4m4n5/the-seinfeld-chronicles) on GitHub
- [How To Web Scrape Wikipedia Using Python, Urllib, Beautiful Soup and Pandas](https://alanhylands.com/how-to-web-scrape-wikipedia-python-urllib-beautiful-soup-pandas/)
    - For scraping series metadata
- Search: "csv data to python dictionary"
    - [Creating a dictionary from a csv file? | StackOverflow](https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file)
### 05:19 PM
- I got the data I wanted by scraping Wikipedia and then narrowed down my list to a total of 43 tv shows
- Now, I want to try web scraping to get show transcripts (which I'll then have to clean)
    - [Star Trek webscraping script](https://github.com/BirkoRuzicka/Star-Trek-Transcripts/blob/main/StarTrek_webscraping.py)
    - [scraping a website that requires you to scroll down | StackOverflow](https://stackoverflow.com/questions/45620396/scraping-a-website-that-requires-you-to-scroll-down)
### 08:15 PM
- Used BeautifulSoup to get all of the episode urls and id's for every show
    - [BeautifulSoup | Dev Cheatsheets](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/libraries/beautifulsoup.html)
- Saved the dfdict to a pickle in case something happens and my shit gets lost
- Don't think I need [this](https://towardsdatascience.com/scraping-from-all-over-wikipedia-4aecadcedf11) anymore
- Now I need to actually scrape every single episode and then clean its text and then calculate its entropy... rip