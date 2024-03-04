"""Welcome to Reflex! This file create a counter app."""


import reflex as rx

def on_button_clicked():
    print("Button clicked!")

app = rx.App()

window = rx.Window(app, title="Reflex Example")
button = rx.Button(window, text="Click me!", on_clicked=on_button_clicked)

app.run()