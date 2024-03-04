---
layout: post
title: Different pip incantations I always forget
date: 2024-03-02
tags: 
    - python
    - conda
    - pip
---

Using [showyourwork]() for the preparation of the paper discussing the methodology behind [kinisi]() has led to some unusual use of conda and pip. 
I have regularly found myself googling the same things over and over to answer questions aboht formatting pip dependencies in a conda `environment.yml` file. 
Instead of repeating these searches, I thought it would be good to write them down in a post that I can refer to in future. 
Before you email me, yes [I know the problems of mixing conda and pip](https://stackoverflow.com/questions/56134588/is-that-a-bad-idea-to-use-conda-and-pip-install-on-the-same-environment) but showyourwork uses conda and the kinisi methodology has things that rely on pip. 

## Dependency on a local (development) version of a package

The first use case is part of the development cycle, where you want to run showyourwork against different versions of the development code. 
For example, to optimise the way that some operation is performed. 
In this case, we can give the `environment.yml` an absolute path to the directory with the `pyproject.toml` or `setup.py` file. 
For this example, you can enforce that the environment installs an editable version of the pacakge with a `-e` flag. 

In the `environment.yml` this looks like: 

```yml
dependencies:
  - ...
  - ...
  - pip:
      - -e /Users/arm61/code/kinisi
```

## Dependency on a remote (Github) version of a package

### Dependency on a specific branch of the remote 
