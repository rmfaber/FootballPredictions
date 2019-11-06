# FootballPredictions

A project mainly for fun and personal development. The endgoal is to build a machine-learning model that predicts the results for football matches. In doing so I would like to improve the following skills: web-scraping, creating neat data frames from raw data, general programming, project organisation, and machine learning.

Obviously this dream is still very far away. I have divided the project into the following bits, each of which is again divided into multiple subtasks.

# Web-scraping
A preliminary search found no freely accessible pre-processed data for the Eredivisie, although that data might be out there. The goal here is to produce this type of neat data from human-readable websites, so as to learn and build webscraping proficiency.

The final end-product of this step are the results for each match in the Eredivisie going back in time as far as possible. 

* Produce the results from one round of matches
* Produce the results from one year of matches
* Produce the results from the last decade of matches
* Produce the results for all of the matches available on the website

A potential wish here is to also include other information about the football clubs. European matches and transfers are the obvious targets.

# Data Pre-processing
To be able to predict future matches and train a machine learning model we need to get our data into the right format. The label of our machine learning model will be either the result (win, draw, loss) per match or the number of goals scored per team. The features might be the form of the team (results of last X matches), the historic placement of the team (last years final standings for example), whether the match is away or home, the time of season, and similar information about the opponent.

We thus need to create multiple dataframes: the final standings of each season (ideally made simply from the results of all matches in that season), the matches within a season, a frame with all historic matches, and possibly more.

# Machine Learning

Using this data-frame we can try multiple machine learning methods, comparing their predictive performance and generalibility. We'll see how much data we can acquire before we can break this step down into multiple subtasks.
