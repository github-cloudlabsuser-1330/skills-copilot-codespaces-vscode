# Define variables
$resourceGroupName = "myResourceGroup"
$location = "EastUS"
$vmName = "myVM"
$adminUsername = "azureuser"
$adminPassword = "P@ssw0rd1234!"

# Create a resource group
az group create --name $resourceGroupName --location $location

# Create a virtual network
az network vnet create --resource-group $resourceGroupName --name myVnet --subnet-name mySubnet

# Create a public IP address
az network public-ip create --resource-group $resourceGroupName --name myPublicIP

# Create a network security group
az network nsg create --resource-group $resourceGroupName --name myNetworkSecurityGroup

# Create a virtual network card and associate with public IP address and NSG
az network nic create --resource-group $resourceGroupName --name myNic --vnet-name myVnet --subnet mySubnet --network-security-group myNetworkSecurityGroup --public-ip-address myPublicIP

# Create a virtual machine
az vm create --resource-group $resourceGroupName --name $vmName --nics myNic --image UbuntuLTS --admin-username $adminUsername --admin-password $adminPassword

# Open port 22 to allow SSH traffic to host
az vm open-port --port 22 --resource-group $resourceGroupName --name $vmName