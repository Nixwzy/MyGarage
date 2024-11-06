import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

translations = {
    'pt': {
        'button_vehicles': 'Veículos',
        'button_register': 'Registrar Veículo',
        'vehicles_info': 'Aqui serão listados os veículos armazenados.',
        'register_info': 'Aqui será possível registrar um novo veículo.',
    },
    'en': {
        'button_vehicles': 'Vehicles',
        'button_register': 'Register Vehicle',
        'vehicles_info': 'Here the stored vehicles will be listed.',
        'register_info': 'Here you can register a new vehicle.',
    }
}

def show_vehicles(lang):
    messagebox.showinfo(translations[lang]['button_vehicles'], translations[lang]['vehicles_info'])

def register_vehicle(lang):
    messagebox.showinfo(translations[lang]['button_register'], translations[lang]['register_info'])

def main():
    root = tk.Tk()
    root.title("MyGarage v0.0.1")
    root.geometry("600x900")
    root.overrideredirect(False)
    root.resizable(False, False)

    top_bar = tk.Frame(root, bg="#1C1C1E", height=80)
    top_bar.pack(fill=tk.X)

    button_frame = tk.Frame(top_bar, bg="#1C1C1E")
    button_frame.pack(expand=True)

    button_vehicles = tk.Button(button_frame, text=translations['pt']['button_vehicles'], command=lambda: show_vehicles('pt'), bg="#1C1C1E", fg="white", relief="flat", height=2, width=15)
    button_vehicles.pack(side=tk.LEFT, padx=20)

    button_register = tk.Button(button_frame, text=translations['pt']['button_register'], command=lambda: register_vehicle('pt'), bg="#1C1C1E", fg="white", relief="flat", height=2, width=15)
    button_register.pack(side=tk.LEFT, padx=20)

    vehicle_list_frame = tk.Frame(root, bg="#1C1C1E")
    vehicle_list_frame.pack(expand=True, fill=tk.BOTH)

    label_vehicles = tk.Label(vehicle_list_frame, text="Lista de Veículos", bg="#1C1C1E", fg="white", font=("Helvetica", 16))
    label_vehicles.pack(pady=10)

    vehicles = [
        {
            "name": "Toyota Corolla",
            "year": 2022,
            "color": "Preto",
            "plate": "XYZ-1234",
            "price": "R$ 50.000",
            "condition": "pipipi",
            "image": "MyGarage/images/catIdle1.png"
        },
        {
            "name": "Honda CB500",
            "year": 2022,
            "color": "Preto",
            "plate": "XYZ-1234",
            "price": "R$ 50.000",
            "condition": "pipipi",
            "image": "MyGarage/images/catIdle1.png"
        },
    ]

    for vehicle in vehicles:
        vehicle_frame = tk.Frame(vehicle_list_frame, bg="#2C2C2E", bd=1, relief=tk.SOLID, padx=10, pady=10)
        vehicle_frame.pack(fill=tk.X, padx=10, pady=5)

        vehicle_image = Image.open(vehicle["image"])
        vehicle_image = vehicle_image.resize((100, 100), Image.LANCZOS)
        vehicle_image_tk = ImageTk.PhotoImage(vehicle_image)
        image_label = tk.Label(vehicle_frame, image=vehicle_image_tk, bg="#2C2C2E")
        image_label.image = vehicle_image_tk
        image_label.pack(side=tk.LEFT, padx=5, pady=5)

        vehicle_name_label = tk.Label(vehicle_frame, text=f"{vehicle['name']} - {vehicle['year']}", bg="#2C2C2E", fg="white", font=("Helvetica", 14))
        vehicle_name_label.pack(pady=5)

        specifications_label = tk.Label(vehicle_frame, text=f"Cor: {vehicle['color']}\nPlaca: {vehicle['plate']}\nPreço avaliado: {vehicle['price']}\nCondição: {vehicle['condition']}", bg="#2C2C2E", fg="white", font=("Helvetica", 12))
        specifications_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
