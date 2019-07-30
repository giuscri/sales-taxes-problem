.PHONY: test

test:
	pipenv run pytest --cov=sales_taxes . # https://stackoverflow.com/a/55338611/2219670
