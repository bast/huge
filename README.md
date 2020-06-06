

# huge

Find huge additions in Git history.


### Command line options

```
$ huge --help

Usage: huge [OPTIONS]

Options:
  --branch TEXT          Which branch to scan.  [default: master]
  --num-entries INTEGER  How many top entries to show.  [default: 20]
  --cutoff INTEGER       Cutoff (bytes) below which to ignore entries.
                         [default: 1000000]

  --help                 Show this message and exit.
```


### Example output

```
$ huge

scanning the history ...
100%|████████████████████████████████████████████████████████████████████| 2493/2493 [00:59<00:00, 41.56it/s]


  size (MB)  path                                                    commit
-----------  ------------------------------------------------------  ----------------------------------------
   43.0599   test/dectests/decrimp2/result/decrimp2_CO2H2.out        c375b575a6310f056a4dd07f9327b3d217b0ea4b
   43.0269   test/dectests/decsosrimp2/result/decsosrimp2_CO2H2.out  3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
   10.7648   test/dectests/large_decrimp2/dens.restart               3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
   10.7648   LSDALTON/test/dectests/large_decrimp2/dens.restart      c45c4467bf72141bf073fcb584eed0786095c339
   10.7648   test/dectests/large_decrimp2/overlapmatrix              3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
   10.7648   test/dectests/large_decrimp2/lcm_orbitals.u             3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
   10.7648   test/dectests/large_decrimp2/fock.restart               3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
   10.7648   test/dectests/large_decrimp2/cmo_orbitals.u             3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
   10.7648   LSDALTON/test/dectests/large_decrimp2/overlapmatrix     c45c4467bf72141bf073fcb584eed0786095c339
   10.7648   LSDALTON/test/dectests/large_decrimp2/lcm_orbitals.u    c45c4467bf72141bf073fcb584eed0786095c339
   10.7648   LSDALTON/test/dectests/large_decrimp2/fock.restart      c45c4467bf72141bf073fcb584eed0786095c339
   10.7648   LSDALTON/test/dectests/large_decrimp2/cmo_orbitals.u    c45c4467bf72141bf073fcb584eed0786095c339
    2.53132  src/LSint/lsdalton_dftd_pars.h                          3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
    2.53132  LSDALTON/LSint/lsdalton_dftd_pars.h                     c45c4467bf72141bf073fcb584eed0786095c339
    1.9964   test/ref/n2_energy_densfitFCK3_old.ref                  3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
    1.9964   LSDALTON/test/ref/n2_energy_densfitFCK3_old.ref         c45c4467bf72141bf073fcb584eed0786095c339
    1.83527  test/ref/decmp2_geoopt_FO.ref                           3bfa9d4d59e7523921cd66244e2d8f2fb488fbd1
    1.83527  LSDALTON/test/ref/decmp2_geoopt_FO.ref                  c45c4467bf72141bf073fcb584eed0786095c339
    1.80867  src/FraME/FraME.tar.gz                                  35a9ce3cc06da8c635fdef44d3d1689e7946fc60
    1.80866  src/FraME/FraME.tar.gz                                  12651386cc1d7d29876179fd22629e29703a3f0a
```
