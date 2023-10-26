from netmiko import ConnectHandler

# Define device information
device = {
    'device_type': 'juniper_junos',
    'ip': 'your_router_ip',
    'username': 'your_username',
    'password': 'your_password',
}

# Connect to the device
try:
    net_connect = ConnectHandler(**device)
    print("Connected to the device.")

    # Enter configuration mode
    net_connect.config_mode()

    # Define the configuration command you want to change
    config_command = "set system login user new_user class super-user"

    # Send the configuration command
    output = net_connect.send_config_set(config_command)
    print(f"Configuration command sent: {output}")

    # Save the configuration
    save_output = net_connect.save_config()
    print(f"Configuration saved: {save_output}")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Disconnect from the device
    net_connect.disconnect()
    print("Disconnected from the device.")
