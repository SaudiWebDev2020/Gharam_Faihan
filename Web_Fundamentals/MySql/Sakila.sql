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

//3
SELECT actor.actor_id,film.title, film.description, film.release_year 
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id 
join actor on actor.actor_id = film_actor.actor_id
WHERE film_actor.actor_id = 5

//4

SELECT customer.first_name , customer.last_name, customer.email , customer.address_id
FROM customer 
JOIN store ON store.store_id=customer.store_id
JOIN address ON address.address_id=customer.address_id
JOIN city ON address.city_id=city.city_id
WHERE store.store_id=1 AND city.city_id IN (1, 42, 312, 459)

//5

SELECT film.title , film.description, film.release_year, film.rating ,film.special_features
FROM film 
WHERE film.rating = "G" AND film.special_features LIKE 'behind the scenes'

//6

SELECT film.film_id , film.title , actor.actor_id , actor.first_name , actor.last_name 
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id 
join actor on actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369

//7

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id 
WHERE film.rental_rate = 2.99 AND category.name = 'Drama'

//8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name , actor.first_name, actor.last_name 
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER'


