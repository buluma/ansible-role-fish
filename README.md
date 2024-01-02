# Ansible role [fish](https://galaxy.ansible.com/ui/standalone/roles/buluma/fish/documentation)

Install the Friendly Interactive Shell (fish)

|GitHub|Version|Issues|Pull Requests|Downloads|
|------|-------|------|-------------|---------|
|[![github](https://github.com/buluma/ansible-role-fish/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/ansible-role-fish/actions/workflows/molecule.yml)|[![Version](https://img.shields.io/github/release/buluma/ansible-role-fish.svg)](https://github.com/buluma/ansible-role-fish/releases/)|[![Issues](https://img.shields.io/github/issues/buluma/ansible-role-fish.svg)](https://github.com/buluma/ansible-role-fish/issues/)|[![PullRequests](https://img.shields.io/github/issues-pr-closed-raw/buluma/ansible-role-fish.svg)](https://github.com/buluma/ansible-role-fish/pulls/)|[![Ansible Role](https://img.shields.io/ansible/role/d/buluma/fish)](https://galaxy.ansible.com/ui/standalone/roles/buluma/fish/documentation)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/buluma/ansible-role-fish/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- hosts: all
  become: yes

  vars:
    distros:
      - Debian9
      - Debian10
      - RedHat7
      - RedHat8
      - Fedora30
      - Fedora31
      - Fedora32
      - Ubuntu16
      - Ubuntu18
      - Ubuntu20

  tasks:

    - include_role:
        name: buluma.fish
      when: ansible_facts.distribution ~ ansible_facts.distribution_major_version in distros
```

Also see a [full explanation and example](https://buluma.github.io/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/buluma/ansible-role-fish/blob/master/defaults/main.yml):

```yaml
---
fish_release_version: 3
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/buluma/ansible-role-fish/blob/master/requirements.txt).


## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://buluma.github.io/) for further information.

Here is an overview of related roles:

![dependencies](https://raw.githubusercontent.com/buluma/ansible-role-fish/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/buluma):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/repository/docker/buluma/enterpriselinux/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/buluma/ubuntu/general)|all|
|[Debian](https://hub.docker.com/repository/docker/buluma/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/buluma/fedora/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/buluma/ansible-role-fish/issues)

## [Changelog](#changelog)

[Role History](https://github.com/buluma/ansible-role-fish/blob/master/CHANGELOG.md)

## [License](#license)

[Apache 2.0](https://github.com/buluma/ansible-role-fish/blob/master/LICENSE)

## [Author Information](#author-information)

[Shadow Walker](https://buluma.github.io/)

