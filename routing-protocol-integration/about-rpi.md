# Dynamic Routing Protocol Integration (RIP & OSPF)

A network engineering project demonstrating the integration and redistribution of two different dynamic routing protocols (RIP and OSPF) within a single MikroTik router environment. This project highlights cross-protocol communication and automated internet route distribution.

## Tech Stack
* **Routing Protocols:** RIP (Routing Information Protocol) & OSPF (Open Shortest Path First)
* **Networking Concepts:** Route Redistribution, Distance Vector, Link-State, Network Address Translation (NAT)
* **Platform/OS:** MikroTik RouterOS (Winbox)

## Key Features
* **Multi-Protocol Integration:** Successfully combined a distance-vector protocol (RIP) and a link-state protocol (OSPF) within a 4-router topology.
* **Route Redistribution:** Configured redistribution on the boundary routers (Router 1 and Router 4) to allow seamless exchange of routing tables between the OSPF area and the RIP network, enabling end-to-end ICMP ping connectivity across all PCs.
* **Automated Internet Routing:** Implemented NAT and a single default route to the internet exclusively on Router 1. Leveraged the redistribution settings to automatically propagate this internet route to all other routers, providing internet access to all connected PCs without manual static routing on each device.
* **Interface & Network Configuration:** Systematically configured IP addresses, bridge loopback interfaces, and assigned specific network segments to their respective routing protocols (OSPF instances and RIP networks).
