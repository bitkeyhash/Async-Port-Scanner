import asyncio

async def scan_port(ip, port):
    """
    Scans a specific port on the given IP address.
    If the port is open, it prints the result.
    """
    try:
        # Attempt to open a connection to the target IP and port
        reader, writer = await asyncio.open_connection(ip, port)
        print(f"[OPEN] Port {port} is open on {ip}")
        writer.close()
        await writer.wait_closed()
    except:
        # Ignore exceptions (closed or inaccessible ports)
        pass

async def scan_ports(ip, start_port, end_port, max_concurrent_tasks=1000):
    """
    Scans a range of ports on the given IP address with a limit on concurrent tasks.
    
    Args:
        ip (str): Target IP address.
        start_port (int): Starting port number.
        end_port (int): Ending port number.
        max_concurrent_tasks (int): Maximum number of concurrent tasks.
    """
    semaphore = asyncio.Semaphore(max_concurrent_tasks)  # Limit concurrent tasks

    async def sem_task(port):
        async with semaphore:
            await scan_port(ip, port)

    # Create tasks for all ports in the range
    tasks = [sem_task(port) for port in range(start_port, end_port + 1)]
    
    # Run all tasks concurrently
    await asyncio.gather(*tasks)

def main():
    """
    Main function to handle user input and initiate the asynchronous port scanner.
    """
    print("Welcome to the Async Port Scanner!")
    
    # Get target IP address from user
    ip = input("Enter the target IP address: ").strip()
    
    # Get port range from user
    try:
        start_port = int(input("Enter the starting port (e.g., 1): ").strip())
        end_port = int(input("Enter the ending port (e.g., 65535): ").strip())
        
        # Validate port range
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range. Ports must be between 1 and 65535.")
        
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"\nScanning IP: {ip} from port {start_port} to {end_port}...\n")
    
    # Run the asynchronous scanner
    asyncio.run(scan_ports(ip, start_port, end_port))
    
    print("\nScan complete!")

if __name__ == "__main__":
    main()
