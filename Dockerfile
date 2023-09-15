FROM ubuntu:20.04

LABEL maintainer "Tobias Verbeke <tobias.verbeke@openanalytics.eu>"

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Dash and dependencies
RUN pip3 install dash==2.13.0 && \
    pip3 install pandas

RUN mkdir app
COPY app/app.py /app
COPY app/gdp-life-exp-2007.csv /app

EXPOSE 8050

WORKDIR /app
CMD ["python3", "app.py"]
