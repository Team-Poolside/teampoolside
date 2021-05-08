FROM continuumio/miniconda3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install -y \
    gcc \
    lsb-release \
    gnupg2 \
    netcat

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

RUN apt-get update && apt-get install -y \
    postgresql \
    && apt-get clean all

COPY environment.yml .
RUN conda env create -f environment.yml

COPY . .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]