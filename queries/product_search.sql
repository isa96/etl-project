select product_search as product, count(*) as search
from search
group by product
order by search desc;