#!/bin/bash

docker run -d -p 3000:5000 contador-backend
docker run -d -p 5000:5000 contador-backend
docker run -d -p 5030:5000 contador-backend

