import csv

from schemas.schemas import IPInfo


def ip_to_int(ip):
    """
    Convert a dot-decimal format IP address to its decimal representation.
    """
    octets = ip.split('.')
    decimal_ip = sum(int(octet) * (256 ** i) for i, octet in enumerate(reversed(octets)))
    return decimal_ip


def prepare_ip_key(ip):
    """
    Because all data is an IP range from ...0 to ...255, we can just use the first 3 octets to find the ip range.
    E.g. data for 97.26.57.15 would be located in the 97.26.57.0 key
    """
    ip_start_range = '.'.join(ip.split('.')[:3] + ["0"])
    print(ip_start_range)
    decimal_ip = ip_to_int(ip_start_range)
    return str(decimal_ip)


class IPDatabase:
    def __init__(self, filepath='artifacts/IP2LOCATION-LITE-DB11.CSV'):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.db = list(csv.reader(file))

        # using the first column as the key, makes it easier & faster to find the data
        # loops through the data once, and then we can just use the key to find the data
        self.data = {
            row[0]: row
            for row in self.db
        }

    async def get_ip_info(self, ip):
        ip_key = prepare_ip_key(ip)
        data = self.data.get(ip_key, None)
        if not data:
            return None

        return IPInfo(
            ip=ip,
            country_key=data[2],
            country=data[3],
            region=data[4],
            city=data[5],
            latitude=data[6],
            longitude=data[7],
            zip_code=data[8],
            timezone=data[9],
        )
