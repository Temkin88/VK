import socket
import re
from pyvkteamsclient.client import DesktopClient
import ipaddress


def get_user_ip_address_env_api_subnet(user: DesktopClient) -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = user.api_url
    pattern = r"http[s]{0,1}:[\/]{2}"
    host = re.sub(pattern, "", host)
    ipaddress_host = socket.gethostbyname(host)
    s.connect((ipaddress_host, 80))
    ip_address_of_client = s.getsockname()[0]
    return ip_address_of_client


def check_ip_addr_in_trusted_subnets(ip_address_of_client: str, ip_address_of_trusted_subnets: list[str]) -> bool:
    for ip_address_of_trusted_subnet in ip_address_of_trusted_subnets:
        try:
            ip_address = ipaddress.ip_address(ip_address_of_client)
            network = ipaddress.ip_network(ip_address_of_trusted_subnet, strict=False)
            if ip_address in network:
                return True
        except ValueError as e:
            Exception(f"Error: Invalid IP address or subnet format: {e}")
            return False
    return False


def check_user_ip_addr_in_trusted_subnets(user: DesktopClient, ip_address_of_trusted_subnets: list[str]) -> bool:
    client_ip_address = get_user_ip_address_env_api_subnet(user)
    return check_ip_addr_in_trusted_subnets(client_ip_address, ip_address_of_trusted_subnets)
