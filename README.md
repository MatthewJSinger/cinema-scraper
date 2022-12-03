![Cinema Scraper](Banner.png)
A script to find out what's on at the cinema
## Usage
This project works by scraping data from the following website: [Data Thistle](https://film.datathistle.com/)
The Cinema class can be used to scrape all the information of all the movies playing at that cinema for the next week.
Import it like this:
```python
from CinemaScraper import Cinema
```
The Cinema class takes 1 or 2 arguments, the first being the name of the cinema, the second being the link to the page to scrape. If a link is not provided the script will attempt to find a cinema based on the name passed. For example; both of these work:
```Python
    cinema = Cinema("Vue Manchester", "https://film.datathistle.com/cinema/43008-vue-manchester-printworks")
```
```python
    cinema = Cinema("Vue Manchester")
```
##### Methods of Cinema include:
| Method           | Description                                                        |
|------------------|------------------------------------------------------------------- |
| getAllMovieData  | Returns a list of Movie objects containing movie data              |
| printAllShowings | Neatly outputs all of the Movies and their times shown             |
| printWhatsOn     | Neatly outputs only the Movie titles of everything that is playing |
##### Movie Class
The Movie Class stores the following data:
    - Title
    - Description
    - Show Times
    - Link to poster image
These can be accessed with the following:
```python
    Movie.title
    Movie.description
    Movie.showTimes
    Movie.image
```
##### The Curator
The curator is a class that handles the scraping i.e. fetching the data.
Movie data can be fetched directly from a page using the curator class and returned as a list without instantiating a Cinema object
```python
from CinemaScraper import Curator
Curator().fetchMovieData(https://film.datathistle.com/cinema/43008-vue-manchester-printworks")
```
