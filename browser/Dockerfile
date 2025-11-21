# Use the official Selenium Chrome image
FROM selenium/standalone-chrome:latest

# Switch to root to install updates if needed, then back to user
USER root
RUN apt-get update && apt-get clean
USER seluser

# Expose the Selenium port
EXPOSE 4444