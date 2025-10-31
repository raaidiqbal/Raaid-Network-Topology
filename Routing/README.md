This is the README file for Raaid's Routing project 

CS 331, Fall 2025

## Contents of this directory

This directory contains all artifacts, data, and visuals for the **Routing Analysis Project**, part of the Network Topology project.

NetworkTopology/
├── RawData/
└── Artifacts/

### Analyzed Endpoints

* Lahore University of Management Sciences
* London School of Economics
* University of Queensland
* University of California, Santa Cruz
* University of São Paulo
* Microsoft Corporation 

### Tools and Methods

- Telnet to access Route Views BGP collector
- Kepler.gl for the global map
- Diagrams.net for AS path diagrams
- Google My Maps for ISP locations
- Excel and Python for crunching numbers

## Key Insights

- Hurricane Electric (AS6939) showed up in every single route since it's a massive Tier 1 backbone
- Most routes took about 3-4 hops on average
- Regional destinations (UCSC, Microsoft) had the shortest paths
- São Paulo had the longest route at around 5 hops
- BGP routes show what networks decide based on policy, traceroutes show what actually happens in real-time  

### Links

- [Cloudflare Blog: “How BGP Keeps the Internet Running”](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/)  
- [Wikipedia: Internet Service Provider (ISP)](https://en.wikipedia.org/wiki/Internet_service_provider)  
- [Cloudflare: What is an Autonomous System?](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)  
- [ARIN: Autonomous System Numbers](https://www.arin.net/resources/guide/asn/)  
- [Cloudflare: Internet Protocol (IP)](https://www.cloudflare.com/learning/network-layer/internet-protocol/)  
- [Computer Networks: A Systems Approach — Scaling the Internet](https://book.systemsapproach.org/scaling/global.html)  
- [APNIC Blog: The Economics of BGP Peering](https://blog.apnic.net/2020/09/21/the-economics-of-bgp-peering/)  
- [Wikipedia: Telnet](https://en.wikipedia.org/wiki/Telnet)  
- [Wikipedia: Traceroute](https://en.wikipedia.org/wiki/Traceroute)  
- [Cloudflare: What is a CDN?](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)  
- [Wikipedia: Internet Backbone](https://en.wikipedia.org/wiki/Internet_backbone) 

