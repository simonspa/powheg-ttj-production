# powheg-ttj-production
Scripts for POWHEG BOX v1 sample production for the ttJ user process

Installation
------------
 * Install `FASTJET 3.0.6`:
   * Use this version, newer versions might create problems and won't compile.
   * Build and install:
  ```
  wget http://fastjet.fr/repo/fastjet-3.0.6.tar.gz
  tar -xvf fastjet-3.0.6.tar.gz
  cd fastjet-3.0.6
  ./configure --prefix=$PWD/../fastjet-bin
  make
  make check
  make install
  ```

 * Install `LHAPDF 5.9.1`:
   * Download version 5.9.1, not the release 6.x since it won't work.
   * Build and install:
  ```
  wget http://www.hepforge.org/archive/lhapdf/lhapdf-5.9.1.tar.gz
  tar -xvzf lhapdf-5.9.1.tar.gz
  cd lhapdf-5.9.1
  ./configure --prefix=$PWD/../LHAPDF-bin
  make
  make install
  ```

 * Prepare environment variables
  ```
  #!/bin/bash
  export PATH=/nfs/dust/cms/user/spanns/powhegbox/fastjet-bin/bin:$PATH
  export PATH=/nfs/dust/cms/user/spanns/powhegbox/LHAPDF-bin/bin:$PATH
  export LHAPATH=/nfs/dust/cms/user/spanns/powhegbox/LHAPDF-bin/share/lhapdf/PDFsets
  ```

 * Install `POWHEG-BOX v1`:
   * `$ svn checkout --username anonymous --password anonymous svn://powhegbox.mib.infn.it/trunk/POWHEG-BOX`
   * the user process is located in the `ttJ` subfolder.
   * Hadronic top-quark pair-production with one jet and parton showering, S. Alioli, S.O. Moch and P. Uwer, JHEP 1201 (2012) 137, arXiv:1110.5251 [paper]
   ```
   cd POWHEG-BOX/ttJ
   make pwhg_main
   ```

 * Get the NAF scripts for multiple POWHEG nodes from this repository.

Production
----------
 * Log into your NAF job submission machine
 * Edit the configuration in `config/powheg.input-tmp` to your needs
 * create a new directory cd `cd` into it
 * run the production:
 
 ```
 # produce grids and stuff, no event generation yet
 export MASS=172p5
 ../runPowhegNAF.sh 1 $MASS
 # generate events:
 ../runPowhegNAF.sh 3 $MASS
```

* have fun.

Plotting
--------

 * use `topdrawer`: `wget theory.fnal.gov/people/parke/TD/td.tar.gz`
 * if this version doesn't work for you, compile your own from here: https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/TopDrawer
 
 ```
 wget https://cp3.irmp.ucl.ac.be/projects/madgraph/raw-attachment/wiki/TopDrawer/td.tgz
 mkdir td && cd td/ && tar -xvf ../td.tgz
 make
 ```
 
 * You need `g77` to compile this, `gfrotran` which is delivered with most modern distributions won't work.
 
 
