import random
from news import News

class Person:
    def __init__(self, threshold, interested_in, patience):
        self.threshold = threshold
        self.interested_in = interested_in
        self.friends_list = list()
        self.has_read = list()
        self.patience = patience

    def is_interested_in(self, category):
        return category in self.interested_in

    def has_read_news(self, news):
        return news in self.has_read

    def make_friends(self, population, n):
        for _ in range(n):
            self.friends_list.append(random.choice(list(filter(lambda x: x != self and x not in self.friends_list, population))))

    def process_news(self, news, time_step): 
        if news in self.has_read:
            return []
        
        if news.category not in self.interested_in:
            return []
         
        if news.get_excitement( time_step ) < self.threshold:
            return []
        
        self.has_read.append(news)
  
        return list( filter( lambda x: news.category in x.interested_in, self.friends_list ) )
