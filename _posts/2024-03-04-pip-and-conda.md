---
layout: post
title: Some pip incantations that I want to remember
date: 2024-03-04
tags: 
    - python
    - conda
    - pip
---

Using [showyourwork]() for the preparation of the paper discussing the methodology behind [kinisi]() has led to some unusual use of conda and pip. 
I have regularly googled the same things over and over to answer questions about formatting pip dependencies in a conda `environment.yml` file. 
Instead of repeating these searches, I decided to write them down in a post that I can refer to in future. 
Before you email me, yes [I know the problems of mixing conda and pip](https://stackoverflow.com/questions/56134588/is-that-a-bad-idea-to-use-conda-and-pip-install-on-the-same-environment) but showyourwork uses conda, and the kinisi methodology has things that rely on pip. 

## Dependency on a local (development) version of a package

The first use case is part of the development cycle, where you want to run showyourwork against different development code versions. 
For example, to optimise the way that some operation is performed. 
In this case, we can give the `environment.yml` an absolute path to the directory with the `pyproject.toml` or `setup.py` file. 
For this example, you can enforce that the environment installs an editable package version with a `-e` flag. 

For this `environment.yml`, this looks like this: 

```yml
dependencies:
  - ...
  - ...
  - pip:
      - -e /Users/arm61/code/kinisi
```

## Dependency on a remote (Github) version of a package

The second way that I have found myself working with `environment.yml` files is to run showyourwork against the GitHub repository.
For example, if the latest version of the code has yet to be released. 

In this case, we need the following `environment.yml` file:

```yml
dependencies:
  - ...
  - ...
  - pip:
    - git+https://github.com/bjmorgan/kinisi.git
```

### Dependency on a specific branch of the remote 

Finally, if we want a specific branch of the GitHub repository, then the `@` syntax is used. 
Making the `enviroment.yml` look like this: 

```yml
dependencies:
  - ...
  - ...
  - pip:
    - git+https://github.com/bjmorgan/kinisi.git@minimum_eigenvalue_method
```

One thing to note about all of these approaches is that showyourwork will keep an eye on scripts to see if the outputs need to be updated; it will not keep an eye on these dependencies in the same way. 
So if you don't change the `enviroment.yml` file, your scripts won't necessarily be rerun. 
Hopefully, this can help others or simply serve as a reminder for me. 
