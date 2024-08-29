import flet as ft
from views.views import (Sobre, Tecnologias, Projetos)


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.all(0)
    page.fonts = {
        "RobotoBold": r"\fonts\Roboto-Bold.ttf",
        "RobotoReular": r"\fonts\Roboto-Regular.ttf",
    }

    text_style = ft.TextStyle(
        color=ft.colors.WHITE,
        size=20,
        font_family="RobotoBold",
        weight=ft.FontWeight.W_300
    )

    menu_lateral = ft.Container(
        content=ft.Column(
            controls=[
                ft.CircleAvatar(
                    foreground_image_src=r"/eu.jpg",
                    width=200,
                    height=200
                ),
                ft.TextButton(
                    content=ft.Text(
                        value="SOBRE", 
                        style=text_style,
                    ),
                    on_click=lambda _: scroll_to_key("Sobre")
                ),
                ft.TextButton(
                    content=ft.Text(
                        value="TECNOLOGIAS", 
                        style=text_style
                    ),
                    on_click=lambda _: scroll_to_key("Tecnologias")
                ),
                ft.TextButton(
                    content=ft.Text(
                        value="PROJETOS", 
                        style=text_style
                    ),
                    on_click=lambda _: scroll_to_key("Projetos")
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor="#005ac0",
        width=300,
        expand=2,
    )

    pagina_principal = ft.Column(
        controls=[
            Sobre(page.height),
            Tecnologias(page.height),
            Projetos(page.height),
        ],
        scroll=ft.ScrollMode.ADAPTIVE,
        spacing=0,
        expand=10,
    )

    def scroll_to_key(key):
        pagina_principal.scroll_to(key=key, duration=1000)
    
    page.add(ft.Row(
        controls=[
            menu_lateral,
            pagina_principal
        ],
        spacing=0,
        expand=True
    ))





ft.app(main, view=ft.AppView.WEB_BROWSER)
