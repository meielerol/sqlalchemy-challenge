# sqlalchemy-challenge

Checking out the climate in Honolulu, Hawaii to make plans for a surfing vacation.

<p align="center"><img src="https://github.com/meielerol/sqlalchemy-challenge/blob/main/images/image.png" alt ="Honolulu Surf"></p>

## Climate Analysis and Exploration

The analysis can be found in the [climate-analysis.ipynb](https://github.com/meielerol/sqlalchemy-challenge/blob/main/climate_starter.ipynb) notebook. Data was drawn from the [hawaii.sqlite](https://github.com/meielerol/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite) database.

Percipitation inches over the last year of the data for the most active station is shown in the bar graph below.

<p align="center"><img src="https://github.com/meielerol/sqlalchemy-challenge/blob/main/output-data/Percipitation-Chart.png" alt="Percipitation Inches vs Date Bar Chart"></p>

Frequency of temperatures across the various stations is shown in the histogram below.

<p align="center"><img src="https://github.com/meielerol/sqlalchemy-challenge/blob/main/output-data/ActiveStation-Temp-Chart.png" alt="Frequency vs Temperature (F) Histogram"></p>

## Climate App

The climate [app.py](https://github.com/meielerol/sqlalchemy-challenge/blob/main/app.py) lists all available routes on the home page. Users can find various json APIs with the data from the [hawaii.sqlite](https://github.com/meielerol/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite) database.

## Extra Analyses

### Temperature

For the selected dates, 8/23/2016-8/23/2017, the bar chart shows the average temperature of the stations with an error bar.

<p align="center"><img src="https://github.com/meielerol/sqlalchemy-challenge/blob/main/output-data/AvgTemp-Chart.png" alt="Average Trip Temperature (F)"></p>