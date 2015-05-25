# Letsrun Posts
In this project we explore the connections between forum posting
and responses on the Letsrun.com's [forum][letsrun], a popular 
running/track and field website. We'll use
the Python web scraping framework [Scrapy][scrapy] to obtain
the forum posts, [mongoDB][mongo] to store the post information,
and [Spark][spark] to analyze the graph of post connections.

## Scraping
In order to scrape the posts from the forums run the following command:
```
$ scrapy crawl -L ERROR
```
from the `crawl` folder. Once we've scraped enough posts export it
to a text file using the `mongoexport` command.

## Graph Analysis
Now to find the most "important" posters, i.e. those with the highest
PageRank run the shell script `run.sh`. After scraping about 6 years
worth of data the top results look like:

![Ranking](img/rank.jpg)

A few of these results make clear sense even if you're not
a frequent poster seeing as rojo and wejo are the brothers who
founded the website.

[letsrun]: http://www.letsrun.com/forum "LetsRun"
[scrapy]: http://scrapy.org/ "Scrapy"
[mongo]: https://www.mongodb.org/ "mongoDB"
[spark]: https://spark.apache.org/ "Spark"
[pagerank]: http://en.wikipedia.org/wiki/PageRank "PageRank"