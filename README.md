Деплой в Kubernetes (minikube)

- Запуск кластера: `minikube start --driver=docker`
- Сборка образа в minikube: `eval $(minikube docker-env)` + `docker build -t project-1-k8s-ci-app -f docker/Dockerfile .`
- Деплой: `kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml`
- Доступ: `minikube service project-1-service` → http://127.0.0.1:36479
- Результат: приложение отвечает "FastAPI works"


## День 5: Продвинутый Kubernetes

- ConfigMap: APP_ENV, LOG_LEVEL и т.д.
- Secret: DB_PASSWORD
- Liveness / Readiness probes (tcpSocket на порт 8000)
- Rolling update: изменение APP_VERSION → плавное обновление без даунтайма
- Rollback: `kubectl rollout undo` → мгновенный откат к предыдущей версии

Демонстрация:
kubectl rollout status deployment/project-1-app
kubectl get pods -w (наблюдение за подами)
