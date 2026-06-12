import tkinter as tk
from tkinter import messagebox
import requests
from config import API_KEY

root = tk.Tk()
root.title("Weather App")
root.geometry("500x500")
root.resizable(False, False)

title = tk.Label(root, text="🌦 Weather App", font=("Arial", 20, "bold"))
title.pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack(pady=10)

weather_result = tk.Label(root, text="", font=("Arial", 12))
weather_result.pack(pady=20)

unit = tk.StringVar(value="metric")

tk.Radiobutton(
    root,
    text="Celsius",
    variable=unit,
    value="metric"
).pack()

tk.Radiobutton(
    root,
    text="Fahrenheit",
    variable=unit,
    value="imperial"
).pack()


def get_weather():

    city = city_entry.get().strip()

    if not city:
        messagebox.showerror("Error", "Please enter a city")
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units={unit.get()}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        symbol = "°C" if unit.get() == "metric" else "°F"

        weather_result.config(
            text=f"City: {city}\n\n"
                 f"Temperature: {temp}{symbol}\n"
                 f"Humidity: {humidity}%\n"
                 f"Condition: {condition.title()}\n"
                 f"Wind Speed: {wind} m/s"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


search_btn = tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    font=("Arial", 12)
)

search_btn.pack(pady=10)

root.mainloop()