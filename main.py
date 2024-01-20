import flet as fl
from model import buttons

input_row: fl.TextField = fl.TextField(value="0", read_only=True)


def open_menu(event: fl.TapEvent) -> None:
    ...


def evaluate(event: fl.TapEvent, page: fl.Page) -> None:
    if event.control.text == "=":
        input_row.value = str(eval(input_row.value))
    elif event.control.text == "AC":
        input_row.value = "0"
    else:
        input_row.value = input_row.value.lstrip("0") + event.control.text.replace(
            "+/_", "-"
        ).replace("X", "*").replace("÷", "/")

    print(input_row.value)

    page.update()


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

    page.add(input_row)

    for tier in buttons:
        page.add(
            fl.Row(
                expand=True,
                alignment=fl.MainAxisAlignment.CENTER,
                controls=[
                    fl.TextButton(text=button, on_click=lambda e: evaluate(e, page))
                    for button in tier
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
