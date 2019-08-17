# data_pirate_cep

The project simply builds a web crawler to get all ZIP Code ranges and locals from "Correios"s website.

# Getting Started

## Add UFs for crawling

In the file uf.json, replace the UFs abbreviation with the UFs needed for crawling.

## Install and Run

> This project was tested in Linux.

1. [Install Docker](https://docs.docker.com/install/)
2. Clone this project to your local environment.
3. Run `docker build -t data_pirate_cep .` from the top level directory for your project, to build the docker image.
4. Run `docker build -t data_pirate_cep .` to run the web crawler.

## After Running

There will be a jsonl file named "addresses" in the top level directory with all the data.