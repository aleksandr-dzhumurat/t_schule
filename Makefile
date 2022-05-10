CURRENT_DIR = $(shell pwd)
USER_NAME = $(shell whoami)
USER_ID = $(shell id -u)
USER_GROUP = $(shell id -g)

build:
	docker build \
		--build-arg USER_ID="${USER_ID}" \
		--build-arg GROUP_ID="${GROUP_ID})" \
		-f ${CURRENT_DIR}/Dockerfile \
		-t ml_service:latest \
		${CURRENT_DIR}

clear:
	docker rm -f ml_app || true

train: clear
	docker run \
	    -it --rm \
		-v "${CURRENT_DIR}/src:/srv/src" \
		-v "${CURRENT_DIR}/data:/srv/data" \
		ml_service:latest \
		"python3.8" src/run.py

run-flask:
	docker run \
	    -it --rm \
	    -d \
		-v "${CURRENT_DIR}/src:/srv/src" \
		-v "${CURRENT_DIR}/data:/srv/data" \
		-p 5001:5000 \
		--name ml_app \
		ml_service:latest \
		"python3.8" src/app.py

test-api:
	docker exec \
	    -it \
		ml_app \
		"python3.8" \
		-c "import requests; print(requests.get('http://0.0.0.0:5000/api/feature_extractor?doc_id=1').json())"
