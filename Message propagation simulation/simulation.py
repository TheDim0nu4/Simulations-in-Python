import random
from news import News, CATEGORIES
from person import Person
from population import Population, HomogeneousPopulation
import numpy

def simulate_spread(all_news, population):
    
    result = dict()
    for news in all_news:
        readers_count = [0, 5]
        first_5_readers = population.introduce_news( news )
        readers = []
        for person in population.people:
            if person.process_news( news, 1 ) != [] and person not in first_5_readers:
                readers.append(person)

        readers_count.append( population.get_number_of_interested( news.category ) )
        
        result[news] = readers_count
 
    return result



def average_spread_with_excitement_rate(excitement_rate, pop_size, friends_count, patience_limit, test_count=100):
    count = []
    for _ in range(test_count):
        news = News( random.choice(CATEGORIES), excitement_rate, 10, 1)
        population = Population( pop_size, friends_count, patience_limit)
        news_sim = simulate_spread( [news], population)
        count.append( news_sim[news][-1] )
    
    return count, sum(count)/len(count)


def excitement_to_reach_percentage(percentage, pop_size, friends_count, patience_limit):
    population = Population( pop_size, friends_count, patience_limit )
    news = News( random.choice(CATEGORIES), 0.01, 10, 1 )

    for i in numpy.arange(0.01, 1.01, 0.01):
        news.excitement_rate = i
        all_news = [news, ]
        people = simulate_spread(all_news, population)[news][-1]
        readers_categ = population.get_number_of_interested(news.category)
        if abs(people/readers_categ - percentage) < 0.05:
            return i
   
    return 


def excitement_to_reach_percentage_special_interest(percentage, pop_size, friends_count, patience_limit, news_category):
    population = HomogeneousPopulation(pop_size, friends_count, patience_limit, news_category)
    news = News( news_category, 0.01, 10, 1)

    for i in numpy.arange(0.01, 1.01, 0.01):
        news.excitement_rate = i
        all_news = [news, ]
        people = simulate_spread(all_news, population)[news][-1]
        readers_categ = population.get_number_of_interested(news.category)
        if abs(people/readers_categ - percentage) < 0.05:
            return i
   
    return 



if __name__ == '__main__':
    pass
