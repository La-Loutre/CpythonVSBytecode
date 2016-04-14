# Cpython vs binary performance (python2.7)

## Test

$ make

$ python3 test_use_binary.py

## Result


Matrice add result , size mat =1000,repeat =100

Binary time : 0.000782012939453125

CPython time : 0.018803119659423828

Speed increase with binary+latency : x24.04451219512195



Matrice add result , size mat =1000,repeat =1000

Binary time : 0.0007157325744628906

CPython time : 0.15341782569885254

Speed increase with binary+latency : x214.35076615589608
