# https://github.com/pypa/pipenv/blob/9208ec9/Dockerfile

FROM kennethreitz/pipenv

COPY . /app

CMD python3 test_sales_taxes.py
