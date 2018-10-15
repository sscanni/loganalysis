create view BadReqs as
select date_trunc('day', time) as logdate, count(*) as BadCount
from log
where left(status,1) in ('4', '5')
group by logdate
order by logdate
;

create view TotReqs as
select date_trunc('day', time) as logdate, count(*) as TotCount
from log
group by logdate
order by logdate
;