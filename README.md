# Azure Roles

## Overview

This repository contains the following Ansible roles related to managing Azure Virtual Machines:

|Role Name|Function|
|---|---|
|azure-prereqs|Used to install the required packages onto RHEL for the azure modules to function|
|azure-create-network-interface|Creates a Network Interface that can be attached to a Virtual Machine|
|azure-delete-network-interface|Deletes a Network Interface |
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
These roles require the following packages to be already installed on Ansible server.

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

## Available Roles



## Author Information
Original author - Brad McIntyre.

Last modified -

This is maintained by:
--------------------------

Datacom Systems (Wellington) Limited

Team: UDM Team

Contact Name: Brad McIntyre

Contact E-mail: bradm@datacom.co.nz