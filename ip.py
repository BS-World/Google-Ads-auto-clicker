import subprocess
import time
import logging

def change_ip(interface, new_ip, subnet_mask='255.255.255.0', gateway='1.1.1.1'):
    try:
        # Command to change IP address
        command = [
            'netsh', 'interface', 'ip', 'set', 'address',
            interface, 'static', new_ip, subnet_mask, gateway
        ]
        subprocess.run(command, check=True)
        logging.info(f"Successfully changed IP to {new_ip}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error changing IP to {new_ip}: {e}")

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    interface = 'Local Area Connection* 4'  # Use the exact interface name
    ip_base = '192.164.1.'  # Base IP address for changing
    subnet_mask = '255.255.255.0'
    gateway = '1.1.1.1'
    
    for i in range(1, 255):
        new_ip = f"{ip_base}{i}"
        change_ip(interface, new_ip, subnet_mask, gateway)
        time.sleep(120)  # Sleep for 120 seconds (2 minutes)

if __name__ == '__main__':
    main()
