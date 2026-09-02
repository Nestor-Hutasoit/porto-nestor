# Enterprise Network Design (Perusahaan Nagoya)

A top-down hierarchical network architecture and implementation designed for Perusahaan Nagoya's new building[cite: 12]. This project focuses on building a highly available, segmented, and secure enterprise network utilizing multilayer switches, dynamic routing, and IPSec VPN tunneling.

## Tech Stack
* **Routing Protocols:** OSPF (Open Shortest Path First)
* **Switching & VLAN:** Inter-VLAN Routing, Port-Security, and Trunking
* **Security & VPN:** IPSec VPN, Access Control Lists (ACL), and SSH
* **Services:** Centralized DHCP Server with IP Helper addressing
* **Simulation Tool:** Cisco Packet Tracer

## Key Features
* **Hierarchical Redundancy:** Implemented a multi-layer architecture with dual Multilayer Switches (MLS) and dual ISPs to ensure network resilience and eliminate single points of failure.
* **Logical Segmentation:** Divided the network into 6 specific VLANs (Sales & Marketing, HR & Logistic, Finance & Admin, Admin & Humas, IT, and Server) for optimized traffic management.
* **Dynamic Convergence:** Configured OSPF as the internal routing protocol to ensure fast and dynamic route discovery.
* **Secure Data Center Connectivity:** Established an IPSec VPN tunnel across public ISP networks to securely encrypt traffic between the main office and the Server Side.
* **Device & Access Security:** Secured remote device management using SSH v2 with strict ACL filtering, and enforced physical security at the access switch level using Port-Security with violation shutdown.
* **Centralized DHCP Provisioning:** Utilized IP Helper addresses on the MLS to relay DHCP requests from various VLANs to a centralized server.
