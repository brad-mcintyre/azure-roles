# Create Azure Storage Account

## Overview

Creates a Storage Account on the Azure platform

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
- Ansible Cloud Module **azure_rm_storageaccount**
 - Create, update or delete a storage account.


## Available 'azure_rm_storeageaccount' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|account_type|no||<ul><li>Premium_LRS</li><li>Standard_GRS</li><li>Standard_LRS</li><li>Standard_RAGRS</li><li>Standard_ZRS</li><ul>| Type of storage account. Required when creating a storage account. NOTE: Standard_ZRS and Premium_LRS accounts cannot be changed to other account types, and other account types cannot be changed to Standard_ZRS or Premium_LRS.|
|ad_user|no| |<ul>|Active Directory username. Use when authenticating with an Active Directory user rather than service principal.|
|append_tags|no|true|| Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata. 
|client_id|no|||Azure client ID. Use when authenticating with a Service Principal.|
|custom_domain|no||| User domain assigned to the storage account. Must be a dictionary with 'name' and 'use_sub_domain' keys where 'name' is the CNAME source. Only one custom domain is supported per storage account at this time. To clear the existing custom domain, use an empty string for the custom domain name property. Can be added to an existing storage account. Will be ignored during storage account creation.|
|kind|no|Storage|<ul><li>Storage</li><li>StorageBlob</li><ul>|The 'kind' of storage.|
|location|no|||Valid Azure location. Defaults to location of the resource group.|
|name|yes|||Name of the storage account to update or create.|
|password|no|||Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.|
|profile|no|||Security profile found in ~/.azure/credentials file.|
|resource_group|yes|||Name of the resource group containing the virtual machine.|
|secret|no||| Azure client secret. Use when authenticating with a Service Principal.|
|state|no|Present|<ul><li>Absent</li><li>Present</li></li>|AAssert the state of the virtual machine.State 'present' will check that the machine exists with the requested configuration. If the configuration of the existing machine does not match, the machine will be updated. Use options started, allocated and restarted to change the machine's power state. State 'absent' will remove the virtual machine.|
|subscription_id|no|||Your Azure subscription Id.|
|tags|no|||Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false. |
|tenant|no|||Azure tenant ID. Use when authenticating with a Service Principal.|

## Role Variables
|variable|location|example|comments|
|---|---|---|---|---|
|azure_subscription_id|encrypted vault file|aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|Your Azure subscription Id.|
|azure_tenant|encrypted vault file|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|Azure tenant ID. Use when authenticating with a Service Principal.|
|azure_client_id|encrypted vault file|cccccccc-cccc-cccc-cccc-cccccccccccc|Azure client ID. Use when authenticating with a Service Principal.|
|azure_secret|encrypted vault file|dddddddddddddddddddddddddddddddddddddddddddd| Azure client secret. Use when authenticating with a Service Principal.|
|azure_vm_name|vars|testvm1|Name or list of names for the VMs|
|azure_resource_group|vars|Test_Env_1|Name of the resource group containing the virtual machine.|
|azure_virtual_network_name|vars|Test_Env_1-vnet|Name of the Virtual Network to build the VM in|
|azure_storage_account_type|vars|<ul><li>Standard_GRS</li><li>Standard_LRS (default)</li><li>Standard_RAGRS</li><li>Standard_ZRS</li><li>Premium_LRS</li><ul>| Type of Storage|
|azure_storage_account_kind|vars|<ul><li>Storage (default)</li><li>StorageBlob</li><ul>|Kind of Storage|
|azure_storage_account_name|vars|testvm101|Name of the Storage Account|


## Examples

~~~
---
# This test playbook will create a storage account
- name: Test playbook for azure-create-storage-account
  hosts: localhost
  connection: local
  gather_facts: false
  user: ansible
  become: yes

  vars_files:
    - /home/ansible/vault.yml

  vars:
    azure_resource_group: Test_Env_1
    azure_storage_account_type: Standard_LRS
    azure_storage_account_kind: Storage
    azure_vm_name:
      - name: win2008testvm1
        azure_storage_account_name: win2008testvm101

  roles:
    - azure-create-storage-account
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
