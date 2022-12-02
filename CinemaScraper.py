import requests
from bs4 import BeautifulSoup

def parseDay(shortDayInput):
    shortDay = shortDayInput.split(" ")[0]
    easyDays = ["Mon","Fri","Sun"]
    if shortDay in easyDays:
        return shortDay.title() + "day"
    elif shortDay == "Tue":
        return "Tuesday"
    elif shortDay  == "Wed":
        return "Wednesday"
    elif shortDay == "Thu":
        return "Thursday"
    elif shortDay == "Sat":
        return "Saturday"
    else:
        raise ValueError(shortDay)

def extractDetails(movies):
    movieList = []
    
    for movieData in movies:
        try:
            name = movieData.h4.get_text()
            description = movieData.p.get_text()
            movie = Movie(name,description)
            rawDays = movieData.findAll('h5')
            for rawDay in rawDays:
                day = parseDay(rawDay.get_text())
                timeParent = rawDay.find_next_sibling("div")
                rawTimes = timeParent.find_all("li")
                times = [time.time.get_text() for time in rawTimes]
                movie.addShowing(day,times)
            movieList.append(movie)
        except AttributeError:
            pass
            
    return movieList

def getURL(searchQuery):
    baseURL = "https://film.datathistle.com/search/what:"
    URL = baseURL + searchQuery
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "lxml")
    rawLink = soup.select(".placeSummary a")[0]
    link = rawLink.get('href')
    return "https://film.datathistle.com/" + link


    
 

class Cinema:
    def __init__(self,name,*args):
        self.name = name
        if len(args) > 0:
            self.URL = args[0]
        else:
            self.URL = getURL(self.name)


        self.movieInfo = self.getData()
        
    def __repr__(self):
        return self.name
    
    def getData(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "lxml")
        parent = soup.find(class_="eventSchedules")
        movies = parent.findChildren("div", recursive=False)
    
        movieList = extractDetails(movies)
        return movieList
    
    def getAllShowings(self):
        return self.movieInfo

    def printAllShowings(self):
        print(f"----------{self.name}----------")
        movieList = self.movieInfo
        for movie in movieList:
            times = movie.getAllTimes()
            print(movie)
            for key in times:
                timeStrings = times[key]
                print(key + " : " + ", ".join(map(str,timeStrings)))
            print("\n")

    def printWhatsOn(self):
        print(f"----------{self.name}----------")
        for movie in self.movieInfo:
            print(movie)

        

class Movie:
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.showTimes = {'Monday': [],
               'Tuesday': [],
               'Wednesday': [],
               'Thursday': [],
               'Friday':[],
               'Saturday': [],
               'Sunday': []}
    def addShowing(self,day,times):
        if len(self.showTimes[day]) == 0:
            self.showTimes[day] = times
    def getTimesForDay(self,day):
        return self.showTimes[day]
    def getAllTimes(self):
        tempDict = {}
        for key in self.showTimes.keys():
            if len(self.showTimes[key]) != 0:
                tempDict[key] = self.showTimes[key]
        return tempDict        
    def __repr__(self):
        return self.title
