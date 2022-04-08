CURRENT_DIR = $(shell pwd)
USER_NAME = $(shell whoami)
USER_ID = $(shell id -u)
USER_GROUP = $(shell id -g)

pun_pipeline: loload_data_from_kafka prepare_wide_dataset prepare_ocr_dataset
	echo "Pipline running..."

build:
	docker build \
		--build-arg USER_ID="${USER_ID}" \
		--build-arg GROUP_ID="${GROUP_ID})" \
		-f ${CURRENT_DIR}/Dockerfile \
		-t ml_service:latest \
		${CURRENT_DIR}

train:
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
		ml_service:latest \
		"python3.8" src/app.py
