# Relay Payments - Data Engineer Exercise


## Objective

This exercise is intended to be a gauge of technical fit. Instead of building everything from scratch - we've provided a basic project structure that resembles what you might find when entering a new role with an existing codebase. You'll find several well documented libraries in use - but feel free to not use them if you so choose. 

## Installation & Pre-Requisites
This test example is built with Python, dlt, dbt, and duckdb. 

You should only need to install `duckdb` outside of pip. You can do so from [here](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=package_manager)

1. Clone the Repo
2. Install the dependencies `pip install -r requirements.txt`
3. Confirm you can run the baseline of the project

```bash
$ python space_x_data.py
$ cd dbt
$ dbt build
```

## Instructions & Deliverable

Your goal is to add functionality to the existing code that meets the criteria in the sections below. We expect that this exercise should take between 2-4 hours. We're not looking for perfect - but that you can make reliable assumptions about the data you're working with and understand tradeoffs in how you build your solution. 

Get through as much as you can in the allotted time. Even if you haven't gotten all the way through it, send over what you have. 

The final deliverable should be a zip file with instructions about how to run it. Include a quick blurb in the Readme about if/where you got stuck and how you might have worked around it. 

### Data Ingestion & Storage
- It should ingest data about [SpaceX Rocket Launches & Launch Locations](https://github.com/r-spacex/SpaceX-API/blob/master/docs/launches/v4/all.md) into DuckDB. It should also include geo data about where the rocket launch took place. 
- It should ingest [Earthquake data from USGS](https://earthquake.usgs.gov/fdsnws/event/1/) from the beginning of 2012 to the end of 2022 into DuckDB, including GEO data about where the earthquake occurred. This should include only earthquakes of > 5 magnitude.

### Data Modeling
You've been tasked with building a data model(s) that help answer a few key questions from the data we've ingested above. You should modify the existing dbt project to complete this task. 

How many successful SpaceX launches have their been? How many of those launches had an earthquake of > 5 magnitude occur within 30 days and 2500 miles of them? 


### Extending the base

Lastly, your users have reviewed the findings, and would like to expand the scope of our earthquake data. They'd like to expand our earthquake data to include earthquakes of > 2 magnitude. 






