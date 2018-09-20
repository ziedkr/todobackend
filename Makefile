#
PROJECT_NAME ?= todobackend
# to tag the docker rease avec le nom de l'org
ORG_NAME ?= ooredoo
# to tag the docker reposdotie rease avec le nom de l'org
REPO_NAME ?= todobackend

# variaee pour la localisation des fichier 
DEV_COMPOSE_FILE := docker/dev/docker-compose.yml
REL_COMPOSE_FILE := docker/release/docker-compose.yml

#les docker commpose porject nmanme et le build_uid poour jenkis lors du tad
REL_PROJECT := $(PROJECT_NAME)$(BUILD_ID)
DEV_PROJECT := $(REL_PROJECT)dev


.PHONY: testx buildx releasex test build release clean # phony will check for binary file to avoud the repetition of a file name

testx:
	echo "Hello zied"
	echo "from make"

buildx:
	echo "Hello zied from buildx"
	

releasex:
	echo "Hello zied from eleasex"



test:
	docker-compose   -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) build 
	docker-compose   -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE)  up agent 
	docker-compose   -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE)  up test 

build:
	docker-compose -f $(DEV_COMPOSE_FILE) up builder

release:
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) build 
	docker-compose -p $(REL_PROJECT)  -f $(REL_COMPOSE_FILE) up agent
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) run --rm app manage.py collectstatic --noinput # bootstrap l'env
	docker-compose -p $(REL_PROJECT)  -f $(REL_COMPOSE_FILE) run --rm app manage.py migrate --noinput  # migree le shema 
	docker-compose  -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) up test 


clean:
	docker-compose  -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) kill
	docker-compose  -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE)  rm -f 
	docker-compose  -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) kill
	docker-compose  -p $(REL_PROJECT)  -f $(REL_COMPOSE_FILE) rm -f  




	#
	#