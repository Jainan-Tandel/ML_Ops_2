docker build -t digits:v1.1 -f docker/Dockerfile . 
docker volume create digit_volume
docker run -d --name Digits_models -v digit_volume:/digits/models digits:v1.1
