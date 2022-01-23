# ingress
echo "Adding the ingress..."
minikube addons enable ingress

kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
kubectl apply -f ingress.yaml