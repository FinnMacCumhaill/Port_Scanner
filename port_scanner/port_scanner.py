import socket
import concurrent.futures
import sys
import colorama
from colorama import init
import textwrap
# author:FinnMacCumhaill
# A program that performs a port scan, displaying the ports, services, and banner information on the network.
# Highlighting the banner info in green text, and open ports in red.
# Improved the format of the banner text, in the port scan.
# To enable the use of the escape chars in Windows and not just Linux and macOS
init(strip=False)
# ASCII Escape Chars
RED, GREEN, RESET = "\033[91m","\033[92m","\033[0m"

# A function to format the results of the port scan.
def format_port_results(results):
    # Initializes a string to hold the formatted results.
    formatted_results = "Port Scan Results:\n"
    # Adds a header line with columns for Port, Service, and Status.​
    formatted_results += "{:<8} {:20} {:<10}\n".format("Port", "Service", "Status")
    # Adds a separator line.​
    formatted_results += '-' * 60 + "\n"
    # Iterates over the scan results.
    for port, service, banner, status in results:
        # Checks if the port is open.
        if status:
            # Adds the port, service, and the status to the results string, coloured red for open ports.
            formatted_results += f"{RED}{port:<8} {service:<20} {'Open':<10}{RESET}\n"
        # Checks if a banner was retrieved.
        if banner:
            # Cleans up the garbage chars, that appears in the output of the port scan.
            clean_banner = banner.strip().replace(", , ,", "").replace(", ,","").rstrip(',').replace('/t', '')
            # Splits the banner into lines.
            banner_lines = clean_banner.split('\n')
            # Iterates over the banner lines.
            for line in banner_lines:
                # To successfully wrap the banner lines for improved formatting in our port scan results.
                wrapped_lines = textwrap.wrap(line, width=60)
                # Iterates the initialiser i , wrapped and enumerate the wrapped banner lines.
                for i, wrapped in enumerate(wrapped_lines):
                    # Checks if initialiser i is equal to zero.
                    if i == 0:
                        # Adds the following "└─" char.
                        prefix = "└─ "
                    # In all other cases.
                    else:
                        # Adds 3 spaces.
                        prefix = "   "
                    # Adds each line of the banner to the results string, colored green.
                    formatted_results += f"{GREEN}{'':<9}{prefix}{wrapped}{RESET}\n"
    # Returns the formatted results string.
    return formatted_results

# A function to retrieve the banner from a socket.
def get_banner(sock):
    # Starts a try block to handle potential errors.
    try:
        # Sets a 1-second timeout for the socket.
        sock.settimeout(1)
        # Receives up to 1024 bytes from the socket, 
        # Decodes the bytes to a string, and removes any leading or trailing whitespace.
        banner = sock.recv(1024).decode().strip()
        # Returns the banner.
        return banner
    # Catches any exceptions that occur.
    except:
        # Returns an empty string if an exception occurs.
        return ""

# A function to scan a single port based on the target IP Address.
def scan_port(target_ip, port):
    # Starts a try block to handle potential errors.
    try:
        # Creates a new TCP socket.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Sets a 1-second timeout for the socket.
        sock.settimeout(1)
        # Attempts to connect to the target IP Address and port.
        # Returns 0 if the connection is successful.
        result = sock.connect_ex((target_ip, port))
        # Checks if the connection was successful.
        if result == 0:
            # Starts a try block to handle potential errors.
            try:
                # Attempts to get the service name for the port.
                service = socket.getservbyport(port, 'tcp')
            # Catches any exceptions that occur.
            except:
                # Sets the service name to 'Unknown' if an exception occurs.  
                service = 'Unknown'
            # Retrieves the banner from the socket.    
            banner = get_banner(sock)
            # Returns the port, service, banner, and the status indicating the port is open.
            return port, service, banner, True
        # If the connection was not successful.
        else:
            # Returns the port, empty strings for the service, and banner, and a status indicating the port is closed.
            return port, "", "", False
    # Catches any exceptions that occur.
    except:
        # Returns the port, empty strings for the service, and banner, and a status indicating the port is closed.
        return port, "", "", False
    # Ensures the following block always executes.
    finally:
        # Closes the socket.
        sock.close()

# A function to scan a range of ports on the target host.
def port_scan(target_host, start_port, end_port):
    # Resolves the target host to an IP address.
    target_ip = socket.gethostbyname(target_host)
    # Prints a message indicating the start of the scan.
    print(f"Starting scan on host: {target_ip}")
    # Initializes an empty list to store the scan results.
    results = []
    # Creates a thread pool executor with a maximum of 400 threads.
    with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
        # Submits tasks to scan each port in the specified range and stores the futures in a dictionary.
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}
        # Calculates the total number of ports to scan.
        total_ports = end_port - start_port + 1
        # Iterates over the completed futures.
        for i, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            # Retrieves the result from the future.
            port, service, banner, status = future.result()
            # Appends the result to the results list.
            results.append((port, service, banner, status))
            # Updates the progress on the same line
            sys.stdout.write(f"\rProgress: {i}/total_ports ports scanned")
            # Flushes the output buffer to ensure the progress message is displayed.
            sys.stdout.flush()

    # Writes a newline to move to the next line.
    sys.stdout.write("\n")
    # Prints the formatted scan results.
    print(format_port_results(results))

# Ensures that the following code block runs only if the script is executed directly.
if __name__ == '__main__':
    # Prompts the user to enter the target IP address or hostname.
    target_host = input("Enter your target ip: ")
    # Prompts the user to enter the starting port number.
    start_port= int(input("Enter the start port: "))
    # Prompts the user to enter the ending port number.
    end_port = int(input("Enter end port: "))
    # Calls the port_scan function with the provided arguments.
    port_scan(target_host, start_port, end_port)