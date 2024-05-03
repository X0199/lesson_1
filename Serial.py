class MyShows:

    def __init__(self, serial, platform, first_series_year, actors=[], serie=1, rate=None):
        self.__rate = rate
        self.__serie = serie
        self.__actors = actors
        self.__first_series_year = first_series_year
        self.__platform = platform
        self.__serial = serial
        # self.__serial = "Breaking Bad"
        # self.__place = "Netflix"
        # self.__first_series_year = 2008

    @property
    def rate(self):
        return self.__rate

    @property
    def serie(self):
        return self.__serie

    @property
    def actors(self):
        return self.__actors

    @property
    def first_series_year(self):
        return self.__first_series_year

    @property
    def platform(self):
        return self.__platform

    @property
    def serial(self):
        return self.__serial

    @serie.setter
    def serie(self, num):
        return self.__serie == num

    @rate.setter
    def rate(self, rating):
        return self.__rate == rating

    @rate.deleter
    def rate(self):
        if self.__rate in range(0, 11):
            del self.__rate
            return self.__rate
        elif self.__rate == None:
            return "Rate the movie: "

    def actor_changer(self, old, new):
        if old in self.__actors:
            self.actors.remove(old)
            self.actors.append(new)
            return self.__actors
        else:
            return f"No old in {self.__actors}: "

    def info(self):
        return {'Series Name': self.__serial,
            'Platform': self.__platform,
            'First Series Year': self.__first_series_year,
            'Current Serie': self.__serie,
            'Rate': self.__rate,
            'Actors': self.__actors
            }



user = MyShows("Breaking Bad", "Netflix", 2008, ["Bryan Cranston", 'Aaron Paul', "Anna Gunn", "Dean Norris", "RJ Mitte"], 5,10)
print(user.__dict__)
user.actor_changer("RJ Mitte", "Jonathan Banks")
# print(user.actors)
# print(user.rate)
print(user.info())