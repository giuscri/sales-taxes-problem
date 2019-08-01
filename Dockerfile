# https://github.com/pypa/pipenv/blob/9208ec9/Dockerfile

FROM kennethreitz/pipenv
COPY . /app
RUN apt install -y afl
RUN pipenv install --deploy --system
CMD python3 test_sales_taxes.py
