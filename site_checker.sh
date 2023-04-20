#!/bin/bash

# Define o comando a ser executado pelo cronjob
COMMAND="/home/lavino/.pyenv/shims/python /mnt/c/Users/Lavin/Documents/indicium/Desafio_modulo_II/__main__.py -f data/urls.csv"

# Adiciona o comando ao cronjob para ser executado diariamente à meia-noite
crontab -r

(crontab -l 2>/dev/null; echo "0 0 * * * $COMMAND") | crontab -

/home/lavino/.pyenv/shims/python /mnt/c/Users/Lavin/Documents/indicium/Desafio_modulo_II/__main__.py -f data/urls.csv

