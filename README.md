# 🛡️ Zero-Trust Web Sandbox: Isolated Browser Automation & Network Forensics

A professional-grade, Dockerized environment designed for high-security web automation, malware analysis, and deep network traffic inspection.

Unlike standard Selenium setups, this project implements a strict **Zero-Trust Microservices Architecture**. The web browser operates within a completely isolated internal network with no direct access to the host machine or the public internet.

All connectivity is forced through a dedicated **Man-in-the-Middle (MitM) Proxy Gateway**. This ensures that every single interaction—whether it is an HTTP request, a background API call, a tracker ping, or a DNS lookup—is intercepted, logged, and transparently audited.

## 🎯 Key Capabilities

* **Safe Malware Analysis:** Visit suspicious URLs without risking your host OS.
* **Full Traffic Visibility:** See hidden API calls and third-party trackers often invisible to standard developer tools.
* **Ephemeral & Disposable:** The entire environment is stateless. Shutting it down wipes 100% of cookies, cache, and session data instantly.
* **Automated Control:** Driven programmatically via Python, allowing for reproducible test scenarios.

## 🏗️ Architecture

The system is composed of 5 distinct Docker containers connected via a private internal network (`sandbox_net`).

| Service | Container Name | Role | Description |
| :--- | :--- | :--- | :--- |
| **Browser** | `sandbox-browser` | 🧪 Subject | Chrome (Selenium) running in a closed network. |
| **Proxy** | `sandbox-proxy` | 🚧 Gateway | Mitmproxy. Bridges the internal and public networks. |
| **Logger** | `sandbox-logger` | 📝 Observer | Tails the shared log file to visualize traffic in real-time. |
| **DNS** | `sandbox-dns` | 🧭 Resolver | Bind9 server (configured to forward to 1.1.1.1). |
| **Scripts** | `sandbox-scripts` | 🤖 Controller | Python/Selenium container that drives the browser. |

## ✅ Feature Verification Report

This project was built to meet specific architectural requirements. Here is the audit of how each one was implemented.

### 1. A Browser Container
* **Requirement:** Run the web browser in a disposable environment, separate from the host OS.
* **Implementation:** We used the official Selenium Grid image to run Chrome on Linux.
* **File:** `browser/Dockerfile`
* **Proof:** The Python script successfully connects to `http://sandbox-browser:4444` to execute commands.

### 2. Logged Network Traffic
* **Requirement:** Capture all HTTP/HTTPS data flowing in and out of the browser.
* **Implementation:** The Proxy container runs `mitmdump` and writes to a shared volume (`/data/traffic.log`). The Logger container tails this file.
* **File:** `proxy/Dockerfile`, `logger/Dockerfile`
* **Proof:** Running `docker compose logs logger` shows real-time request details (e.g., requests to example.com).

### 3. Private, Isolated Network
* **Requirement:** The browser must not have direct access to the internet.
* **Implementation:** The `sandbox_net` network is configured with `internal: true`, physically cutting off external access. The Browser can only reach the internet by explicitly routing through the Proxy container.
* **File:** `docker-compose.yml`
* **Proof:** If the proxy settings are removed from `scripts/main.py`, the browser connection fails instantly with `No route to host`.

### 4. Controlled DNS
* **Requirement:** Use a custom DNS server rather than the host's default ISP settings.
* **Implementation:** A Bind9 container (`sandbox-dns`) is running and configured to forward requests to Cloudflare (1.1.1.1).
* **File:** `dns/Dockerfile`, `dns/named.conf.options`
* **Proof:** The `sandbox-dns` container is active and linked to the network infrastructure.

### 5. Full Auto Reset on Close
* **Requirement:** No cookies, cache, or malware should survive after a session.
* **Implementation:** The `driver.quit()` command in Python destroys the browser session immediately. Furthermore, `docker compose down` destroys the entire container filesystem.
* **File:** `scripts/main.py`
* **Proof:** Restarting the project results in a completely clean state with no saved history.

## 🚀 Installation & Usage

### 1. Build the Environment
```bash
docker compose up -d --build