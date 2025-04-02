# Github Actions
GitHub Actions is a suite of features in GitHub to automate your software development workflows right in your code repository and collaborate on pull requests and issues.

Workflow

Action

[Github Docs](https://docs.github.com/en/actions)

# Setup workflow to automate web app deployment

[cd.yaml](../../.github/workflows/cd.yaml) creates a workflow in Github repo that perform the following actions.
* Build an image from a Dockerfile
* Push the image to an Azure container registry
* Deploy the container image to Azure App service

1. Provision the Azure Container Registry (ACR) and Azure App Service (AAP) instances on Azure. For this, reuse the existing resource group and previously provisioned instances.

2. In the GitHub workflow, Azure credentials are required to authenticate with the Azure CLI. There are several ways to authenticate to Azure from GitHub. Refer to the [Azure documentation](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure) for more details. For this demo, a service principal with the Contributor role will be created and scoped to the resource group for your container registry. This service principal will allow the workflow to perform the necessary actions securely.

    * Substitute the name of your group in the following az group show command to retrive the groupId.

    Log in to Azure using cli.
    ```shell
    az login
    ```
    List resource groups using the below command.
    ```shell
    az group list
    ```
    Retrieve groupId using the below command.
    ```shell
    az group show --name <resource-group-name> --query id --output tsv

    e.g: % az group show --name sgsrg --query id --output tsv
        /subscriptions/xxxxxxxx-b644-455f-xxxx-3eb394xxxxxx/resourceGroups/sgsrg
    ```

    * Create a service principal using the below command with contributor role scoped to the resource group.
    ```shell
        az ad sp create-for-rbac --scope groupId --role Contributor --sdk-auth
    ```
    Save the JSON output because this need to be saved as secret credential in repository settings. Also, take note of the clientId, which you need to update the service principal in the next section.

    * Update the Azure service principal credentials to allow push and pull access to your container registry. This step enables the GitHub workflow to use the service principal to authenticate with your container registry and to push and pull a Docker image.

    Get the resourceId of your container registry by running the below command. Substitute the name of your container registry in the following az acr show command.
    ```shell
    az acr show --name <container-registry-name> --resource-group <resource-group-name> --query id --output tsv
    ```

    Use az role assignment create to assign the AcrPush role, which gives push and pull access to the registry. Substitute the clientId of your service principal.

    ```shell
    az role assignment create --assignee <clientId> --scope <resourceId> --role AcrPush
    ```

    * In the GitHub UI, navigate to your repository and select Security > Secrets and variables > Actions. Select New repository secret to add the following secrets.

    | Secret              | Value                                                                 |
    |---------------------|-----------------------------------------------------------------------|
    | AZURE_CREDENTIALS   | The entire JSON output from the service principal creation step      |
    | REGISTRY_LOGIN_SERVER | The login server name of your registry (all lowercase). Example: myregistry.azurecr.io |
    | REGISTRY_USERNAME   | The clientId from the JSON output from the service principal creation |
    | REGISTRY_PASSWORD   | The clientSecret from the JSON output from the service principal creation |
    | RESOURCE_GROUP      | The name of the resource group you used to scope the service principal |

    * These secret credentials are accessed in [cd.yaml](../../.github/workflows/cd.yaml) workflow.


## References
1. [Configure a GitHub Action to create a container instance](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-github-action)
2. [Deploy to Azure App Service by using GitHub Actions](https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions?tabs=userlevel%2Cpython%2Caspnetcore)
3. https://www.youtube.com/watch?v=JFSl_D3TKrU
