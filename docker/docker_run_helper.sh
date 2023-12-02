docker build -t digitsDeps:v1.1 -f docker/DependencyDockerfile . 
docker build -t digitsFinal:v1.1 -f docker/FinalDockerfile .
docker run -d --name Digits_models -v $(pwd)/models:/digits/models digitsFinal:v1.1 -it
