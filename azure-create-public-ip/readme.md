# Create Azure Public IP Address

## Overview

Creates a Public IP Address on the Azure platform

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
- Ansible Cloud Module **azure_rm_publicipaddress**
 - Create, update and delete a Public IP address.


## Available 'azure_rm_publicipaddress' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|ad_user|no| |<ul>|Active Directory username. Use when authenticating with an Active Directory user rather than service principal.|
|allocation_method|no|Dynamic|<ul><li>Dynamic</li><li>Static</li><ul>|Control whether the assigned Public IP remains permanently assigned to the object. If not set to 'Static', the IP address my changed anytime an associated virtual machine is power cycled.|
|append_tags|no|True||Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata.|
|client_id|no|||Azure client ID. Use when authenticating with a Service Principal.|
|domain_name_label|no|||The customizable portion of the FQDN assigned to public IP address. This is an explicit setting. If no value is provided, any existing value will be removed on an existing public IP.|
|location|no|||Valid Azure location. Defaults to location of the resource group.|
|name|yes|||Name of the Public IP.|
|password|no|||Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.|
|profile|no|||Security profile found in ~/.azure/credentials file.|
|resource_group|yes|||Name of the resource group containing the virtual machine.|
|secret|no||| Azure client secret. Use when authenticating with a Service Principal.|
|state|no|present|<ul><li>absent</li><li>present</li><ul>|Assert the state of the virtual network. Use 'present' to create or update and 'absent' to delete.|
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
|azure_public_ip_allocation_method|vars|Static|Public IP Allocation Method|
|domain_name_label|vars|testvm1|The customizable portion of the FQDN assigned to public IP address. |

## Examples

~~~
---
# This test playbook will create a public ip
- name: Test playbook for azure-create-public-ip
  hosts: localhost
  connection: local
  gather_facts: false
  user: ansible
  become: yes

  vars_files:
    - /home/ansible/vault.yml

  vars:
    azure_resource_group: Test_Env_1
    azure_public_ip_allocation_method: Dynamic
    azure_public_ip_name: 
      - win2008testvm101
      - centostestvm101

  roles:
    - azure-create-public-ip
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
