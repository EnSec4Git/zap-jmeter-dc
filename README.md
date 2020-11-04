Example DevSecOps Pipeline
===============

This repository contains an example DevSecOps pipeline for the OpenAPI PetStore example API.

The pipeline consists of 2 Docker "Compositions":
* OWASP ZAP security test + local PetStore container
* JMeter performance test + local PetStore container

After the two build steps complete, an additional Python script is started (within Docker), that summarizes the results.

Note that the CI configuration itself is stored within TeamCity and is not part of this repository (but probably should be, as well).
