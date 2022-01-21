#!/bin/bash

echo "start minikube "
#minikube start

# mysql
echo "Creating the volumes and mysql deployment and service..."
#docker pull mysql
kubectl apply -f mysql_pv.yaml
kubectl apply -f mysql_pv_claim.yaml
kubectl apply -f secrets.yaml
# kubectl apply -f mysql_deployment.yaml
# kubectl apply -f mysql_service.yaml
kubectl create -f mysql_deployment.yaml
kubectl create -f mysql_service.yaml


# init py
echo "Creating init py deployment and service..."
kubectl create  -f init_py_deployment.yaml 
kubectl create  -f init_py_service.yaml 

# web py
echo "Creating the web py deployment and service..."
kubectl create  -f web_py_deployment.yaml 
kubectl create  -f web_py_service.yaml 


# frontend
echo "Creating the frontend deployment and service..."
# kubectl apply -f frontend_deployment.yaml
# kubectl apply -f frontend_service.yaml
kubectl create  -f frontend_deployment.yaml
kubectl create  -f frontend_service.yaml

# multi stage
echo "Creating the multi stage go deployment and service..."
# kubectl apply -f multi_stage_deployment.yaml
# kubectl apply -f multi_stage_service.yaml
kubectl create  -f multi_stage_deployment.yaml
kubectl create  -f multi_stage_service.yaml

# ingress
echo "Adding the ingress..."
minikube addons enable ingress
echo "delete something."

kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
echo "sedaj pa res Adding the ingress..."

kubectl apply -f ingress.yaml

echo "if you want to go to dashboard go to new terminal and run"
echo "minikube dashboard"

