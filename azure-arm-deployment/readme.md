# Azure ARM template Deployment

This role is still a work in progress


## Overview

Deploys a ARM template on the Azure platform

## Requirements (on host that executes modules)
This role requires the following packages to be already installed on Ansible server.

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


## Module used
- Ansible Cloud Module **azure_rm_deployment**
 - Create or destroy Azure Resource Manager template deployments via the Azure SDK for Python.


## Available 'azure_rm_deployment' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|ad_user|no| |<ul>|Active Directory username. Use when authenticating with an Active Directory user rather than service principal.|
|client_id|no|||Azure client ID. Use when authenticating with a Service Principal.|
|deployment_mode|no|incremental|<ul><li>complete</li><li>incremental</li><ul>|In incremental mode, resources are deployed without deleting existing resources that are not included in the template. In complete mode resources are deployed and existing resources in the resource group not included in the template are deleted.|
|deployment_name|no|ansible-arm||The name of the deployment to be tracked in the resource group deployment history. Re-using a deployment name will overwrite the previous value in the resource group's deployment history.|
|location|no|||Valid Azure location. Defaults to location of the resource group.|
|parameters|no||| A hash of all the required template variables for the deployment template. This parameter is mutually exclusive with 'parameters_link'. Either one of them is required if "state" parameter is "present". |
|parameters_link|no|||Uri of file containing the parameters body. This parameter is mutually exclusive with 'parameters'. Either one of them is required if "state" parameter is "present".|
|password|no|||Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.|
|profile|no|||Security profile found in ~/.azure/credentials file.|
|resource_group_name|no|||The resource group name to use or create to host the deployed template|
|secret|no||| Azure client secret. Use when authenticating with a Service Principal.|
|state|no|present|<ul><li>present</li><li>absent</li></li>|Use with state 'present' to start the machine. Set to false to have the machine be 'stopped'.|
|state|no|Present|<ul><li>Absent</li><li>Present</li></li>|If state is "present", template will be created. If state is "present" and if deployment exists, it will be updated. If state is "absent", stack will be removed.|
|subscription_id|no|||Your Azure subscription Id.|
|template|no|||A hash containing the templates inline. This parameter is mutually exclusive with 'template_link'. Either one of them is required if "state" parameter is "present".|
|template_link|no|||Uri of file containing the template body. This parameter is mutually exclusive with 'template'. Either one of them is required if "state" parameter is "present".|
|tenant|no|||Azure tenant ID. Use when authenticating with a Service Principal.|
|wait_for_deployment_completion|no|true|<ul><li>yes</li><li>no</li><ul>| Whether or not to block until the deployment has completed.|
|wait_for_deployment_polling_period|10||| Time (in seconds) to wait between polls when waiting for deployment completion. |

## Role Variables
|variable|location|example|comments|
|---|---|---|---|---|
|azure_subscription_id|encrypted vault file|aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|Your Azure subscription Id.|
|azure_tenant|encrypted vault file|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|Azure tenant ID. Use when authenticating with a Service Principal.|
|azure_client_id|encrypted vault file|cccccccc-cccc-cccc-cccc-cccccccccccc|Azure client ID. Use when authenticating with a Service Principal.|
|azure_secret|encrypted vault file|dddddddddddddddddddddddddddddddddddddddddddd| Azure client secret. Use when authenticating with a Service Principal.|
|azure_admin_password|encrypted vault file| password123|Password for the admin username. |
|azure_admin_username|encrypted vault file|testadmin|Admin username used to access the host after it is created. |
|azure_vm_name|vars|testvm1|Name or list of names for the VMs|
|azure_resource_group|vars|Test_Env_1|Name of the resource group containing the virtual machine.|
|azure_location|vars|vars|australiasoutheast|Azure location|
|azure_template_link|vars|'https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-vm-winrm-windows/azuredeploy.json'|URL link to template json file|
|wait_for_deployment_completion|vars|yes|Whether or not to block until the deployment has completed.|
|wait_for_deployment_polling_period|vars|10| Time (in seconds) to wait between polls when waiting for deployment completion.|

## Examples

~~~
---
# This test playbook will deploy an ARM template

- name: Test playbook for azure-create-vm
  hosts: localhost
  connection: local
  gather_facts: false
  user: ansible
  become: yes

  vars_files:
    - /home/ansible/vault.yml

  vars:
    azure_vm_name: testvm2
    azure_storage_account_name: testvm201
    azure_network_interface_name: testvm2-nic1
    azure_vm_size: Standard_D1
    azure_windows_os_version: 2012-R2-Datacenter
    azure_resource_group: Test_Env_1
    azure_virtual_network_name: Test_Env_1-vnet
    azure_public_ip_name: testvm201
    azure_vm_size: Standard_D1
    azure_template_link: 'https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-vm-winrm-windows/azuredeploy.json'
    azure_location: australiasoutheast


  roles:
    - azure-arm-deployment

~~~

## License
Proprietary or whatever license from source OSS role this role is based upon.

## Author Information
Original author - Brad McIntyre.

Last modified -

This role is maintained by:
--------------------------

Datacom Systems (Wellington) Limited

Team: UDM Team

Contact Name: Brad McIntyre

Contact E-mail: bradm@datacom.co.nz
