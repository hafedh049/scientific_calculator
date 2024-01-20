import flet as fl


def open_menu(event: fl.TapEvent) -> None:
    print(1)


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
    page.add(
        fl.TextField(data="0"),
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
