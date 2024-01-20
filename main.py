import flet as fl


def main(page: fl.Page) -> None:
    ...


if __name__ == "__main__":
    fl.app(
        target=main,
        assets_dir="assets/",
        title="Scientific Calculator",
        name="Scientific Calculator",
        use_color_emoji=True,
        view=fl.AppView.FLET_APP,
    )
