docker build -t base:v2.1 -f docker/DependencyDockerfile . 
docker build -t digits:v2.1 -f docker/FinalDockerfile .
docker run -d --name Digits_models -it digits:v2.1
az acr login --name MLOpsJainan
docker tag base:v2.1 mlopsjainan.azurecr.io/base:v2.1
docker tag digits:v2.1 mlopsjainan.azurecr.io/digits:v2.1
docker push mlopsjainan.azurecr.io/base:v2.1
docker push mlopsjainan.azurecr.io/digits:v2.1
