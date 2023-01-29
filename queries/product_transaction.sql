select product_transaction as product, sum(amount_transaction) as transaction
from transaction
group by product
order by transaction desc;