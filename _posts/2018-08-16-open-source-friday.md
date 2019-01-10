---
layout: post
title: Open Source Friday
subtitle: Working on open projects
date: 2018-08-16
---
[Open source Friday](https://opensourcefriday.com/) in an initiative started by GitHub, which pushes people and businesses to contribute to open source code once a week.

As part of a personal experiment, to grow my skills as a programmer while improving code that exists in the open-source community, I am going to try and spend (at least some of) my Fridays working on open source programming projects.
Obviously as a PhD student I have a bit more freedom with my time than the typical programmer, so I understand that not everyone is able to do this.

I am going to try and (to some extent) document the open-source work I do, and maybe this will allow me to offer insight to contributing to open source code.

This started on last Friday (2018-08-10), and I am going to *briefly* write about one of my contributions.

### My first pull request (in mdanalysis)

mdanalysis is a python library for molecular dynamic simulation analysis.
I wanted to contribute something after getting back in touch with one of the maintainers ([@richardjgowers](https://github.com/richardjgowers)) whom I had met a conference a few years ago.

Richard suggested [issue #1897](https://github.com/MDAnalysis/mdanalysis/issues/1897) as a good place for a newbie to work on.
This particular issue was related to the [PDB file format](https://www.rcsb.org/pdb/static.do?p=file_formats/pdb/index.html), in particular the fact that if there are more than 99999 atoms in the PDB trajectory it starts to count in base36.
This seemed initially to be an easy fix, simply if the number is greater than 99999 convert from hex using ```int(number, 36)```.

However, after implementing some tests, which failed, I discovered that as with many things about the PDB file format, it wasn't a *very* easy fix.
It turns out, as discussed in the [pull request](https://github.com/MDAnalysis/mdanalysis/pull/1978#issuecomment-411688646), the PDB file format doesn't fall back to standard base36, instead implementing a [case-sensitive hybrid36](http://cci.lbl.gov/hybrid_36/pdb_format_evolution.pdf).
Basically the way that the PDB atom indexing is as follows:

- counts from 1 to 99999,
- once it reaches 100000, there are only 5 columns available for numbers so it goes to A0000, then A0001, ..., A000Z, etc.,
- this then counts until ZZZZZ, which is equivalent to 43770015,
- then it uses the lower case versions, a0000,
- this continues to zzzzz, meaning that in 5 columns the pdb can count to 87440031.

So late Friday afternoon, after I included some tests that *hopefully* immortalised some of my office mates in the [code](https://github.com/MDAnalysis/mdanalysis/blob/develop/testsuite/MDAnalysisTests/topology/test_pdb.py#L45), the pull request was accepted and I became an official contributor to mdanalysis.

Hopefully this is a series I will continue when I have time.
