"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import webbrowser


presentation = "Welcome to my data engineering portfolio!\n\nI am a recent graduate with a passion for data and new technologies. After completing a two-year internship/apprenticeship program in data science and engineering, I have gained valuable hands-on experience in collecting, processing, and analyzing large datasets.\n\nMy portfolio showcases a selection of projects that I have completed during my studies and professional experiences. "

texte = "J'ai travaillé chez auchan pendant 1 an et demi j'ai développé des lfux sur gcp avec piwik pro et le tralala"


import reflex as rx

def index() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.avatar(src="https://avatars.githubusercontent.com/u/114836746?v=4", fallback="RX", size="9"),
            rx.divider(size="4",orientation="vertical"),
            rx.heading("François Lenne", size="8", weight="bold",spacing="3"),
            rx.text(presentation,size="3",high_contrast=True,weight="medium",),
            rx.html('<img src="https://skillicons.dev/icons?i=py,r,md,git,gcp,bash,regex,azure" class="mt-4">'),
            direction="column",
            spacing="4",
        ),
        rx.html('<hr class="my-8 border-gray-400 dark:border-gray-500">'),
        rx.box(
            rx.section(
                rx.heading("Projects"),
                padding_left="30px",
            ),
            rx.section(
                rx.heading("Company that I worked for"),
                rx.card(
                    rx.link(
                        rx.flex(
                            rx.avatar(src="https://cdn.worldvectorlogo.com/logos/auchan-51597.svg", size="9"),
                            rx.heading("Data analyst/engineer", size="7", weight="bold", color_scheme="blue"),
                            spacing="7",
                        ),
                    ),
                    size="3",
                    as_child=True,
                    background_image = "linear-gradient(144deg, #FFCCCC, #FF9999 50%, #FF6666)",
                ),
                rx.card(
                    rx.link(
                        rx.flex(
                            rx.avatar(src="https://www.creads.com/wp-content/uploads/2021/05/logo-laposte.png", size="9"),
                            rx.heading("Data analyst/engineer", size="7", weight="bold", color_scheme="blue"),
                            spacing="7",
                        ),
                    ),
                    size="3",
                    as_child=True,
                    background_image = "linear-gradient(144deg, #ffff00, #00008b)",
                ),
                padding_left="30px",
                padding_right="12px",
            ),
            rx.section(
                rx.heading("Contact"),
                rx.text("Feel free to reach out to me! On this channel"),                
                rx.link(rx.button(rx.icon(tag="mail"),"Send me an email !",size="4",radius="large"), href="mailto:francois.lenne59@gmail.com"),
                rx.link(rx.button(rx.icon(tag="linkedin"),"Connect on LinkedIn",size="4",radius="large"), href="https://www.linkedin.com/in/fran%C3%A7ois-lenne-5975b9174/", color_scheme="blue"),
                rx.link(rx.button(rx.icon(tag="github"),"Follow me on Github !",size="4",radius="large",background_image = "linear-gradient(144deg, #000000, #1a1a1a 50%, #333333)", _hover= {"cursor": "pointer"}), href="https://github.com/Francois-lenne"),
                padding_left="30px",
                padding_right="12px",
            ),
            width="100%",
        ),
    )




# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    )
)
app.add_page(index)