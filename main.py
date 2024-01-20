import flet as fl
from model import buttons


def open_menu(event: fl.TapEvent) -> None:
    print(event)


def main(page: fl.Page) -> None:
    page.title = "Scientific Calculator"
    page.window_width = 400
    page.window_center()
    page.window_resizable = False
    page.add(
        fl.Row(
            alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                fl.Text("Scientific Calculator", size=18, color=fl.colors.WHITE),
                fl.IconButton(
                    icon=fl.icons.GRID_GOLDENRATIO, icon_size=15, on_click=open_menu
                ),
            ],
        )
    )

    page.add(fl.TextField(data="0", read_only=True))

    for tier in buttons:
        page.add(
            fl.Row(
                expand=True,
                alignment=fl.MainAxisAlignment.CENTER,
                controls=[
                    fl.TextButton(text=button, on_click=open_menu) for button in tier
                ],
            )
        )

    page.update()


if __name__ == "__main__":
    fl.app(
        target=main,
        assets_dir="assets/",
        name="Scientific Calculator",
        use_color_emoji=True,
        view=fl.AppView.FLET_APP,
    )
