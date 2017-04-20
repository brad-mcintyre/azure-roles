# Delete Azure Security Group

## Overview

Deletes a Security Group on the Azure platform

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
- Ansible Cloud Module **azure_rm_securitygroup**
 - Create, update or delete a network security group.


## Available 'azure_rm_securitygroup' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|ad_user|no| |<ul>|Active Directory username. Use when authenticating with an Active Directory user rather than service principal.|
|append_tags|no|True|<ul><li>True</li><li>False</li></li>|Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata.|
|client_id|no|||Azure client ID. Use when authenticating with a Service Principal.|
|default_rules|no|||The set of default rules automatically added to a security group at creation. In general default rules will not be modified. Modify rules to shape the flow of traffic to or from a subnet or NIC. See rules below for the makeup of a rule dict.|
|location|no|||Valid Azure location. Defaults to location of the resource group.|
|name|yes|||Name of the security group to operate on.|
|password|no|||Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.|
|profile|no|||Security profile found in ~/.azure/credentials file.|
|purge_default_rules|no|||Remove any existing rules not matching those defined in the default_rules parameter.|
|resource_group|yes|||Name of the resource group the security group belongs to. |
|rules|no||See Dictionary object rules table below|Set of rules shaping traffic flow to or from a subnet or NIC. Each rule is a dictionary.|
|source_address_prefix|no|*||IP address or CIDR from which traffic originates.|
|secret|no||| Azure client secret. Use when authenticating with a Service Principal.|
|state|no|present|<ul><li>absent</li><li>present</li>|Assert the state of the security group. Set to 'present' to create or update a security group. Set to 'absent' to remove a security group.|
|subscription_id|no|||Your Azure subscription Id.|
|tags|no|||Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false. |
|tenant|no|||Azure tenant ID. Use when authenticating with a Service Principal.|

###Dictionary object rules###
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|source_address_prefix|no|* ||IP address or CIDR from which traffic originates.|
|destination_address_prefix|no|*||IP address or CIDR to which traffic is headed.|
|protocol|no|*|<ul><li>Udp</li><li>Tcp</li><li>*</li><ul>|Accepted traffic Protocol.|
|name|yes|||Unique name for the rule. 
|description|no|||Short description of the rule's purpose.|
|direction|no|Inbound|<ul><li>Inbound</li><li>Outbound</li><ul>|Indicates the direction of the traffic flow.|
|access|no|Allow|<ul><li>allow</li><li>deny</li><ul>|Whether or not to allow the traffic flow.|
|source_port_range|no|*|| Port or range of ports from which traffic originates. |
|destination_port_range|no|*||Port or range of ports to which traffic is headed.|
|priority|yes|||Order in which to apply the rule. Must a unique integer between 100 and 4096 inclusive.|



## Role Variables
|variable|location|example|comments|
|---|---|---|---|---|
|subscription_id|encrypted vault file|aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|Your Azure subscription Id.|
|tenant|encrypted vault file|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|Azure tenant ID. Use when authenticating with a Service Principal.|
|client_id|encrypted vault file|cccccccc-cccc-cccc-cccc-cccccccccccc|Azure client ID. Use when authenticating with a Service Principal.|
|secret|encrypted vault file|dddddddddddddddddddddddddddddddddddddddddddd| Azure client secret. Use when authenticating with a Service Principal.|
|vm_name|vars|testvm1|Name or list of names for the VMs|
|resource_group|vars|Test_Env_1|Name of the resource group containing the virtual machine.|


## Examples

~~~
---
# This test playbook will delete a security group
- name: Test playbook for azure-delete-security-group
  hosts: localhost
  connection: local
  gather_facts: false
  user: ansible
  become: yes

  vars_files:
    - /home/ansible/vault.yml

  vars:
    resource_group: Test_Env_1
    vm_name:
      - centostestvm1
      - centostestvm2

  roles:
    - azure-delete-security-group
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
