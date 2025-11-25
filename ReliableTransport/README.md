This is the README file for Raaid's Reliable Transport project 

CS 331, Fall 2025

## Contents of this directory

...
ReliableTransport/
│
├── RawData/
│   └── Raaid_full_trace.pcapng # Full capture
│   └── trace_stream8_Raaid.pcapng # Stream used for analysis for Congestion Control
│   └── trace_stream11_Raaid.pcapng # Stream used for analysis for the rest of the application
│
└── Artifacts/

...

This project explores how TCP (Transmission Control Protocol) provides reliable, ordered, and congestion-aware data transfer on top of the Internet s best-effort IP service. Using Wireshark, I captured and analyzed a real TCP connection (from a YouTube session) to illustrate each of TCP s core services: 
- Connection setup (three-way handshake)
- Reliable transmission and recovery Flow control and sliding window
- Congestion control
- Connection termination

Each section of the accompanying writeup highlights these features using annotated packet captures and sequence graphs.
