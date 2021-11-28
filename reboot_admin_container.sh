#!/bin/bash
git pull
kubect  delete deploy sc-admin-deployment
docker build src/smartcity/ -t siriusadmin_web
kubectl apply -f admin-deployment.yaml