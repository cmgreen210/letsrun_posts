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
PageRank run the shell script `run.sh`. After scraping about 6 years worth of data (~350,000 unique posts) the top results look like:

(Flagpole,254.68371549897591)
                                                                                      
(malmo,209.10805804907693)

(rojo,204.06310929039265)

(Mr. Obvious,195.74662662938374)

(coach d,157.77407699252467)

(wejo,145.22868769259176)

(ventolin^3,137.62900254391593)

(agip,125.0166262025914)

(J.R.,111.32776981786107)

(Lorenzo the Magnificent,105.64026174782802)

(Sagarin,103.58223741464299)

(Bad Wigins,102.23172273767389)

(A Duck,101.99230086106138)

(douglas burke,100.91134857395454)

(ukathleticscoach,92.73667200811282)

(luv2run,88.22086095018223)

(Sprintgeezer,85.93270023131225)

(Conundrum,85.74788324534204)

(VIPAM,84.73958514742938)

(redux,83.70637649696344)

A few of these results make clear sense even if you're not
a frequent poster seeing as rojo and wejo are the brothers who
founded the website.


[letsrun]: http://www.letsrun.com/forum "LetsRun"
[scrapy]: http://scrapy.org/ "Scrapy"
[mongo]: https://www.mongodb.org/ "mongoDB"
[spark]: https://spark.apache.org/ "Spark"
[pagerank]: http://en.wikipedia.org/wiki/PageRank "PageRank"