# Enterprise Network Design (Bank Mu)

A comprehensive, top-down enterprise network architecture proposal designed for "Bank Mu", featuring a scalable hierarchical topology that interconnects 20 operational sites. This project simulates a real-world infrastructure deployment focusing on high availability, secure routing, and centralized management.

## Tech Stack
* **Routing Protocols:** OSPF (Open Shortest Path First)
* **Switching & VLAN:** Inter-VLAN Routing, Port-Security, and STP
* **Security & VPN:** IPSec VPN, Access Control Lists (ACL), and SSH
* **Simulation Tool:** Cisco Packet Tracer

## Key Features
* **Top-Down Methodology:** Applied the Top-Down Network Design approach to align business goals with technical protocols and hardware selections.
* **Hierarchical Architecture:** Structured the network with Core, Distribution, and Access layers, implementing Dual Multilayer Switches and Dual ISPs for high availability and redundancy.
* **Logical Segmentation:** Segmented the network into specific VLANs (Sales, HR, Finance, Admin, IT, and Server Farm) to optimize broadcast traffic and improve local security.
* **Secure Communication:** Configured IPSec VPN tunnels and strict ACLs to ensure encrypted and secure data transmission between branch offices and the central server,
* **Centralized Services:** Implemented a centralized DHCP Server using IP Helper addresses for automated IP distribution across different subnets.
