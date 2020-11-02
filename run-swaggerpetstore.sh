#!/bin/sh
docker run -d -e SWAGGER_HOST=http://petstore.swagger.io \
  -e SWAGGER_URL=http://localhost:8080 \
  -e SWAGGER_BASE_PATH=//v2 -p 8080:8080 swaggerapi/petstore