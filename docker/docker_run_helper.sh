docker build -t digitsdeps:v1.1 -f docker/DependencyDockerfile . 
docker build -t digitsfinal:v1.1 -f docker/FinalDockerfile .
docker run -d --name Digits_models -it digitsfinal:v1.1
