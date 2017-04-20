# Delete Azure Storage Account

## Overview

Deletes a Storage Account on the Azure platform

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
- Ansible Cloud Module **azure_rm_virtualmachine**
 - Create, update, stop and start a virtual machine.


## Available 'azure_rm_virtualmachine' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|ad_user|no| |<ul>|Active Directory username. Use when authenticating with an Active Directory user rather than service principal.|
|admin_password|no| |<ul>|Password for the admin username. Not required if the os_type is Linux and SSH password authentication is disabled by setting ssh_password_enabled to false.|
|admin_username|no|||Admin username used to access the host after it is created. Required when creating a VM.|
|allocated|no|True|<ul><li>True</li><li>False</li></li>|Toggle that controls if the machine is allocated/deallocated, only useful with state='present'.|
|append_tags|no|True|<ul><li>True</li><li>False</li></li>|Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata.|
|client_id|no|||Azure client ID. Use when authenticating with a Service Principal.|
|image|yes|||A dictionary describing the Marketplace image used to build the VM. Will contain keys: publisher, offer, sku and version. NOTE: set image.version to 'latest' to get the most recent version of a given image.|
|location|no|||Valid Azure location. Defaults to location of the resource group.|
|name|yes|||Name of the virtual machine.|
|network_interface_names|no|||List of existing network interface names to add to the VM. If a network interface name is not provided when the VM is created, a default network interface will be created. In order for the module to create a network interface, at least one Virtual Network with one Subnet must exist.|
|open_ports|no|||If a network interface is created when creating the VM, a security group will be created as well. For Linux hosts a rule will be added to the security group allowing inbound TCP connections to the default SSH port 22, and for Windows hosts ports 3389 and 5986 will be opened. Override the default open ports by providing a list of ports.|
|os_disk_caching|no|ReadOnly|<ul><li>ReadOnly</li><li>ReadWrite</li></li>|Type of OS disk caching.|
|os_type|no|Linux|<ul><li>Windows</li><li>Linux</li></li>|Base type of operating system.|
|password|no|||Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.|
|profile|no|||Security profile found in ~/.azure/credentials file.|
|public_ip_allocation_method|no|Static|<ul><li>Dynamic</li><li>Static</li></li>|If a public IP address is created when creating the VM (because a Network Interface was not provided), determines if the public IP address remains permanently associated with the Network Interface. If set to 'Dynamic' the public IP address may change any time the VM is rebooted or power cycled.|
|remove_on_absent|no|All||When removing a VM using state 'absent', also remove associated resources.It can be 'all' or a list with any of the following: ['network_interfaces', 'virtual_storage', 'public_ips'].Any other input will be ignored|
|resource_group|yes|||Name of the resource group containing the virtual machine.|
|restarted|no|||Use with state 'present' to restart a running VM.|
|secret|no||| Azure client secret. Use when authenticating with a Service Principal.|
|short_hostname|no|||Name assigned internally to the host. On a linux VM this is the name returned by the `hostname` command. When creating a virtual machine, short_hostname defaults to name.|
|ssh_password_enabled|no|True||When the os_type is Linux, setting ssh_password_enabled to false will disable SSH password authentication and require use of SSH keys.|
|ssh_public_keys|no||| For os_type Linux provide a list of SSH keys. Each item in the list should be a dictionary where the dictionary contains two keys: path and key_data. Set the path to the default location of the authorized_keys files. On an Enterprise Linux host, for example, the path will be /home/<admin username>/.ssh/authorized_keys. Set key_data to the actual value of the public key. |
|started|no|True|<ul><li>True</li><li>False</li></li>|Use with state 'present' to start the machine. Set to false to have the machine be 'stopped'.|
|state|no|Present|<ul><li>Absent</li><li>Present</li></li>|AAssert the state of the virtual machine.State 'present' will check that the machine exists with the requested configuration. If the configuration of the existing machine does not match, the machine will be updated. Use options started, allocated and restarted to change the machine's power state. State 'absent' will remove the virtual machine.|
|storage_account_name|no|||Name of an existing storage account that supports creation of VHD blobs. If not specified for a new VM, a new storage account named <vm name>01 will be created using storage type 'Standard_LRS'.|
|storage_blob_name|no|||Name fo the storage blob used to hold the VM's OS disk image. If no name is provided, defaults to the VM name + '.vhd'. If you provide a name, it must end with '.vhd'|
|storage_container_name|no| vhds ||Name of the container to use within the storage account to store VHD blobs. If no name is specified a default container will created.|
|subnet_name|no|||When creating a virtual machine, if a network interface name is not provided, one will be created. The new network interface will be assigned to the first subnet found in the virtual network. Use this parameter to provide a specific subnet instead.|
|subscription_id|no|||Your Azure subscription Id.|
|tags|no|||Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false. |
|tenant|no|||Azure tenant ID. Use when authenticating with a Service Principal.|
|virtual_network_name|no||| When creating a virtual machine, if a network interface name is not provided, one will be created. The new network interface will be assigned to the first virtual network found in the resource group. Use this parameter to provide a specific virtual network instead. |
|vm_size|no|Standard_D1|| A valid Azure VM size value. For example, 'Standard_D4'. The list of choices varies depending on the subscription and location. Check your subscription for available choices. |

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
  # This test playbook will delete a storage account
- name: Test playbook for azure-create-storage-account
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
    - azure-delete-storage-account
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
