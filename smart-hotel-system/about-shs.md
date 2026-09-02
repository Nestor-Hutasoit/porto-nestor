# Smart Hotel IoT & Monitoring System

An edge-sensing IoT architecture designed to automate housekeeping services and optimize energy management in hotel rooms. This project resolves operational inefficiencies, such as False Make Up Room (MUR) incidents and energy waste, by integrating physical sensors with a secure, real-time data analytics pipeline.

## Tech Stack
* **Hardware:** ESP32, PIR Sensor, DHT11, Magnetic Switch, 5V Relay Module.
* **Networking & Security:** MQTT (Mosquitto Broker), Tailscale VPN.
* **Data Processing & Storage:** Python, InfluxDB.
* **Analytics & Visualization:** Apache Spark (PySpark), Grafana.

## Key Features
* **Edge Sensing & Actuation:** The ESP32 micro-controller processes sensor data locally to evaluate room occupancy and triggers a 5V relay to cut off electrical power when the room is vacant. This ensures energy savings even if internet connectivity is unstable.
* **Multi-Sensor State Machine:** Combines data from a PIR motion sensor and a magnetic door switch using a state machine algorithm[cite: 14]. It utilizes an 8-second delay verification window to accurately confirm if a guest has left the room before updating the occupancy status.
* **Secure Data Transmission:** Deploys Tailscale VPN to establish an encrypted, peer-to-peer mesh network, effectively isolating the MQTT telemetry traffic from public or guest Wi-Fi networks.
* **Micro-Batching Pipeline:** Utilizes a Python subscriber script with a 5-second buffer and state retention mechanism to process MQTT payloads. This approach eliminates empty (NaN) values before writing the time-series data to InfluxDB.
* **Automated Housekeeping Notifications:** Integrates a Telegram Bot that automatically sends a notification to housekeeping staff the moment a room is confirmed empty, preventing False MUR scenarios.
* **Big Data Analytics:** Implements Apache Spark to query historical data from InfluxDB, generating statistical insights such as average temperature and humidity based on room status, extreme temperature detection, and door activity frequency.
