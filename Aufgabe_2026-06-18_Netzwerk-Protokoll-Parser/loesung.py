import os
import ipaddress
from datetime import datetime
from typing import List, Dict


def parse_network_log(log_file_path: str) -> List[Dict]:
    log_data = []
    with open(log_file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Leere Zeile überspringen

            fields = line.split(";")
            if len(fields) != 7:
                continue  # Zeile mit falscher Anzahl an Feldern überspringen

            (
                timestamp_str,
                source_ip_str,
                destination_ip_str,
                protocol,
                port_str,
                size_str,
                status,
            ) = fields

            # Validierung und Typkonvertierung
            try:
                timestamp = datetime.strptime(
                    timestamp_str, "%Y-%m-%d %H:%M:%S"
                )
                source_ip = ipaddress.IPv4Address(source_ip_str)
                destination_ip = ipaddress.IPv4Address(destination_ip_str)
                port = int(port_str)
                size = int(size_str)
                if protocol not in ["TCP", "UDP"]:
                    continue  # Ungültiges Protokoll, Zeile überspringen

                if status not in ["OK", "ERROR", "WARNING"]:
                    continue  # Ungültiger Status, Zeile überspringen

                log_data.append(
                    {
                        "timestamp": timestamp,
                        "source_ip": str(source_ip),
                        "destination_ip": str(destination_ip),
                        "protocol": protocol,
                        "port": port,
                        "size": size,
                        "status": status,
                    }
                )
            except (ValueError, ipaddress.AddressValueError):
                continue  # Fehlerhafte Zeile überspringen

    return log_data


def filter_by_protocol(log_data: List[Dict], protocol: str) -> List[Dict]:
    return [entry for entry in log_data if entry["protocol"] == protocol]


def get_statistics(log_data: List[Dict]) -> Dict:
    total_packets = len(log_data)
    protocol_distribution = {}
    total_bytes = 0
    error_packets = 0

    for entry in log_data:
        protocol = entry["protocol"]
        protocol_distribution[protocol] = (
            protocol_distribution.get(protocol, 0) + 1
        )
        total_bytes += entry["size"]
        if entry["status"] == "ERROR":
            error_packets += 1

    return {
        "total_packets": total_packets,
        "protocol_distribution": protocol_distribution,
        "total_bytes": total_bytes,
        "error_packets": error_packets,
    }
