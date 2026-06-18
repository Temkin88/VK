#!/bin/bash

p='SANDBOX'
s='u.myteaminternal'
v=''
l='INFO'

while getopts p:s:v:l: flag

do
    case "${flag}" in
        p) p=${OPTARG};;
        s) s=${OPTARG};;
        v) v=${OPTARG};;
        l) l=${OPTARG};;
        *)
    esac
done

if [[ -z "${VAR}" ]];
then
  echo "API Version was not passed, trying to get from myteam-config.json"
  v=$(curl "http://$s/myteam-config.json" | jq -r '."api-version"')
  echo "API Version: ${v}"
fi;


echo "Старт в несколько потоков"
allurectl watch -- python -m pytest -n 12 -m $p --sandbox $s --api $v --log-cli-level=$l --dist loadgroup || true
failed_count="1"

if ! [ -f "./.pytest_cache/v/cache/lastfailed" ]
then
	failed_count=$(cat ./.pytest_cache/v/cache/lastfailed | wc -l)
fi

if [ "$failed_count" != "1" ]
then
	echo "Запуск упавших тестов"
	allurectl watch -- python -m pytest --lf -m $p --sandbox $s --api $v --log-cli-level=$l --dist loadgroup || true
else
	echo "Тесты успешны"
fi
