# Youtube comments scraper

Scrapes the comments (only main ones without the replies), number of likes and approximate date of posting from a YouTube video
provided the url. Saves the data either as a json or as a csv

Dates of posting are approximated based on the label above the comments (such as "three month ago")

## Usage 

I used Google Chrome as a browser. If it is installed and added to path it should work just fine 

Libraries required are in ``` requirements.txt ```

To use run in command line: 

```
python comments_scraper.py [url] [number_of_times_to_scroll] [type_to_save_as] [name_of_the_file_to_save_as] 
```
Where:

- [url] : url of the video (i.e https://www.youtube.com/watch?v=YbJOTdZBX1g)
- [number_of_times_to_scroll] : how many times the script will scroll down in the comments section to load the comments. 
Bigger number means more scraped comments, but it might take longer.
- [type_to_save_as] : desired type to save as. (either csv or json)
- [name_of_the_file_to_save_as] : name of the file to save as without the document type (i.e test)

Example:

```
python comments_scraper.py https://www.youtube.com/watch?v=YbJOTdZBX1g 100 json test 
```
Examples of output are in ```test.csv``` and ```test.json```