#!/bin/bash
export PROCESSED_BRANCH_NAME=$(echo ${_BRANCH_NAME} | tr '[:upper:]' '[:lower:]' | sed 's/\//-/g')
gcloud builds submit --config=clone-database.yaml --substitutions _BRANCH_NAME=$PROCESSED_BRANCH_NAME
gcloud builds submit --config=deploy-api.yaml --substitutions _BRANCH_NAME=$PROCESSED_BRANCH_NAME --branch ${_BRANCH_NAME}