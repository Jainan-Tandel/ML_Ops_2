docker build -t base:v2.1 -f docker/DependencyDockerfile . 
docker build -t digits:v2.1 -f docker/FinalDockerfile .
docker run -d --name Digits_models -it digits:v2.1
