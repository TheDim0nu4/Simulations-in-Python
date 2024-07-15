from person import Person
from news import CATEGORIES, News
import random

class Population:
    def __init__(self, n, friends_count, patience_limit):
        self.people = list()
        self.active_news = list()

        self.generate_population(n, friends_count, patience_limit)

    
    def generate_population(self, n, friends_count, patience_limit):
        for _ in range(n):
            rand_categ = list()
            for _ in range(4):
                rand_categ.append(random.choice(list( filter( lambda x: x not in rand_categ, CATEGORIES ) )))
            
            person = Person( random.random(), rand_categ, random.randint(patience_limit[0], patience_limit[1]) )
            self.people.append( person )

        for pers in self.people:
            pers.make_friends( self.people, friends_count)
               

    def introduce_news(self, news):
        result = []
        for person in self.people:
            if person.is_interested_in( news.category ):
                result.append( person )
            if len(result) == 5:
                break
      
        self.active_news.append(news)
        return result

   
    def update_news(self, time_step):
        for news in self.active_news:
            if news.get_excitement( time_step ) == 0:
                self.active_news.remove( news )
        

    def count_readers(self, news):    
        return len([ person for person in self.people if person.has_read_news(news)])

    
    def get_number_of_interested(self, category):
        return len([ person for person in self.people if person.is_interested_in( category )])


class HomogeneousPopulation(Population):
    def __init__(self, n, friends_count, patience_limit, category):
        self.category = category
        super().__init__(n, friends_count, patience_limit )

    def generate_population(self, n, friends_count, patience_limit):
        for _ in range(n):
            rand_categ = [self.category, ]
            for _ in range(3):
                rand_categ.append(random.choice(list( filter( lambda x: x not in rand_categ, CATEGORIES ) )))
            
            person = Person( random.random(), rand_categ, random.randint(patience_limit[0], patience_limit[1]) )
            self.people.append( person )

        for pers in self.people:
            pers.make_friends( self.people, friends_count)