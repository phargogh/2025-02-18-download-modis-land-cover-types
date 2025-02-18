#!/usr/bin/env sh

# mamba install python=3.12 lxml beautifulsoup4 yq

wget https://opendap.cr.usgs.gov/opendap/hyrax/MCD12Q1.061/catalog.xml

python extract-links.py catalog.xml
