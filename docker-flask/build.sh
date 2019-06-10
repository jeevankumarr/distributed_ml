#!/usr/bin/env bash

echo 'Building Docker Image'
docker build -t docker-flask:latest .
echo 'Build Complete'

if [ $1 == 'deploy' ]; then
    echo 'Deploying Image and Starting Service'
    kubectl delete deployments,pod,service flask-dep
    kubectl create -f docker-flask-deployment.yml
    kubectl expose deployment flask-dep --type=NodePort --port 5000
    KUBE_IP=`minikube ip`
    KUBE_PORT=`kubectl get services/flask-dep -o go-template='{{(index .spec.ports 0).nodePort}}'`
    echo 'Go to http://'$KUBE_IP:$KUBE_PORT
fi
