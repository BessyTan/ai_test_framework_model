Python Test Automation Framework for AI Pipelines

Automates validation of ML pipelines and network device testing using PyTest in a Dockerized environment.
Runs model accuracy, data integrity, inference latency tests, and network connectivity/latency validation.

Folder Structure
ai_test_framework/
├── app/                      # Project source code
├── network-sim/              # Network simulation scripts
├── reports/                  # Test HTML reports
├── logs/                     # Logs for network tests
├── tests/                    # PyTest test cases
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

Setup
1. Install dependencies locally (optional)
pip install -r requirements.txt

2. Build and run Docker containers
export DOCKER_BUILDKIT=1
docker-compose up --build


test-framework container: Runs PyTest for AI pipeline tests.

network-sim container: Simulates network devices for connectivity and latency testing.

Run Tests
AI Pipeline Tests
docker exec -it python_test_framework pytest tests/test_pipeline.py --html=reports/pipeline_report.html --self-contained-html

Network Device Tests
docker exec -it python_test_framework pytest tests/test_network_devices.py --html=reports/network_report.html --self-contained-html

Network Device Testing Module

This module validates connectivity, latency, and port availability using Python’s socket library—simulating lab-style network switch testing.

Module Overview
File	Purpose
utils/network_utils.py	Functions to "ping" devices/services and measure latency
tests/test_network_devices.py	PyTest suite automating connectivity and latency tests
Example Test
network_targets = [
    ("127.0.0.1", 80),
    ("localhost", 22),
]

def test_network_device_connectivity():
    results = get_network_status(network_targets)
    for target, info in results.items():
        assert info["status"], f"{target} is unreachable"
        assert info["latency"] is None or info["latency"] < 1.0, f"{target} latency too high"

Reports & Logs

HTML reports are generated in reports/:

pipeline_report.html for AI pipeline tests

network_report.html for network tests

Network test logs are saved in logs/.

Key Benefits

Demonstrates Python-based test automation for AI pipelines and network devices.

Uses PyTest framework consistently for both layers of automation.

Docker ensures reproducibility across machines and CI/CD pipelines.

Easily extensible for real network devices via SSH, SNMP, or REST APIs.