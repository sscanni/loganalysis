-------------------------------------------------------------
--1. What are the most popular three articles of all time? 
-------------------------------------------------------------
-- select CONCAT ('"', title, '"', ' -- ', num, ' views') from
-- (
-- select title, count(*) as num 
-- from articles join log
-- --on path like CONCAT('%/', slug)
-- on path = CONCAT ('/article/' , slug)
-- group by title
-- order by num desc limit 3
-- ) as subq
-- ;

--select slug from articles;
--on path = CONCAT ('/article/' , slug)
--on right(path, length(slug)) = slug
-------------------------------------------------------------
--2. Who are the most popular article authors of all time? 
-------------------------------------------------------------
-- select CONCAT (name, ' -- ', num, ' views') from
-- (
-- select name, count(*) as num 
-- from authors a
-- join articles b
-- on a.id = b.author
-- join log
-- on path = CONCAT ('/article/' , slug)  
-- on right(path, length(slug)) = slug
 -- group by name
-- order by num desc
-- ) subq;
-----------------------------------------------------------
--3. On which days did more than 1% of requests lead to errors? 
-----------------------------------------------------------
--drop view BadReqs;

create view BadReqs as
select date_trunc('day', time) as logdate, count(*) as BadCount
from log
where left(status,1) in ('4', '5')
group by logdate
order by logdate
;

-- --order by logdate desc
-- -- drop view TotReqs;

-- create view TotReqs as
-- select date_trunc('day', time) as logdate, count(*) as TotCount
-- from log
-- group by logdate
-- order by logdate
-- ;


-- select TO_CHAR(logdate :: DATE, 'Mon dd, yyyy'), CONCAT(TO_CHAR(percentage, '99D99'), '%')  
-- from
--  (select b.logdate, CAST(BadCount as numeric) / TotCount * 100 as percentage      
--   from BadReqs b
--   join TotReqs c
--   on b.logDate = c.logdate
--   where (CAST(BadCount as numeric) / TotCount * 100) > 1.00
--   order by percentage desc
--   ) as q;




   
