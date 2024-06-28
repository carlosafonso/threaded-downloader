.PHONY: build-client build-server push-client push-server all

build-client:
	docker build -t carlosafonso/egress-benchmark-client:latest client/

build-server:
	docker build -t carlosafonso/egress-benchmark-server:latest nginx/

push-client:
	docker push carlosafonso/egress-benchmark-client:latest

push-server:
	docker push carlosafonso/egress-benchmark-server:latest

all: push-client push-server
