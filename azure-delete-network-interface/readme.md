# Delete Azure Network Interface

## Overview

Deletes a Network Interface on the Azure platform

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
- Ansible Cloud Module **azure_rm_networkinterface**
 - Create, update or delete a network interface.

## Available 'azure_rm_networkinterface' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|ad_user|no| |<ul>|Active Directory username. Use when authenticating with an Active Directory user rather than service principal.|
|append_tags|no|True||Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata.|
|client_id|no|||Azure client ID. Use when authenticating with a Service Principal.|
|location|no|||Valid Azure location. Defaults to location of the resource group.|
|name|yes|||name of the network interface.|
|open_ports|no|||When a default security group is created for a Linux host a rule will be added allowing inbound TCP connections to the default SSH port 22, and for a Windows host rules will be added allowing inbound access to RDP ports 3389 and 5986. Override the default ports by providing a list of open ports.|
|os_type|no|Linux|<ul><li>Windows</li><li>Linux</li><ul>|Determines any rules to be added to a default security group. When creating a network interface, if no security group name is provided, a default security group will be created. If the os_type is 'Windows', a rule will be added allowing RDP access. If the os_type is 'Linux', a rule allowing SSH access will be added.|
|password|no|||Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.|
|private_ip_address|no|||Valid IPv4 address that falls within the specified subnet.|
|private_ip_allocation_method|no|Dynamic|<ul><li>Dynamic</li><li>Static</li><ul>|Specify whether or not the assigned IP address is permanent. NOTE: when creating a network interface specifying a value of 'Static' requires that a private_ip_address value be provided. You can update the allocation method to 'Static' after a dynamic private ip address has been assigned.|
|profile|no|||Security profile found in ~/.azure/credentials file. |
|public_ip|not|true||When creating a network interface, if no public IP address name is provided a default public IP address will be created. Set to false, if you do not want a public IP address automatically created.|
|public_ip_address_name|no|||Name of an existing public IP address object to associate with the security group.|
|public_ip_allocation_method|no|Dynamic|<ul><li>Dynamic</li><li>Static</li><ul>|If a public_ip_address_name is not provided, a default public IP address will be created. The allocation method determines whether or not the public IP address assigned to the network interface is permanent.|
|resource_group|yes|||Name of the resource group containing the virtual machine.|
|secret|no||| Azure client secret. Use when authenticating with a Service Principal.|
|security_group_name|no|||Name of an existing security group with which to associate the network interface. If not provided, a default security group will be created.
|state|no|present|<ul><li>absent</li><li>present</li><ul>|Assert the state of the virtual network. Use 'present' to create or update and 'absent' to delete.|
|subnet_name|no|||Name of an existing subnet within the specified virtual network. Required when creating a network interface|
|subscription_id|no|||Your Azure subscription Id.|
|tags|no|||Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false. |
|tenant|no|||Azure tenant ID. Use when authenticating with a Service Principal.|
|virtual_network_name|no|||Name of an existing virtual network with which the network interface will be associated. Required when creating a network interface.|

## Role Variables
|variable|location|example|comments|
|---|---|---|---|---|
|azure_subscription_id|encrypted vault file|aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|Your Azure subscription Id.|
|azure_tenant|encrypted vault file|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|Azure tenant ID. Use when authenticating with a Service Principal.|
|azure_client_id|encrypted vault file|cccccccc-cccc-cccc-cccc-cccccccccccc|Azure client ID. Use when authenticating with a Service Principal.|
|azure_secret|encrypted vault file|dddddddddddddddddddddddddddddddddddddddddddd| Azure client secret. Use when authenticating with a Service Principal.|
|name|vars|testvm1|Name or list of names for the VMs|
|azure_resource_group|vars|Test_Env_1|Name of the resource group containing the virtual machine.|
|azure_network_interface_name|vars|Testvm1_nic1|Name of the netword interface to delete|


## Examples

~~~
---
# This test playbook will delete a network interface
- name: Test playbook for azure-delete-network-interface
  hosts: localhost
  connection: local
  gather_facts: false
  user: ansible
  become: yes

  vars_files:
    - /home/ansible/vault.yml

  vars:
    azure_resource_group: Mocatad_EV15_AS
    azure_name:
      - name: win2008testvm1
        azure_network_interface_name: win2008testvm1-nic1

  roles:
    - azure-delete-network-interface
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
