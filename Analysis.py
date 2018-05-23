#!/usr/bin/env python

import psycopg2
DBNAME = "news"

"who are most popular three articles"
queryOne = '''select title,count(*) as num from articles,log where log.path
like concat('%',articles.slug) group by articles.title order by num desc
limit 3'''

"who are most popular article authors"

queryTwo = '''select authors.name,count(*) as views from authors,articles,log
where  authors.id = articles.author and log.path like concat('%',articles.slug)
group by authors.name order by views desc'''

"which day the error were more than 1%"

queryThree = '''select to_char(date(time),'Mon DD,YYYY'),
(sum(case log.status when '200 OK' then 0 else 1 end)*100.0/count(log.status))
as num from log group by date(time) order by num desc limit 1'''


def get_result(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    print('The result of the query is---------: \n')
    for result in data:
        print(result[0], '--------->', result[1])
    db.close()
    return data

print('  \n \n which are most popular three articles\n')
get_result(queryOne)
print(' \n \n who are most popular article authors\n ')
get_result(queryTwo)
print(' \n \nwhich day the error were more than 1%\n')
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute(queryThree)
data = c.fetchall()
print('The result of the query is---------: \n')
print("%s --------->%.1f" % (data[0][0], data[0][1])+"% errors")
db.close()

