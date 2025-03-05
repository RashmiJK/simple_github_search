# Deploying Containerized Web Apps Using Azure Container Registry and Azure App Service
In this session, we'll learn about Azure Container Registry and Azure App Service followed by deploying a simple app developed using FastAPI via the Azure Portal, and then explore deployment using GitHub Actions as a demo.

## Pre-requisites
+ Containers
+ Some ability of any programming language
+ Azure Command line
+ Some basic understanding of Continuous Deployment (to understand what is being achieved through GitHub Actions)

## Let's understand the basics
1. [Basics of containers](presentation/1-basics_of_containers.md)
2. [What is Azure Container Registry](presentation/2-basics_of_ACR.md)
3. [What is Azure App Service](presentation/3-basics_of_AP.md)
4. [Basics of Github Actions](presentation/4-basics_actions.md)
5. Demo

# Setting Up Your Workspace for This Repository
This is a simple web application developed using FastAPI to search for GitHub projects using keywords. It is designed for use in a technical demo session. The repository includes a `devcontainer.json` file to assist the Dev Container extension in quickly setting up the development environment. Refer to the [Developing inside a container](https://code.visualstudio.com/docs/devcontainers/containers) documentation to learn more. The web application is also dockerized to facilitate easy deployment in the cloud.

1. Create python virtual environment
2. python -m pip install -e .
3. fastapi dev src/app.py

### Execute

### Deploy
#### Deploy through Azure UI
#### Continuous deployment using Github Actions
