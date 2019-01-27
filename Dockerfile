FROM ubuntu:18.04

MAINTAINER Tobias Verbeke "tobias.verbeke@openanalytics.eu"

RUN apt-get update && apt-get install -y python python-pip

# Dash and dependencies
RUN pip install dash==0.36.0  # The core dash backend
RUN pip install dash-renderer==0.17.0  # The dash front-end
RUN pip install dash-html-components==0.13.5  # HTML components
RUN pip install dash-core-components==0.43.0  # Supercharged components
RUN pip install plotly --upgrade  # Plotly graphing library used in examples

# app dependencies
RUN pip install pandas

RUN mkdir app
COPY app/app.py /app

EXPOSE 8050

WORKDIR /app
CMD ["python", "app.py"]
