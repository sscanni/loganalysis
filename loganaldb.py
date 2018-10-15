#!/usr/bin/env python2
# "Database code" for the Website Log Analysis Program.

# Note:
# Used this: "on path = CONCAT ('/article/' , slug)"
# instead of this: "on path like CONCAT('%/', slug)"
# because the first statement performed much better.

import psycopg2

DBNAME = 'news'


def get_loginfo(infoparm):

    # Retrieve the Most Popular Three Articles of All Time
    if infoparm == '1':
        sqltext = """select
              CONCAT ('"', title, '"', ' -- ', num, ' views') from
              (select title, count(*) as num
                  from articles join log
                  on path = CONCAT ('/article/' , slug)
                  group by title
                  order by num desc limit 3
              ) as subq;
          """
    # Retrieve the Most Popular Article Authors of All Time
    elif infoparm == '2':
        sqltext = """select CONCAT (name, ' -- ', num, ' views')
                  from
                  (select name, count(*) as num
                  from authors a
                  join articles b
                  on a.id = b.author
                  join log
                  on path = CONCAT ('/article/' , slug)
                  group by name
                  order by num desc
                  ) as subq;
                  """
    # Retrieve the Days with More Than 1% of Requests Leading to Errors
    elif infoparm == '3':
        sqltext = """select CONCAT(TO_CHAR(logdate :: DATE, 'Mon dd, yyyy')
                    , ' -- ',
                    CONCAT(TO_CHAR(percentage, '99D99'), '%'), ' errors')
                    from
                    (select b.logdate, CAST(BadCount as numeric) / TotCount
                      * 100 as percentage
                      from BadReqs b
                      join TotReqs c
                      on b.logDate = c.logdate
                      where (CAST(BadCount as numeric) / TotCount * 100) > 1.00
                      order by percentage desc
                      ) as q;
                  """
    else:
        print('unknown request - should not happen')

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sqltext)
    logdata = c.fetchall()
    db.close()
    return logdata
