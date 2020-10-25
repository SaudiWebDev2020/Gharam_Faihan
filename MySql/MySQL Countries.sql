//1
SELECT countries.name, languages.language, languages.percentage 
FROM countries 
JOIN languages ON countries.code = languages.country_code
WHERE language = 'Slovene'

//2
SELECT countries.name AS countries, COUNT(cities.id) AS number_cities
FROM countries
JOIN cities ON countries.code = cities.country_code
GROUP BY countries.code
ORDER BY COUNT(cities.id) desc

//3
SELECT cities.name , cities.population , countries.id
FROM cities
INNER JOIN countries ON cities.country_id=countries.id
WHERE countries.name= 'Mexico' and cities.population>500000
ORDER BY cities.population desc

//4

SELECT countries.name , languages.language , languages.percentage
FROM countries
INNER JOIN languages ON countries.code =languages.country_code
WHERE languages.percentage > 89
ORDER BY languages.percentage desc

//5

SELECT countries.name , countries.surface_area , countries.population
FROM countries
WHERE countries.surface_area < 501 and countries.population > 100000

//6

SELECT name , government_form , capital , life_expectancy
FROM countries
WHERE government_form= 'Constitutional Monarchy' and life_expectancy >75


//7
SELECT  countries.name , cities.name, cities.district , cities.population
FROM countries
INNER JOIN cities ON  cities.country_code = countries.code
WHERE countries.name = 'Argentina' AND cities.district='Buenos Aires'

//8

SELECT  region , COUNT(id) as number_countries
FROM countries
group by region
order by number_countries desc

