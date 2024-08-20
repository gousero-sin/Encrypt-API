docker build -t api .
docker run -p 5000:5000 --add-host=localhost:127.0.0.1 --name api api

