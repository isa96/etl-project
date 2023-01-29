select *
from 
(
select country_customer as country, count(*) as transaction
from transaction as tr
left join customer as cs
on tr.id_customer = cs.id_customer
group by country
order by transaction desc
) 
as tr_null
where country is not null;