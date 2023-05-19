#!/usr/bin/env bash

for ((i=0;i<10;i++)); do
    for ((j=0;j<10;j++)); do
        if [[ "${i}" == "${j}" ]]; then
            echo "${i}, ${j}"
        fi
    done
done
