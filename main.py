import flet as fl


def open_menu() -> None:
    print(1)


def main(page: fl.Page) -> None:
    page.title = "Scientific Calculator"
    page.window_width = 400
    page.window_center()
    page.window_resizable = False
    page.add(
        controls=fl.Row(
            [
                fl.Text("Scientific Calculator", size=25, color=fl.colors.WHITE),
                fl.Container(width=page.window_width),
                fl.IconButton(
                    icon=fl.Icon(fl.icons.GRID_3X3_ROUNDED, size=15), on_click=open_menu
                ),
            ]
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
