# Azure Roles

## Overview

**NOTE:** All testing of these Azure roles was done on Ansible 2.3 installed on RHEL 7.3. The Ansible Host was located in Azure inside the Resource Group being used.

This repository contains the following Ansible roles related to managing Azure Virtual Machines:

|Role Name|Function|
|---|---|
|azure-prereqs|Used to install the required packages onto RHEL for the azure modules to function|
|azure-create-network-interface|Creates a Network Interface that can be attached to a Virtual Machine|
|azure-delete-network-interface|Deletes a Network Interface |
|azure-create-public-ip-address|Creates a public ip address that can be attached to a network interface|
|azure-delete-public-ip-address|Deletes a public ip address|
|azure-create-vm-linux|Creates a Linux VM |
|azure-create-vm-windows|Creates a Windows VM|
|azure-delete-vm|Creates a Linux VM|
|azure-create-security-group|Creates a Network Security Group the can be attached to a Network Interface|
|azure-delete-security-group|Deletes a Network Security Group
|azure-create-storage-account|Creates a Storage Account that can be attached to a Virtual Machine|
|azure-delete-storage-account|Deletes a Storage Account|
|azure-deallocate-vm|Deallocates a Virtual Machine|
|azure-restart-vm|Restarts a Virtual Machine|
|azure-start-vm|Starts a Virtual Machine|
|azure-stop-vm|Stops a Virtual Machine|

## Requirements (on host that executes modules)
These roles require the following packages to be already installed on the Ansible server.

- python 2.7.x
- ansible 2.2.x

The following required packages can be installed using the azure-prereqs role.

##### yum packages
- python-pip (Required for pip package installs)
- gcc (Prereq for cryptography package)
- libffi-devel (Prereq for cryptography package)
- python-devel (Prereq for cryptography package)
- openssl-devel (Prereq for cryptography package)
- nodejs (Required for npm package installs)
- npm (Required for npm package installs)

##### npm packages
- azure-cli (Required for command line access to Azure)

##### pip packages
- cryptography (Prereq for msrestazure package)
- azure==2.0.0rc5 (Azure SDK package)
- msrestazure (Azure msrestazure package)

##Authenticating with Azure##

Using the Azure Resource Manager modules requires authenticating with the Azure API. You can choose from two authentication strategies:

- Active Directory Username/Password
- Service Principal Credentials

All the Azure roles in this repository are configured to Service Principle Credentials.

Service Principle Authentication requires the following:

- Your Client ID, which is found in the “client id” box in the “Configure” page of your application in the Azure portal
- Your Secret key, generated when you created the application. You cannot show the key after creation. If you lost the key, you must create a new one in the “Configure” page of your application.
- And finally, a tenant ID. It’s a UUID (e.g. ABCDEFGH-1234-ABCD-1234-ABCDEFGHIJKL) pointing to the AD containing your application. You will find it in the URL from within the Azure portal, or in the “view endpoints” of any given URL.

**NOTE:** The Service Principle Account must have Contributor permissions at the subscription level not just the Resource Group level.

##Ansible Vault##

These roles have been configured and tested using Ansible Vault. The following variables have been set in Ansible Vault.

|variable|location|example|comments|
|---|---|---|---|---|
|azure_subscription_id|encrypted vault file|aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|Your Azure subscription Id.|
|azure_tenant|encrypted vault file|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|Azure tenant ID. Use when authenticating with a Service Principal.|
|azure_client_id|encrypted vault file|cccccccc-cccc-cccc-cccc-cccccccccccc|Azure client ID. Use when authenticating with a Service Principal.|
|azure_secret|encrypted vault file|dddddddddddddddddddddddddddddddddddddddddddd| Azure client secret. Use when authenticating with a Service Principal.|
|azure_admin_password|encrypted vault file| password123|Password for the admin username. |
|azure_admin_username|encrypted vault file|testadmin|Admin username used to access the host after it is created. |

## Modules used
- Ansible Packaging Module **yum**
 - Installs, upgrade, removes, and lists packages and groups with the yum package manager.
- Ansible Packaging Module **pip**
 - Manages Python library dependencies.
- Ansible Packaging Module **npm**
 - Manages node.js packages with Node Package Manager 
- Ansible Cloud Module **azure_rm_virtualmachine**
 - Create, update, stop and start a virtual machine.
- Ansible Cloud Module **azure_rm_virtualnetwork**
 - Create, update or delete a virtual networks.
- Ansible Cloud Module **azure_rm_securitygroup**
 - Create, update or delete a network security group.
- Ansible Cloud Module **azure_rm_storageaccount**
 - Create, update or delete a storage account.
- Ansible Cloud Module **azure_rm_publicipaddress**
 - Create, update or delete a storage account.

## Author Information
Original author - Brad McIntyre.

Last modified -

This is maintained by:
--------------------------

Datacom Systems (Wellington) Limited

Team: UDM Team

Contact Name: Brad McIntyre

Contact E-mail: bradm@datacom.co.nz