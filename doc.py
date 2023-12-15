import requests
import tkinter as tk

def get_exchange_rates(base_currency):
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your API key
    url = f'https://api.example.com/exchangerates/{base_currency}?apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['rates']

def update_exchange_rates():
    base_currency = base_currency_var.get()
    rates = get_exchange_rates(base_currency)
    result_text.delete(1.0, tk.END)  # Clear previous rates
    for currency, rate in rates.items():
        result_text.insert(tk.END, f'{currency}: {rate}\n')

# Create GUI
root = tk.Tk()
root.title("Real-Time Currency Exchange Rates")

base_currency_label = tk.Label(root, text="Base Currency:")
base_currency_label.pack()

base_currency_var = tk.StringVar()
base_currency_entry = tk.Entry(root, textvariable=base_currency_var)
base_currency_entry.pack()

update_button = tk.Button(root, text="Update Rates", command=update_exchange_rates)
update_button.pack()

result_text = tk.Text(root, height=10, width=30)
result_text.pack()

# Start GUI event loop
root.mainloop()