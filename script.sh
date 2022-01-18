# init py
kubectl apply -f init_py_deployment.yaml 
kubectl apply -f init_py_service.yaml 

# web py
kubectl apply -f web_py_deployment.yaml 
kubectl apply -f web_py_service.yaml 

# mysql
kubectl apply -f mysql_pv.yaml
kubectl apply -f mysql_pv_claim.yaml
kubectl apply -f secrets.yaml
kubectl apply -f mysql_deployment.yaml
kubectl apply -f mysql_service.yaml
# kubectl create -f mysql_deployment.yaml
# kubectl create -f mysql_service.yaml

# frontend
kubectl apply -f frontend_deployment.yaml
kubectl apply -f frontend_service.yaml

# multi stage
kubectl apply -f multi_stage_deployment.yaml
kubectl apply -f multi_stage_service.yaml

# ingress
kubectl apply -f ingress.yaml

