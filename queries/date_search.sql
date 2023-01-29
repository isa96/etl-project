select date_search as date, count(*) as search
from search
group by date
order by date desc;