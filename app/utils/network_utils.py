import socket
import time

def get_network_status(targets):
    results = {}
    for host, port in targets:
        start = time.time()
        try:
            with socket.create_connection((host, port), timeout=1.0):
                latency = time.time() - start
                results[(host, port)] = {"status": True, "latency": latency}
        except Exception:
            results[(host, port)] = {"status": False, "latency": None}
    return results
