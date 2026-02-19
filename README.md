Деплой в Kubernetes (minikube)

- Запуск кластера: `minikube start --driver=docker`
- Сборка образа в minikube: `eval $(minikube docker-env)` + `docker build -t project-1-k8s-ci-app -f docker/Dockerfile .`
- Деплой: `kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml`
- Доступ: `minikube service project-1-service` → http://127.0.0.1:36479
- Результат: приложение отвечает "FastAPI works"
