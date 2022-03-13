FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install --no-install-recommends -y\
       ca-certificates  \
       make \
	   python3 \
	   golang \
       git

RUN go get github.com/ad-freiburg/gtfs-shp-eval

RUN mkdir -p /output

COPY Makefile /
COPY README.md /
COPY fetch_ids.py /
COPY fetch_feeds.py /

WORKDIR /

RUN make help

ENTRYPOINT ["make"]
