.PHONY: test

test: docker-build-image
	sudo docker run --rm sales-taxes make pytest

pytest:
	pytest --cov=sales_taxes . # https://stackoverflow.com/a/55338611/2219670

docker-build-image:
	sudo docker image build -t sales-taxes -f Dockerfile .

pipenv-pytest:
	pipenv run make pytest
