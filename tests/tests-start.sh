#!/usr/bin/env bash

set -e
set -x
while getopts uif: flag
do
    case "${flag}" in
        u) test_folder="unit/";;
        i) test_folder="integration/";;
        f) test_folder=${OPTARG};;
    esac
done
pytest --cov=src --cov-report term-missing tests/${test_folder}