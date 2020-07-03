# Learning how to do web scraping

I was interested in learning how to do web scraping, and also had a friend who approached me with a fun problem: She wanted to scrape posts from fitness-related accounts and influencers on Instagram for info about upcoming fitness classes to add to a schedule. My favorite part about programming is coming up with tricky problems and tinkering around to solve them and learning a ton in the process. 

While web scraping is not always allowed and Instagram certainly isn't designed to have data pulled from it, I figured I could experiment on a very small scale as a learning exercise.

I also wanted to use Python for my web scraping because I have been wanting to use the language more. In the last few months, I've spent most of my time writing in JavaScript and Ruby but the first programming language I learned in college was Python. I wanted to go back to my routes.

The imdb-scraper.py file contains my first experiment using a tutorial to learn the basics of scraping on a site with easy-to-access elements and clear class names. The instagram-scraper.py file contains my explorations of looking at Instagram, which is much harder to scrape because their class names are created dynamically through flexbox. 

This is a work in progress, but what I ended up with is a command line tool that allows you to input the tag name you want to search. The scraper then looks at the nine posts in the featured section and accumulates the comments into an array. As a next step, I will look at searching the comments for particular phrases like "am/pm" or days of the week to see if I can determine if they include a schedule.

![Instagram Results](/instagram-result.png)

