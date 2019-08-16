# data_pirate_cep

The project simply builds a web crawler to get all ZIP Code ranges and locals from "Correios"s website.

# Getting Started

## Add UFs for crawling

In the file uf.json, replace the UFs abbreviation with the UFs needed for crawling.

## Install and Run

> This project was tested in Windows ONLY.

1. [Install Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
2. Clone this project to your local environment.
3. Run `docker-compose up` from the top level directory for your project.

## After Running

> There will be a jsonl file named "addresses" in the project diretory with all the data.

This `docker-compose up` command will start a `crawler` service and run the crawler for the specified UFs.ervice and run the crawler for the specified UFs.