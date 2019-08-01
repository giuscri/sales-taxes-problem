# https://github.com/pypa/pipenv/blob/9208ec9/Dockerfile

FROM kennethreitz/pipenv
RUN apt install -y afl
RUN pipenv install --deploy --system
COPY . /app
