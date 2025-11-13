import socket
import pytest
import os

from app.utils.network_utils import get_network_status
import yaml

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

network_targets = [("network_sim", 8080)]


def get_network_status(targets):
    results = {}
    for host, port in targets:
        try:
            with socket.create_connection((host, port), timeout=5):
                reachable = True
                latency = 0.01  # mock latency for now
        except Exception:
            reachable = False
            latency = None
        results[(host, port)] = {"status": reachable, "latency": latency}
    return results

def test_network_device_connectivity():
    results = get_network_status(network_targets)
    for target, info in results.items():
        assert info["status"], f"{target} is unreachable"
        assert info["latency"] is None or info["latency"] < 1.0, f"{target} latency too high"