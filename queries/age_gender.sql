select extract(year from now()) - cast(right(birthdate_customer, 4) as int) as age, gender_customer as gender, count(*) as people
from customer
group by age, gender
order by gender desc, age desc;