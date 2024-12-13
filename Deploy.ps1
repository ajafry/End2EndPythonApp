$RG_NAME = '<name of the target resource group>'
$LOCATION = 'deployment region'
$ACA_ENVIRONMENT_NAME = '<Name of the ACA environment>'
$ACR_NAME = '<registry name only>'
$ACR_REGISTRY_SERVER = "$ACR_NAME.azurecr.io"

$CONTAINER_APP_NAME = 'app-ui'
# The Set-Location command is used to change the current directory to the relevant folder so that the correct Dockerfile can be picked up
Set-Location '<path to the app-ui folder>'
az containerapp up --name $CONTAINER_APP_NAME --resource-group $RG_NAME --location $LOCATION --registry-server $ACR_REGISTRY_SERVER --environment $ACA_ENVIRONMENT_NAME --source .
Set-Location '..'

$CONTAINER_APP_NAME = 'subtract-api'
Set-Location -Path '.\SubtractMicroservice'
az containerapp up --name $CONTAINER_APP_NAME --resource-group $RG_NAME --location $LOCATION --registry-server $ACR_REGISTRY_SERVER --ingress external --target-port 80 --environment $ACA_ENVIRONMENT_NAME --source .
Set-Location -Path -

$CONTAINER_APP_NAME = 'multiply-api'
Set-Location -Path '.\MultiplyMicroservice'
az containerapp up --name $CONTAINER_APP_NAME --resource-group $RG_NAME --location $LOCATION --registry-server $ACR_REGISTRY_SERVER --ingress external --target-port 80 --environment $ACA_ENVIRONMENT_NAME --source .
Set-Location -Path -

$CONTAINER_APP_NAME = 'add-api'
Set-Location -Path '.\AddMicroservice'
az containerapp up --name $CONTAINER_APP_NAME --resource-group $RG_NAME --location $LOCATION --registry-server $ACR_REGISTRY_SERVER --ingress external --target-port 80 --environment $ACA_ENVIRONMENT_NAME --source .
Set-Location -Path -