This is the README file for Raaid's CS 331, Fall 2025, project repository

## Contents of this repository

### Final Project Portfolio
This reflection ynthesizes lessons across all projects and addresses the central question "How does the structure and implementation of computer networks impact how we interact with the world?"

### 1. Gopher
Implementation of the Gopher protocol (RFC 1436), including both a Python client and server built using raw sockets. The project required interpreting the protocol specification directly, handling directory menus (type 1) and file retrieval (type 0), managing selector strings, and designing a robust message parser without external Gopher libraries.

### 2. Network Topology Analysis (Revised)
Analysis of network topology and routing paths using traceroute data.

### 3. BGP Routing Analysis
Investigation of how data travels across the internet using BGP routing data, examining the "network of networks."

### 4. Reliable Transport
Analysis of TCP traces to demonstrate its key services.

### 5. DNS (Revised)
This project analyzes how DNS works by examining real DNS traffic in Wireshark, using command-line tools like dig, and writing Python code to query hundreds of domains. The results compare Carleton's DNS resolver with Google's resolver, focusing on response behavior, IP differences, and TTL patterns.



## Repository Structure
```
├── README.md
├── Final Reflection.pdf
│
├── Gopher/
│   └── [Gopher Repository](https://github.com/raaidiqbal/cs331-gopher-Raaid)
│
├── NetworkTopology/
│   ├── README.md
│   ├── RawData/
│   ├── Artifacts/
│   └── Slides/
│
├── RoutingAnalysis/
│   ├── README.md
│   ├── RawData/
│   └── Artifacts/
│
├── ReliableTransport/
│   ├── README.md
│   ├── RawData/
│   └── Artifacts/
│
└── DNS/
    ├── README.md
    ├── Artifacts/
    │   ├── dnsExample.py
    │   ├── dnsQueries.py
    │   ├── Raad_Results.csv
    │   ├── Raaid_full_trace.pcapng
    │   ├── top500.csv
    │   └── .gitkeep
    └── RawData/


**Collaborators:**

* Amy Csizmar Dalal





