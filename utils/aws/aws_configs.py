import requests


def get_dynamic_ec2_private_ip():
    """
    Get Aws dynamic EC2 private IP.
    (Pass the function as a List Item in Allowed Hosts)
    """

    ec2_private_ip = None

    try:
        ec2_private_ip = requests.get(
            'http://169.254.169.254/latest/meta-data/local-ipv4',
            timeout=0.01).text
    except requests.exceptions.RequestException:
        pass

    if ec2_private_ip:
        return ec2_private_ip
