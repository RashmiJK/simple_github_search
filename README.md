# Deploying Containerized Web Apps Using Azure Container Registry and Azure App Service
In this session, we'll learn about Azure Container Registry and Azure App Service followed by deploying a simple app developed using FastAPI via the Azure Portal, and then explore deployment using GitHub Actions as a demo.

## Pre-requisites
+ Knowledge of containerization concepts and technologies, such as Docker
+ Some ability of any programming language
+ Familiarity with Azure portal or Azure CLI for managing Azure resources.
+ Some basic understanding of Continuous Deployment (to understand what is being achieved through GitHub Actions)

## Let's understand the basics
1. [Basics of containers](presentation/1-containers.md)
2. Undertanding of git
3. [What is Azure Container Registry](presentation/2-ACR.md)
4. [What is Azure App Service](presentation/3-AAS.md)
5. [Basics of Github Actions](presentation/4-actions.md)

# Setting Up Your Workspace for This Repository
This is a simple web application developed using FastAPI to search for GitHub projects using keywords. It is designed for use in a technical demo session. The repository includes a `devcontainer.json` file to assist the Dev Container extension in quickly setting up the development environment. Refer to the [Developing inside a container](https://code.visualstudio.com/docs/devcontainers/containers) documentation to learn more. The web application is also dockerized to facilitate easy deployment in the cloud. Code is linted with [ruff](https://github.com/astral-sh/ruff) and formatted with [black](https://black.readthedocs.io/en/stable/). Project configurations are set up using [pyproject.toml](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

1. The developemnt environment will be automatically setup for you when you open the project in VS Code with [DevContainer extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) to

2. Setup locally <br>
    a. [Create python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) <br>

    b. [setuptools](https://github.com/pypa/setuptools) allows you to install a package without copying any files to your interpreter directory (e.g. the site-packages directory). This allows you to modify your source code and have the changes take effect without you having to rebuild and reinstall.
    To do that, execute the below command (include the dot in the command; it means current directory)
    ```shell
    python -m pip install -e .
    ```
    <br>
    c. Install the pre-commit hooks. Refer .pre-commit-config file and it's [documentation](https://pre-commit.com/#intro) for better undertsanding on this.
    ```shell
    pre-commit install
    ```
3. Run the web server locally
    ```shell
    fastapi dev src/app.py
    ```
    Open 'http://127.0.0.1:8000' in the browser tab and see the web app responding. This app requires github token to be supplied within in the .env file locally.
    Eg: 'GITHUB_TOKEN=<your token>'

# Deploy through Azure UI
1. Containerize your web app using 'docker build' command
2. Push the conatiner to Azure Container registry
3. Create an instance of Azure App Services and deploy your app

### Setup Continuous deployment using Github Actions
