This is the README file for Raaid's DNS project

CS 331, Fall 2025

### Revised for Final Reflection

In the revision, I addressed the missing analysis and subquestions by:

- Adding Part 4 to fully complete the report.
- Expanding Part 2 to identify all parts of the DNS message (ID, flags, opcode, rcode, question/answer/authority/additional sections, TTLs, etc.), not just the 5-tuple and flags.
- Comparing Wireshark vs. dig more carefully, explaining what appears only in the packet trace (e.g., full header fields, multiple queries, caching behavior) versus in command-line output (e.g., nicely summarized answers, timing).
- Explicitly discussing how many DNS servers were used (Carleton’s resolvers and Google’s), how they appear in the data, and what that implies about redundancy and resolver behavior.

This revision makes the DNS project’s protocol analysis and measurement discussion more complete and aligned with the assignment questions.

## Contents of this folder 

This project analyzes how DNS works by examining real DNS traffic in Wireshark, using command-line tools like dig, and writing Python code to query hundreds of domains. The results compare Carleton's DNS resolver with Google's resolver, focusing on response behavior, IP differences, and TTL patterns.

```
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
