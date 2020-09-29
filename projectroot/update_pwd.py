import os, sys
with open(sys.argv[1], 'r') as f: 
	x = f.read()
fromexpr = 'C:/dev/10.7/apama-test/system/correlator/corba/testcases/correctness/Corr_Corba_cor_1529'
assert fromexpr in x, x
x = x.replace(fromexpr, os.getcwd().replace('\\','/'))
print(x)
with open(sys.argv[1], 'w') as f: 
	f.write(x)
