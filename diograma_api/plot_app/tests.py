import requests
import os


url = 'https://25e1-213-230-78-164.ngrok-free.app/api/plot/'
data = {"x_values": [1,4,10,14,60], "y_values": [30, 60, 50,4,14]}


response = requests.post(url, json=data)


print(f"Response Status Code: {response.status_code}")


if response.status_code == 200 and 'image/png' in response.headers.get('Content-Type', ''):

    file_name = f"plot_x{data['x_values'][0]}_y{data['y_values'][0]}.png"


    try:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"Plot saved as {file_name}")
    except Exception as e:
        print(f"Error saving the plot: {e}")
else:
    print("Error: The response is not a valid image or there was an issue with the request.")
    print(f"Response Content: {response.text}")
