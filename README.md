# Washcat
---
Automation tool in Python to correlate cleartext passwords from a Hashcat pot file to the NTLM account names in the original job


```
usage: washcat.py [-h] [-o OUTPUT] [--ntlmv2] jobfile potfile

positional arguments:
  jobfile               Original Hashcat™ job file containing account names and hashes
  potfile               Original Hashcat™ pot file containing hashes and cleartext passwords

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of the output file which should contain the correlated names
                        and cleartext passwords (Default: stdout)
  --ntlmv2              Switch: Set job file hash type as NTLMv2 (Default: NTLM)
```

# Features
* Takes as input a list of NTLM hashes with account names (Hashcat format) such as : `admin:8757:aad3b435b51404eeaad3b435b51304ee:3ce5759293f20731a18800f526b5f6ce::: `
* Correlates with a typical Hashcat pot file which contains cleartext passwords but not the account names.


# Installation
* ` git clone https://github.com/stormyordos/washcat.git `
* Should work on most distributions supporting Python 3.x.

# Examples
* Dumps correlated account names and passwords to the standard output : `./washcat.py ntlmhashes.job ntlmcracked.pot`


