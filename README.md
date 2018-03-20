# cidr-sift
CIDR-Sift is a python script to sort IP addresses into CIDR blocks using netaddr. It was written to help a friend with processing large IP address sets in relation to a given list of CIDR blocks, and posted here to (hopefully) help someone out who's learning how to use netaddr. Python, and by association netaddr, makes this incredibly intuitive, but I did my best to structure the code and use sensible naming conventions for greater legibility.

The idea here was to create a (very) simple script to process large data sets as quickly as possible. There may still be room for optimization, but I did the following in around 25 minutes:
- Research how to implement netaddr
- Research how to install a python module
- Look up python's file I/O syntax
- Create a rough algorithm
- Test

Quick walk-through of how it works and what the code is doing:
How to use:
python cidrsift.py <path-to-cidr-file> <path-to-ip-file>

Example CIDR and IP address files can be found in this repository under "examples."

What it's doing:
1. Import netaddr and sys modules.
2. Check that the user put in at least 2 arguments after the script name, print usage if they did not.
3. Collect the inputs to use as file name strings.
4. Open the cidr file, read it into an array variable.
5. Strip each array element of it's spaces and trailing special chars (\n, \t, etc).
6. Repeat steps 4 and 5 for the IP address file.
7. For each string in the array of CIDR strings, create a CIDR (IPNetwork) object.
7b. While in the above loop: For each IP address string in the array of IP address strings, create an IP (IPAddress) object.
7c. If this IP object falls within the scope that the above CIDR object covers, print it to stdout and remove the respective IP address string from the IP address strings array (we don't have to process it again).

Feel free to mangle the code for your own uses, but please maintain the author and license notice if you intend to use the script verbatim.
