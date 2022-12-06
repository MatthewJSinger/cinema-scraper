<div align="center">
    <img src="Banner.png" alt="Cinema Scraper"/>
</div>

A script to find out what's on at the cinema (UK). Written in Python.

**Requires:** Beautiful Soup 4

## Usage
This project works by scraping data from the following website: [Data Thistle](https://film.datathistle.com/).
The Cinema class can be used to scrape all the information of all the movies playing at that cinema for the next week.
The Cinema class takes 1 or 2 arguments, the first being the name of the cinema, the second being the link to the page to scrape. If a link is not provided the script will attempt to find a cinema based on the name passed. For example; both of these work:
```Python
from CinemaScraper import Cinema
    cinema = Cinema("Vue Manchester", "https://film.datathistle.com/cinema/43008-vue-manchester-printworks")
    cinema = Cinema("Vue Manchester")
```

### Methods of Cinema include:
| Method           | Description                                                                      |
|------------------|--------------------------------------------------------------------------------- |
| getAllMovieData  | Returns a list of Movie objects containing movie data                            |
| getMovie         | Takes a movie title as paramater, returns corresponding movie object             |
| printAllShowings | Neatly outputs all of the Movies and their times shown                           |
| printWhatsOn     | Neatly outputs only the Movie titles of everything that is playing               |
### Movie Class
The Movie Class stores the following data:
- Title
- Description
- Show Times
- Link to poster image

    These can be accessed with the following:
```python
    movie.title
    movie.description
    movie.showTimes
    movie.image
```
### The Curator
The curator is a class that handles the scraping i.e. fetching the data.
Movie data can be fetched directly from a page using the curator class and returned as a list of movie objects without instantiating a Cinema object
```python
from CinemaScraper import Curator
Curator().fetchMovieData(https://film.datathistle.com/cinema/43008-vue-manchester-printworks")
```
## Example Usage
```python
from CinemaScraper import Cinema

def run():
    cinema = Cinema("Vue Manchester")
    movie = cinema.getMovie("The Menu")
    day = "Sunday"
    showTimes = movie.getTimesForDay(day)
    print(f'{movie.title} is playing at the following times on {day} at {cinema.name}}')
    for time in showTimes:
        print(time)
        
if __name == '__main__':
    run()
```
Output
```
The Menu is playing at the following times on Sunday at Vue Manchester Printworks
10:10
12:10
14:20
16:45
18:10
19:50
21:45
```
