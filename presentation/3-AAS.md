# Web Hosting Options in Azure

Azure App Service offers fully managed hosting for web applications, including websites and APIs. You can deploy these applications using either **code** or **containers**, making it an ideal choice for cloud-native web solutions. Explore the available [link](https://learn.microsoft.com/en-us/azure/app-service/deploy) to learn various deployment options for cloud-native apps in Azure.

Azure offers many ways to host your application code. Here is a flowchart that helps you choose the suitable Azure service for your requirements. You can compare their features at full scale in this read.

[![Image](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/images/compute-choices.svg)](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree?toc=%2Fazure%2Fapp-service%2Ftoc.json&bc=%2Fazure%2Fapp-service%2Fbreadcrumb%2Ftoc.json)

# About Azure App Service

Azure App Service is a fully managed platform as a service (PaaS) for developers. It enables you to build and host web apps and RESTful APIs in the language stack of your choice without managing infrastructure.

## Key Features

- Supports multiple languages: .NET, Java, Node.js, Python, PHP, and custom containers.
- Provides improved security, load balancing, autoscaling, high availability, and automated management.
- Supports both Windows and Linux.
- Enables automated deployments from GitHub, Azure DevOps, or any Git repo.

## App Service Plan

With App Service, you pay for the Azure compute resources you use. The compute resources are determined by the [App Service plan](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans) that you run your apps on. When you create an App Service plan in a certain region, a set of compute resources is created for that plan in that region. Whatever apps you put into this App Service plan run on these compute resources as defined by your App Service plan.

Each App Service plan defines:
- Operating System (Windows, Linux)
- Region
- Number of VM instances
- Size of VM
- Pricing tier (Free, Shared, Basic, Standard, Premium, etc.)

## Deployment

You can directly deploy code into Azure App Service. For Python apps, this requires a `requirements.txt` file. [Reference](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python). App Service does not directly support `pyproject.toml` at the moment. This sample app uses `pyproject.toml` for setup. You can generate a compatible `requirements.txt` before deployment or deploy your app using a Docker image. This demo uses the Docker image approach.

There are several ways to deploy your app:
- Deployment Centre
- GitHub Actions
- Azure DevOps
- Containers

In this demo, we'll use the container approach. We'll build a Linux/amd64 compatible image, push it to Azure Container Registry, and deploy that image into Azure App Services. The actions are also written for the same.

## Additional Resources

- [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/)
- [Deploy and run a containerized web app with Azure App Service](https://learn.microsoft.com/en-gb/training/modules/deploy-run-container-app-service/)
