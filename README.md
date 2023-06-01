# Roster-Scraper
A Python script (using Selenium) to Scrape and convert online roster Data to Calendar files (.ics)

## Video Demo
[I understand most people won't ever be able to run this code without a coles login so click to download the video!](https://github.com/James-Nunn/Roster-Scraper/blob/3be6c42a1749ccae16798a1064b8f8ca34c47324/Roster%20Scraper.mp4)

## Problem
My family shares a calendar and likes it to be up to date with my shifts at work. The process of checking my shifts and making calendar events every week became tedious and repetitive very quickly. My current wisdom is that tedious and repetitive tasks tend to be perfect for digital solutions so I got to work making this during my down time. 

## The Roster Data 
<img src="https://github.com/James-Nunn/Roster-Scraper/blob/main/Screenshot%202023-05-31%20at%209.05.39%20am.png?raw=true" height="300px">
<br>
The image above shows a grid like week long roster and a modal that shows each day with a shift assigned. 
After my script heads to the login page and signs me in it redirects me to my roster page when it detects that the home page has been loaded. The script uses 

```python
time.sleep(seconds)
```

Because an expected condition could not be used due to the server reloading the homepage before finally navigating back to my roster page. 

## Scraping
I could have the script navigate to the next week tab select the modals and scrape the data for each day however there was an easier way. Each html element had date-data attribute but I also couldn't access that because selenium would print 'none' during my tests (my guess is because the backend dynamically updates the html afterward). My final solution was to loop through all the days as the roster is (see behind the modal). Then using ICS and datetime I convert the time BNE from ZULU and save a calendar file for each. 
