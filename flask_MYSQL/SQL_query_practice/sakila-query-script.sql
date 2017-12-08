#1
SELECT customer.first_name, customer.last_name, customer.email, concat_ws(', ', address.address, address.address2, city.city, country.country)
FROM CUSTOMER
	JOIN address ON customer.customer_id = address.address_id
	JOIN city ON address.address_id = city.city_id
	JOIN country ON address.address_id = country.country_id;

#2
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS category
FROM film
	JOIN film_category ON film.film_id = film_category.film_id
	JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

#3
SELECT actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) AS name, film.title, film.description, film.release_year
FROM actor
	JOIN film_actor ON film_actor.actor_id = actor.actor_id
	JOIN film ON film.film_id = film_actor.film_id
WHERE actor.actor_id = 5;

#4
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
	JOIN address ON customer.address_id = address.address_id
	JOIN city ON address.city_id = city.city_id
WHERE customer.store_id = 1
	AND city.city_id IN (1, 42, 312, 459);

#5
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
	JOIN film_actor ON film_actor.film_id = film.film_id
WHERE special_features LIKE '%Behind%' 
	AND rating = 'G' 
	AND film_actor.actor_id = 15;

#6
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name,' ',actor.last_name)
FROM film
	JOIN film_actor ON film_actor.film_id = film.film_id
    JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

#7
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS category
FROM film
	JOIN film_category ON film_category.film_id = film.film_id
    JOIN category ON category.category_id = film_category.category_id
WHERE film.rental_rate = 2.99
	AND category.name = 'Drama';

#8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS category, CONCAT(actor.first_name, ' ',actor.last_name) AS actor
FROM film
	JOIN film_category ON film_category.film_id = film.film_id
    JOIN category ON category.category_id = film_category.category_id
    JOIN film_actor ON film_actor.film_id = film.film_id
    JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.first_name = 'SANDRA'
	AND actor.last_name = 'KILMER'
    AND category.name = 'Action';
