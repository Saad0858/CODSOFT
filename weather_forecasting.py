import requests
import tkinter as tk
from tkinter import messagebox
from functools import partial
import tkinter.font as font

def create_window():
    window = tk.Tk()
    window.title("Weather Forecast App")
    window.geometry("700x500+420+160")
    return window
def get_weather_data(location):
    api_key = "02b0fccf051b491120c8480078f7650c"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def parse_weather_data(data):
    if not data:
        return None

    weather_info = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }

    return weather_info

def display_weather_info(weather_info):
    if not weather_info:
        messagebox.showerror("Error", "Weather information not available.")
        return

    listbox.delete(0, tk.END)  # Clear the listbox

    info_str = f"City: {weather_info['city']}"
    listbox.insert(tk.END, info_str)

    info_str = f"Temperature: {weather_info['temperature']}°C"
    listbox.insert(tk.END, info_str)

    info_str = f"Humidity: {weather_info['humidity']}%"
    listbox.insert(tk.END, info_str)

    info_str = f"Description: {weather_info['description']}"
    listbox.insert(tk.END, info_str)

def get_weather(entry):
    location = entry.get()
    weather_data = get_weather_data(location)
    weather_info = parse_weather_data(weather_data)
    display_weather_info(weather_info)

def reset_password():
    city_entry.delete(0, tk.END)
    listbox.delete(0, tk.END)

window = create_window()

frame1 = tk.Frame(window)

label = tk.Label(frame1, text="Weather Forecasting", fg='blue')
label_font = font.Font(size=30, family='comic sans ms')
label['font'] = label_font
label.grid(pady=(10,10), row=1, column=1, columnspan=2)

zip_code = tk.Label(frame1, text="Enter city or zip code")
zip_font = font.Font(size=14, family='comic sans ms')
zip_code['font'] = zip_font
zip_code.grid(pady=(10,10), row=2, column=1)

entry_task_font = font.Font(size=14,family='comic sans ms')
city_entry = tk.Entry(frame1, font=entry_task_font, fg='maroon', width=15)
city_entry.grid(row=2, pady=(20, 10), column=2, padx=(20, 5)) 

btn_font = font.Font(size=14)

result_button = tk.Button(frame1, text="Get Weather", command=partial(get_weather, city_entry), fg='red')
result_button['font'] = btn_font
result_button.grid(row=3, pady=(20, 10), column=1, padx=(20, 5), columnspan=4)

listbox_font = font.Font(size=14, family='comic sans ms')
listbox = tk.Listbox(frame1, height=5, width=22, font=listbox_font)
listbox.grid(row=4, pady=(20, 10), column=1, padx=(20, 5), columnspan=4)

reset_button = tk.Button(frame1, text="Reset", command=reset_password, fg='red')
reset_button['font'] = btn_font
reset_button.grid(row=5, pady=(20, 10), column=1, padx=(20, 5), columnspan=4)

frame1.pack()

window.mainloop()
