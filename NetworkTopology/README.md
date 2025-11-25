This is the README file for Raaid's Network Topology project

CS 331, Fall 2025

### Revised for Final Reflection'

The revision improves clarity and analysis by:

* Using slides more effectively (less text, more visuals and bullet points).
* Reorganizing tables by region/RTT and highlighting outliers.
* Replacing the earlier confusing comparison graph with direct RTT comparisons.
* Adding clearer analysis of routing patterns (e.g., when traffic exits via Hurricane Electric vs. NL) and why some regions show much weaker connectivity.

These updates make the project’s conclusions about global Internet performance and “network of networks” behavior more precise and easier to interpret.

## Directory contents
...

NetworkTopology/
│   README.md
│
├── Artifacts/
│   
│
├── RawData/
│   
│
└── Slides/

The purpose of this project was to test 6 different endpoints to obtain a picture of how Carleton College is connected to the wider internet. The comparison was done using traceroutes, pings, and RIPE.

Endpoints tested:

* Lahore University of Management Sciences
* London School of Economics
* University of Queensland
* University of California, Santa Cruz
* University of São Paulo
* Microsoft Corporation   

Tools used:

* Traceroute (tracert): used to map the path and latency of packets to various global destinations

* Ping: used to measure average Round Trip Times (RTTs)

* RIPE Atlas: used to compare local and global latency measurements

IP lookup tools:

* RIPE
* https://www.submarinecablemap.com/
* whatismyipaddress.com

Visualization tools: Google Slides, and Google Sheets

The results showed that Carleton is connected through Hurricane Electric and Northern Lights. The US is very well connected with low latency, and Asia, Oceania, South America are less well connected.

