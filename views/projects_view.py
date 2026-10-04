from cProfile import label
from dataclasses import dataclass

import flet as ft
import flet_datatable2 as ftd

from services.projectService import ProjectService


def main(page: ft.Page, project_service: ProjectService):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    files = project_service.get_all_files()

    def handle_row_selection_change(e: ft.Event[ftd.DataRow2]) -> None:
        e.control.selected = not e.control.selected
        e.control.update()

    def sort_column(e: ft.DataColumnSortEvent) -> None:
        sorters = [
            lambda d: d.name.lower(),
            lambda d: d.modified_at
        ]
        files.sort(key=sorters[e.column_index], reverse=not e.ascending)
        table.rows = get_data_rows(files)
        table.sort_column_index = e.column_index
        table.sort_ascending = e.ascending
        table.update()

    def get_data_columns() -> list[ftd.DataColumn2]:
        return [
            ftd.DataColumn2(
                label=ft.Text("Name"),
                size=ftd.DataColumnSize.L,
                on_sort=sort_column,
                heading_row_alignment=ft.MainAxisAlignment.START,
            ),
            ftd.DataColumn2(
                label=ft.Text("Last Modified"),
                on_sort=sort_column,
                numeric=True,
                heading_row_alignment=ft.MainAxisAlignment.END,
            ),
        ]

    def get_data_rows(items: list) -> list[ftd.DataRow2]:
        return [
            ftd.DataRow2(
                specific_row_height=50,
                on_select_change=handle_row_selection_change,
                cells=[
                    ft.DataCell(content=ft.Text(file.name)),
                    ft.DataCell(content=ft.Text(file.modified_at)),
                ],
            )
            for file in items
        ]

    table = ftd.DataTable2(
        expand=True,
        show_checkbox_column=True,
        column_spacing=0,
        heading_row_color=ft.Colors.SECONDARY_CONTAINER,
        horizontal_margin=12,
        sort_ascending=True,
        bottom_margin=10,
        min_width=600,
        on_select_all=lambda _: print("All selected"),
        columns=get_data_columns(),
        rows=get_data_rows(files),
    )

    page.add(ft.SafeArea(expand=True, content=table))


if __name__ == "__main__":
    ft.run(main)