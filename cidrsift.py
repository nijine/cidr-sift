# Author: Dmitriy Loshakov
# GitHub: github.com/nijine
# Distributed under GNU GPL v3.0. 
# Feel free to make edits and mangle the code for your own uses, but please
# maintain this notice if you intend to use it verbatim. Thanks.

from netaddr import *
import sys

if len(sys.argv) < 3:
	print("Not enough args.")
	print("Usage: python cidrsift.py <path-to-cidr-file> <path-to-ip-file>")
	sys.exit(1)
	
fnamecidrs = sys.argv[1]
fnameips = sys.argv[2]

with open(fnamecidrs) as fcidrs:
	rawcidrs = fcidrs.readlines()
	
rawcidrs = [l.strip() for l in rawcidrs]

with open(fnameips) as fips:
	rawips = fips.readlines()
	
rawips = [l.strip() for l in rawips]

for rawcidr in rawcidrs:
	cidr = IPNetwork(rawcidr)
	for rawip in rawips:
		ip = IPAddress(rawip)
		if ip in cidr:
			print(rawip)
			rawips.remove(rawip)