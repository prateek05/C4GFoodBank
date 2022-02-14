list:
	@grep '^[^#[:space:]].*:' Makefile

#sets up the whole project
build: init start migrations migrate

#creates the containers and installs dependencies
init:
	docker-compose build 

#starts a detached instance of the containers
start:
	docker-compose up -d  

#lints the backend
lint:
	docker-compose restart
	docker-compose exec web autoflake --in-place --remove-unused-variable .
	docker-compose exec web isort .  
	docker-compose exec web black .  


#tests the backend
test:
	docker-compose restart
	docker-compose exec web python manage.py test

#runs the database migrations
migrate:
	docker-compose restart
	docker-compose exec web python manage.py migrate

#creates any new migrations
migrations:
	docker-compose restart
	docker-compose exec web python manage.py makemigrations

#Stops containers
stop: 
	docker-compose stop