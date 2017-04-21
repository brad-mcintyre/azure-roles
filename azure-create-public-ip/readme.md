# Create Azure Network Interface

## Overview

Creates a Network Interface on the Azure platform

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
- Ansible Cloud Module **azure_rm_virtualnetwork**
 - Create, update or delete a virtual networks.


## Available 'azure_rm_virtualnetwork' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|ad_user|no| |<ul>|Active Directory username. Use when authenticating with an Active Directory user rather than service principal.|
|address_prefixes_cidr|no| ||List of IPv4 address ranges where each is formatted using CIDR notation. Required when creating a new virtual network or using purge_address_prefixes.|
|append_tags|no|True||Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata.|
|client_id|no|||Azure client ID. Use when authenticating with a Service Principal.|
|dns_servers|no|||Custom list of DNS servers. Maximum length of two. The first server in the list will be treated as the Primary server. This is an explicit list. Existing DNS servers will be replaced with the specified list. Use the purge_dns_servers option to remove all custom DNS servers and revert to default Azure servers.|
|location|no|||Valid Azure location. Defaults to location of the resource group.|
|name|yes|||name of the virtual network.|
|password|no|||Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.|
|profile|no|||Security profile found in ~/.azure/credentials file.|
|purge_address_prefixes|no|||Use with state present to remove any existing address_prefixes.|
|purge_dns_servers|no|||Use with state present to remove existing DNS servers, reverting to default Azure servers. Mutually exclusive with dns_servers.|
|resource_group|yes|||Name of the resource group containing the virtual machine.|
|secret|no||| Azure client secret. Use when authenticating with a Service Principal.|
|state|no|present|<ul><li>absent</li><li>present</li><ul>|Assert the state of the virtual network. Use 'present' to create or update and 'absent' to delete.|
|subscription_id|no|||Your Azure subscription Id.|
|tags|no|||Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false. |
|tenant|no|||Azure tenant ID. Use when authenticating with a Service Principal.|

## Role Variables
|variable|location|example|comments|
|---|---|---|---|---|
|subscription_id|encrypted vault file|aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|Your Azure subscription Id.|
|tenant|encrypted vault file|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|Azure tenant ID. Use when authenticating with a Service Principal.|
|client_id|encrypted vault file|cccccccc-cccc-cccc-cccc-cccccccccccc|Azure client ID. Use when authenticating with a Service Principal.|
|secret|encrypted vault file|dddddddddddddddddddddddddddddddddddddddddddd| Azure client secret. Use when authenticating with a Service Principal.|
|vm_name|vars|testvm1|Name or list of names for the VMs|
|resource_group|vars|Test_Env_1|Name of the resource group containing the virtual machine.|
## Role Variables
|variable|location|example|comments|
|---|---|---|---|---|
|subscription_id|encrypted vault file|aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|Your Azure subscription Id.|
|tenant|encrypted vault file|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|Azure tenant ID. Use when authenticating with a Service Principal.|
|client_id|encrypted vault file|cccccccc-cccc-cccc-cccc-cccccccccccc|Azure client ID. Use when authenticating with a Service Principal.|
|secret|encrypted vault file|dddddddddddddddddddddddddddddddddddddddddddd| Azure client secret. Use when authenticating with a Service Principal.|
|vm_name|vars|testvm1|Name or list of names for the VMs|
|resource_group|vars|Test_Env_1|Name of the resource group containing the virtual machine.|
|virtual_network_name|vars|Test_Env_1-vnet|Name of the Virtual Network to build the VM in|
|public_ip|vars|<ul><li>false (default)</li><li>true</li><ul>| Sets a public ip address against a network interface|



## Examples

~~~
---
# This test playbook will create a network interface
- name: Test playbook for azure-create-network-interface
  hosts: localhost
  connection: local
  gather_facts: false
  user: ansible
  become: yes

  vars_files:
    - /home/ansible/vault.yml

  vars:
    resource_group: Test_Env_1
    virtual_network_name: Test_Env_1-vnet
    vm_name:
      - centostestvm1
      - centostestvm2

  roles:
    - azure-create-network-interface
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
