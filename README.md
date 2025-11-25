This is the README file for Raaid's CS 331, Fall 2025, project repository

## Contents of this repository

### Final Project Portfolio
This reflection ynthesizes lessons across all projects and addresses the central question "How does the structure and implementation of computer networks impact how we interact with the world?"

### 1. Gopher
Implementation of the Gopher protocol (RFC 1436), including both a Python client and server built using raw sockets. The project required interpreting the protocol specification directly, handling directory menus (type 1) and file retrieval (type 0), managing selector strings, and designing a robust message parser without external Gopher libraries.

### 2. Network Topology Analysis (Revised)
Analysis of network topology and routing paths using traceroute data.

The revision improves clarity and analysis by:

- Using slides more effectively (less text, more visuals and bullet points).
- Reorganizing tables by region/RTT and highlighting outliers.
- Replacing the earlier confusing comparison graph with direct RTT comparisons.
- Adding clearer analysis of routing patterns (e.g., when traffic exits via Hurricane Electric vs. NL) and why some regions show much weaker connectivity.

These updates make the project’s conclusions about global Internet performance and “network of networks” behavior more precise and easier to interpret.

### 3. BGP Routing Analysis
Investigation of how data travels across the internet using BGP routing data, examining the "network of networks."

### 4. Reliable Transport
Analysis of TCP traces to demonstrate its key services.

### 5. DNS (Revised)
This project analyzes how DNS works by examining real DNS traffic in Wireshark, using command-line tools like dig, and writing Python code to query hundreds of domains. The results compare Carleton's DNS resolver with Google's resolver, focusing on response behavior, IP differences, and TTL patterns.

In the revision, I addressed the missing analysis and subquestions by:

- Adding Part 4 to fully complete the report.
- Expanding Part 2 to identify all parts of the DNS message (ID, flags, opcode, rcode, question/answer/authority/additional sections, TTLs, etc.), not just the 5-tuple and flags.
- Comparing Wireshark vs. dig more carefully, explaining what appears only in the packet trace (e.g., full header fields, multiple queries, caching behavior) versus in command-line output (e.g., nicely summarized answers, timing).
- Explicitly discussing how many DNS servers were used (Carleton’s resolvers and Google’s), how they appear in the data, and what that implies about redundancy and resolver behavior.

This revision makes the DNS project’s protocol analysis and measurement discussion more complete and aligned with the assignment questions.

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





