FROM kennethreitz/pipenv

COPY . /app

CMD python3 test_sales_taxes.py
