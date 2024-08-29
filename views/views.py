import flet as ft


class Sobre(ft.Container):
    def __init__(self, height):
        super().__init__(height=height)
        self.alignment=ft.alignment.top_left
        self.bgcolor="#00d0ff"
        self.key="Sobre"
        self.padding=ft.padding.only(left=50)
        self.content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value="Tainan Ramos",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=50,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    )
                ),
                ft.Text(
                    value="tainan@trsolucoes.com.br",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=20,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    )
                ),
                ft.Text(
                    value=("Sou desenvolvedor RPA (Automação de Processos Robóticos), com foco em UiPath e Python. "
                           "Minha trajetória inclui sólida experiência em mapeamento de processos, lógica de programação e resolução de problemas, sempre com o objetivo de otimizar a eficiência operacional. "
                           "Além do UiPath, possuo habilidades em Business Process Management (BPM), que aplico para melhorar continuamente os processos. "
                           "Também sou proficiente em bancos de dados e linguagens como JavaScript, VB.NET, Node.js, Python, além de ser familiar com o REFramework e as funcionalidades avançadas do UiPath Orchestrator."),
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=20,
                        font_family="RobotoRegular",
                        weight=ft.FontWeight.W_300
                    )
                ),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            content=ft.Image(src="https://img.icons8.com/ios-filled/50/github.png", color=ft.colors.WHITE),
                            on_click=lambda _: self.page.launch_url("https://github.com/tainanramos")
                        ),
                        ft.IconButton(
                            content=ft.Image(src="https://img.icons8.com/ios-filled/50/linkedin.png", color=ft.colors.WHITE),
                            on_click=lambda _: self.page.launch_url("https://www.linkedin.com/in/tainan-ramos/")
                        ),
                    ]
                )
            ]
        )


class Tecnologias(ft.Container):
    def __init__(self, height):
        super().__init__(height=height)
        self.alignment=ft.alignment.top_left
        self.bgcolor="#00d0ff"
        self.key="Tecnologias"
        self.padding=ft.padding.only(left=50)
        self.content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value="Tecnologias",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=50,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    )
                ),
                ft.Text(
                    value="- UiPath",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=20,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    ),
                ),
                ft.Text(
                    value="- Python",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=20,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    ),
                ),
                ft.Text(
                    value="- SQL",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=20,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    ),
                ),
                ft.Text(
                    value="- JavaScript",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=20,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    ),
                ),
                ft.Text(
                    value="- REFramework",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=20,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    ),
                ),
                ft.Text(
                    value="- UiPath Orchestrator",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=20,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    ),
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Image(src="https://img.icons8.com/color/50/uipath.png", color=ft.colors.WHITE),
                            on_hover=remove_branco
                        ),
                        ft.Container(
                            content=ft.Image(src="https://img.icons8.com/fluency/50/python.png", color=ft.colors.WHITE),
                            on_hover=remove_branco
                        ),
                        ft.Container(
                            content=ft.Image(src="https://img.icons8.com/ios/50/javascript--v1.png", color=ft.colors.WHITE),
                            on_hover=remove_branco
                        ),
                        ft.Container(
                            content=ft.Image(src="https://img.icons8.com/ios/50/sql.png", color=ft.colors.WHITE),
                            on_hover=remove_branco
                        ),
                    ]
                )
            ]
        )


class Projetos(ft.Container):
    def __init__(self, height):
        super().__init__(height=height)
        self.alignment=ft.alignment.top_left
        self.bgcolor="#00d0ff"
        self.key="Projetos"
        self.padding=ft.padding.only(left=50)
        self.content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value="Carregando...",
                    style=ft.TextStyle(
                        color=ft.colors.WHITE,
                        size=50,
                        font_family="RobotoBold",
                        weight=ft.FontWeight.W_300
                    )
                )
            ]
        )
    
def remove_branco(e):
    if(e.data == "true"):
        e.control.content.color = None
    else:
        e.control.content.color = ft.colors.WHITE
    
    e.control.update()
