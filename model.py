from typing import Dict, List, Any
from flet import colors


buttons: List[Dict[str, Any]] = [
    {
        "AC": {
            "background_color": colors.GREY,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 1,
            "column_index": 1,
        },
        "+/_": {
            "background_color": colors.GREY,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 1,
            "column_index": 2,
        },
        "%": {
            "background_color": colors.GREY,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 1,
            "column_index": 3,
        },
        "÷": {
            "background_color": colors.BLUE,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 1,
            "column_index": 4,
        },
    },
    {
        "7": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 2,
            "column_index": 1,
        },
        "8": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 2,
            "column_index": 2,
        },
        "9": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 2,
            "column_index": 3,
        },
        "X": {
            "background_color": colors.BLUE,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 2,
            "column_index": 4,
        },
    },
    {
        "4": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 3,
            "column_index": 1,
        },
        "5": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 3,
            "column_index": 2,
        },
        "6": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 3,
            "column_index": 3,
        },
        "-": {
            "background_color": colors.BLUE,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 3,
            "column_index": 4,
        },
    },
    {
        "1": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 4,
            "column_index": 1,
        },
        "2": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 4,
            "column_index": 2,
        },
        "3": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 4,
            "column_index": 3,
        },
        "+": {
            "background_color": colors.BLUE,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 4,
            "column_index": 4,
        },
    },
    {
        "0": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 5,
            "column_index": 1,
        },
        ".": {
            "background_color": colors.GREY_400,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 5,
            "column_index": 3,
        },
        "=": {
            "background_color": colors.BLUE,
            "text_color": colors.WHITE,
            "places": 1,
            "row_index": 5,
            "column_index": 4,
        },
    },
]
