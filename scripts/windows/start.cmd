docker build -t user_service_image .
docker run -dit --name user_service user_service_image
docker exec -it user_service bash