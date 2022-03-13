# Setup for GTFS shape quality survey

This evaluates the shape quality of *all* the latest GTFS feeds on [transitfeeds.com](https://transitfeeds.com/), for each year between 2015 and 2020.

Feeds will be downloaded an given to [gtfs-shp-eval](https://github.com/ad-freiburg/gtfs-shp-eval) for evaluation.

This requires an a transitfeeds.com [API-key](https://transitfeeds.com/api/keys).

## Requirements

 * python3
 * [gtfs-shp-eval](https://github.com/ad-freiburg/gtfs-shp-eval)

## Usage

    $ make API_KEY=<YOUR_TRANSITFEEDS_API_KEY> eval

Results will be printed to stdout and written to `*.res` files.

## Via Docker

    $ docker build -t shp-eval .
    $ docker run -t shp-eval API_KEY=<YOUR_TRANSITFEEDS_API_KEY> eval
