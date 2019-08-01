.PHONY: test fuzz docker-build-image pytest pipenv-pytest

run: docker-build-image
	@echo -e "** Running sales_taxes in a container"
	@echo -e '** Type items purchased, one per line, as "1 book at 12.45"'
	@echo -e "** When you're done press [ctrl-d]"

	@sudo docker run --rm -i sales-taxes python3 sales_taxes.py

test: docker-build-image
	@sudo docker run --rm sales-taxes make pytest

fuzz: docker-build-image
	@sudo docker run --rm -it sales-taxes py-afl-fuzz -o afl/output/ -i afl/input/ -- python3 sales_taxes.py

docker-build-image:
	@sudo docker image build -t sales-taxes -f Dockerfile .

pytest:
	@pytest --cov=sales_taxes . # https://stackoverflow.com/a/55338611/2219670
