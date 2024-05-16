import requests
from bs4 import BeautifulSoup

def trace_phone_number(phone_number):
    url = f'https://www.searchyellowdirectory.com/reverse-phone/{phone_number}/'

    try:
        response = requests.get(url, timeout=10)  # Add timeout parameter
        response.raise_for_status()  # Raise an error if the response is not successful

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extracting location and carrier information
        location = soup.find('span', class_='region')
        carrier = soup.find('span', class_='carrier')

        if location and carrier:
            print(f"Location: {location.text.strip()}")
            print(f"Carrier: {carrier.text.strip()}")

        else:
            print("Unable to trace location.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    phone_number = input("Enter the phone number to trace: ")
    trace_phone_number(phone_number)
