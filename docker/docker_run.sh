docker build -t digits:v1.1 -f docker/Dockerfile . 
docker run -d --name Digits_models -v $(pwd)/models:/digits/models digits:v1.1 -it
