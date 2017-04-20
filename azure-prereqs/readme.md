# Install Azure Module Prerequisites

## Overview

Installs the required packages for Azure Module functionality.

## Requirements (on host that executes modules)
This role requires the following packages installed on Ansible server.

- python 2.7.x
- ansible 2.2.x

The following packages are installed as part of this role.

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
 - Module will install if not already existing 
- Ansible Packaging Module **npm**
 - Manages node.js packages with Node Package Manager 
 - Module will install if not already existing 

## Available 'yum' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|conf_file|no|no|<ul>|The remote yum configuration file to use for the transaction.|
|disable_gpg_check|no|no|<ul><li>yes</li><li>no</li><ul>|Whether to disable the GPG checking of signatures of packages being installed. Has an effect only if state is present or latest.|
|disablerepo|no|||Repoid of repositories to disable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a ",".|
|enablerepo|no|||Repoid of repositories to enable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a ",".|
|exclude|no|||Package name(s) to exclude when state=present, or latest|
|installroot|no| / ||Specifies an alternative installroot, relative to which all packages will be installed.|
|list|no|||Package name to run the equivalent of yum list `<package>` against.|
|name|yes|||Package name, or package specifier with version, like `name-1.0`. When using state=latest, this can be '*' which means run: yum -y update. You can also pass a url or a local path to a rpm file (using state=present). To operate on several packages this can accept a comma separated list of packages or (as of 2.0) a list of packages.|
|skip_broken|no|no|<ul><li>yes</li><li>no</li></li><ul>|Resolve depsolve problems by removing packages that are causing problems from the trans‐ action.|
|state|no|present|<ul><li>present</li><li>installed</li><li>latest</li><li>absent</li><li>removed</li><ul>|Whether to install (`present` or `installed`, `latest`), or `remove` (`absent` or `removed`) a package.|
|update_cache|no|no|<ul><li>yes</li><li>no</li><ul>|Force yum to check if cache is out of date and redownload if needed. Has an effect only if state is present or latest.|
|validate_certs|no|yes|<ul><li>yes</li><li>no</li><ul>|This only applies if using a https url as the source of the rpm. e.g. for localinstall. If set to `no`, the SSL certificates will not be validated. This should only set to `no` used on personally controlled sites using self-signed certificates as it avoids verifying the source site. Prior to 2.1 the code worked as if this was set to `yes`.|

## Available 'pip' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|chdir|no|||cd into this directory before running the command|
|editable|no|true||Pass the editable flag for versioning URLs.|
|executable|no|||The explicit executable or a pathname to the executable to be used to run pip for a specific version of Python installed in the system. For example `pip-3.3`, if there are both Python 2.7 and 3.3 installations in the system and you want to run pip for the Python 3.3 installation. It cannot be specified together with the 'virtualenv' parameter (added in 2.1). By default, it will take the appropriate version for the python interpreter use by ansible, e.g. pip3 on python 3, and pip2 or pip on python 2.|
|extra_args|no|||Extra arguments passed to pip.|
|name|no|||The name of a Python library to install or the url of the remote package. As of 2.2 you can supply a list of names.|
|requirements|no|||The path to a pip requirements file, which should be local to the remote system. File can be specified as a relative path if using the chdir option.|
|state|no|present|<ul><li>present</li><li>absent</li><li>latest</li><li>forcereinstall</li><ul>|The state of module. The 'forcereinstall' option is only available in Ansible 2.1 and above.|
|umask|no|||The system umask to apply before installing the pip package. This is useful, for example, when installing on systems that have a very restrictive umask by default (e.g., 0077) and you want to pip install packages which are to be used by all users. Note that this requires you to specify desired umask mode in octal, with a leading 0 (e.g., 0077).|
|version|no|||The version number to install of the Python library specified in the name parameter|
|virtualenv|no|||An optional path to a virtualenv directory to install into. It cannot be specified together with the 'executable' parameter (added in 2.1). If the virtualenv does not exist, it will be created before installing packages. The optional virtualenv_site_packages, virtualenv_command, and virtualenv_python options affect the creation of the virtualenv.|
|virtualenv_command|no|||The command or a pathname to the command to create the virtual environment with. For example `pyvenv`, `virtualenv`, `virtualenv2`, `~/bin/virtualenv`, `/usr/local/bin/virtualenv`.|
|virtualenv_python|no|||The Python executable used for creating the virtual environment. For example `python3.5`, `python2.7`. When not specified, the Python version used to run the ansible module is used.|
|virtualenv_site_packages|no|yes|<ul><li>yes</li><li>no</li><ul>|Whether the virtual environment will inherit packages from the global site-packages directory. Note that if this setting is changed on an already existing virtual environment it will not have any effect, the environment must be deleted and newly created.|

## Available 'npm' Module Parameters
|parameter|required|default|choices|comments|
|---|---|---|---|---|
|executable|no|||The executable location for npm. This is useful if you are using a version manager, such as nvm|
|global|no||<ul><li>yes</li><li>no</li>|Install the node.js library globally|
|ignore_scripts|no||<ul><li>yes</li><li>no</li><ul>|Use the --ignore-scripts flag when installing.|
|name|no|||The name of a node.js library to install|
|path|no|||The base path where to install the node.js libraries|
|production|no||<ul><li>yes</li><li>no</li><ul>|Install dependencies in production mode, excluding devDependencies|
|registry|no|||The registry to install modules from.|
|state|no||<ul><li>present</li><li>absent</li><li>latest</li><ul>|The state of the node.js library|
|version|no||| The version to be installed |

## Role Variables
|variable|location|example|comments|
|---|---|---|---|---|
|prereq_yum_packages|vars|<ul><li>python-pip</li><li>gcc</li><li>libffi-devel</li><li>python-devel</li><li>openssl-devel</li><li>nodejs</li><li>npm</li><ul>|List of yum packages to install in order of install preference|
|azure_npm_packages|vars|<ul><li>azure-cli</li><ul>|List of npm packages to install in order of install preference|
|azure_pip_packagesvars|vars|<ul><li>cryptography</li><li>azure==2.0.0rc5</li><li>msrestazure</li><ul>|List of pip packages to install in order of install preference|

## Examples

~~~
---
#This test playbook will install the required packages for the Azure modules
- name: Test playbook for azure-prereqs
  hosts: localhost
  gather_facts: false
  user: ansible
  become: yes

  vars:
    prereq_yum_packages:
      - python-pip
      - gcc
      - libffi-devel
      - python-devel
      - openssl-devel
      - nodejs
      - npm

    azure_npm_packages:
      - azure-cli

      azure_pip_packages:
      - cryptography
      - azure==2.0.0rc5
      - msrestazure

  roles:
    - azure-prereqs

    ---



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
