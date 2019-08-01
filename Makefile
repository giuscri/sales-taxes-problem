.PHONY: test

test: docker-build-image
	sudo docker run --rm sales-taxes make pytest

fuzz: docker-build-image
	sudo docker run --rm -it sales-taxes py-afl-fuzz -o afl/output/ -i afl/input/ -- python3 sales_taxes.py

docker-build-image:
	sudo docker image build -t sales-taxes -f Dockerfile .

pytest:
	pytest --cov=sales_taxes . # https://stackoverflow.com/a/55338611/2219670

pipenv-pytest:
	pipenv run make pytest
