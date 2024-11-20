import requests
import struct

def STMconnect(esp32IP, data):
    """
    Communicates with an ESP32 device using HTTP POST requests.
    
    :param esp32IP: IP address of the ESP32 device.
    :param data: Binary file or data to send.
    """
    url = f"http://{esp32IP}/"

    try:
        response = requests.post(url, data = data)
        print(f"Response status code: {response.status_code}")
        print("Response text:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")