//1 
select customer.first_name , customer.last_name ,customer.email ,customer.address_id
from customer
inner join address on address.address_id = customer.address_id
where city_id= 312

//2

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name 
from film
inner join film_category on film_category.film_id = film.film_id
inner join category on category.category_id =film_category.category_id
where category.name = 'comedy'

