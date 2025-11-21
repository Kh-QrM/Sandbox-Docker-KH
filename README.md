🛡️ Microservices Web Testing Sandbox

A fully isolated, multi-container environment for secure web automation and traffic analysis.

This project uses a Microservices Architecture to separate concerns. The browser runs in a strictly internal network with zero direct internet access. It must pass through a specific Proxy Gateway to reach the outside world, ensuring 100% of traffic is logged and inspected.

🏗️ Architecture

The system is composed of 5 distinct Docker containers connected via a private internal network (sandbox_net).

Service

Container Name

Role

Description

Browser

sandbox-browser

🧪 Subject

Chrome (Selenium) running in a closed network.

Proxy

sandbox-proxy

🚧 Gateway

Mitmproxy. Bridges the internal and public networks.

Logger

sandbox-logger

📝 Observer

Tails the shared log file to visualize traffic in real-time.

DNS

sandbox-dns

🧭 Resolver

Bind9 server (configured to forward to 1.1.1.1).

Scripts

sandbox-scripts

🤖 Controller

Python/Selenium container that drives the browser.

✅ Feature Verification Report

This project was built to meet specific architectural requirements. Here is the audit of how each one was implemented.

1. A Browser Container

Requirement: Run the web browser in a disposable environment, separate from the host OS.

Implementation: We used the official Selenium Grid image to run Chrome on Linux.

File: browser/Dockerfile

Proof: The Python script successfully connects to http://sandbox-browser:4444 to execute commands.

2. Logged Network Traffic

Requirement: Capture all HTTP/HTTPS data flowing in and out of the browser.

Implementation: The Proxy container runs mitmdump and writes to a shared volume (/data/traffic.log). The Logger container tails this file.

File: proxy/Dockerfile, logger/Dockerfile

Proof: Running docker compose logs logger shows real-time request details (e.g., requests to example.com).

3. Private, Isolated Network

Requirement: The browser must not have direct access to the internet.

Implementation: The sandbox_net network is configured with internal: true, physically cutting off external access. The Browser can only reach the internet by explicitly routing through the Proxy container.

File: docker-compose.yml

Proof: If the proxy settings are removed from scripts/main.py, the browser connection fails instantly with No route to host.

4. Controlled DNS

Requirement: Use a custom DNS server rather than the host's default ISP settings.

Implementation: A Bind9 container (sandbox-dns) is running and configured to forward requests to Cloudflare (1.1.1.1).

File: dns/Dockerfile, dns/named.conf.options

Proof: The sandbox-dns container is active and linked to the network infrastructure.

5. Full Auto Reset on Close

Requirement: No cookies, cache, or malware should survive after a session.

Implementation: The driver.quit() command in Python destroys the browser session immediately. Furthermore, docker compose down destroys the entire container filesystem.

File: scripts/main.py

Proof: Restarting the project results in a completely clean state with no saved history.

🚀 Installation & Usage

1. Build the Environment

docker compose up -d --build


2. Run the Test Script

To execute the Python automation script:

docker compose exec scripts python main.py


Expected Output: Success! Page Title: Example Domain

3. View Traffic Logs

docker compose logs -f logger


📂 Project Structure

Sandbox-Docker-KH/
├── docker-compose.yml    # The blueprint connecting all services
├── browser/              # Chrome + Selenium
├── proxy/                # Mitmproxy (Runs as Root to write logs)
├── logger/               # Alpine Linux to tail logs
├── dns/                  # Bind9 configuration
└── scripts/              # Python automation logic


🧹 Clean Up

To stop the sandbox and wipe all data:

docker compose down --volumes
