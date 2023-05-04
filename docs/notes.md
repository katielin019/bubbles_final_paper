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
    - Using [Star_Trek_Scripts/scrape.py](https://github.com/GJBroughton/Star_Trek_Scripts/blob/master/scrape.py) to help with test transcript retrieval
- Got script text!! [Super helpful link](https://proxyway.com/knowledge-base/how-to-get-text-from-div-using-beautifulsoup)
    - Now I need to write the script to clean text and figure out how I want to approach structuring the text data :/
### 09:57 PM
- Got the script working for cleaning the text and got the export stuff working too. Now I just need to figure out what's happening with the weird formatting and fix it...
- For removing character names [link](https://stackoverflow.com/questions/49281051/removing-capital-letters-from-a-python-string)
### 11:09 PM
- I want to be done for the evening. I'm fuckin exhausted, man.
- Things I need to do tomorrow:
    1. Write a function to split a string into its sentences and place each sentence inside an array. Then, use that array to write to a .txt file with one sentence per line.
    2. See if this text file has a different entropy than the unformatted one (has extra whitespace and no line breaks).
    3. Write a function to add season and episode data separately to each dataframe. Then write the lambda function to apply this to all dataframes in datadict. Save this new datadict as a new pickle.
    4. Iterating through each show, group the dataframe by seasons and run a "get episode transcript" script for each episode of the season.
        - Also!!! Need to go through each show and write tiny individual scripts to clean specific text anomalies.
    5. Iterating through each show, run a lambda function to calculate the entropy for each individual epsiode.
        - (It might be helpful if I could get the air date for each episode, but that's a bells and whistles add-on)
    6. Make a new dataframe that has every single show, its start and end date, seasons 1-n, and the average entropy for a given season.
    7. Make a new dataframe that calculates the average entropy per show.
    8. Plot things
### Wed May 3
#### 01:03 PM
- Since my last update, I've gotten a sizable chunk of work done.
    - Last night/early this morning, I separated all of the shows by decade to make the data a little bit easier to process instead of trying to handle all 43 shows at once
    - Today, I processed the decade files into dataframes, used those dataframes to get individual episode data for each show, and wrote a function to scrape transcripts from the episode data
    - In the past hour or so, I scraped all of the transcripts for shows that began airing in the 1960s
- I found a [repo](https://github.com/creyD/entro.py) that calculates the Shannon Entropy of a given string or file
    - I had a little trouble figuring out the installation process at first, but [this guide](https://adamj.eu/tech/2019/03/11/pip-install-from-a-git-repository/) was super helpful!
- After my 373 team meeting, I'm gonna take a quick break and then install the entropy calculator and test it out with a function that will parse txt files with a season's worth of episode transcripts into their individual episodes
    - I also need to have a function that will impute the respective entropies of each episode into the dataframe for each decade
    - Later, once I repeat this process for each decade, I'll append each dataframe (including some sort of date/year markers)
#### 03:43 PM
- Installed the entro.py package! Gonna test it out in a sec
- (04:32 PM) Still working on trying to test it out. I have to split the season files into individual episodes first.
    - Just hit a breakthrough though, thanks to [this post](https://pynative.com/python-regex-split/), among others
    - I think it should nearly be smooth sailing from here in terms of being able to test the entropy calculator
#### 08:13 PM
- Took a solid break and am almost ready to jump back in... gonna quickly test one other season corpus to make sure everything is functioning correctly.