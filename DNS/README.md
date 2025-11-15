This is the README file for Raaid's DNS project

CS 331, Fall 2025

## Contents of this folder 

This project analyzes how DNS works by examining real DNS traffic in Wireshark, using command-line tools like dig, and writing Python code to query hundreds of domains. The results compare Carleton's DNS resolver with Google's resolver, focusing on response behavior, IP differences, and TTL patterns.

└─ DNS
├── README.md
│
├─── Artifacts
│   ├── dnsExample.py         
│   ├── dnsQueries.py          
│   ├── Raad_Results.csv       
│   ├── Raaid_full_trace.pcapng
│   ├── top500.csv             
│   └── .gitkeep
│
└─── RawData

To install dnspython:
  pip install dnspython

To run the script:
  python Artifacts/dnsQueries.py
