select date_transaction as date, count(*) as transaction
from transaction
group by date
order by date desc;