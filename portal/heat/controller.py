from openpyxl import load_workbook
from typing import List

from .models import Home


def parsing_xlsx(input_file: str, start_row: int,
                 stop_row: int, start_col: int,
                 stop_col: int, sheet: str = None,
                 cells: tuple = None) -> List[list]:
    """Парсинг XLSX файлов. В результате будет список со вложенными
    списками содержащими данные из ячеек.

    Args:
        input_file (str): прямой или относительный путь к файлу
        start_row (int): номер начальной строки
        stop_row (int): номер завершающей строки
        start_col (int): номер начального столбца
        stop_col (int): номер заверщшающего столбца
        sheet (str, optional): имя листа. если оставить None,
        будет выбран первый лист в книге.
        cells (tuple, optional): ячейки которые необходимо спарсить.
        если оставить None, в результирующем списке будут все ячейки
        от start_col до stop_col

    Returns:
        List[list]: Списко со вложенным списком содержалщим значения ячеек.
    """
    xlsx_file = load_workbook(filename=input_file, data_only=True)
    if sheet is None:
        sheet = xlsx_file[xlsx_file.sheetnames[0]]
    else:
        sheet = xlsx_file[sheet]
    result = []
    for row in range(start_row, stop_row, 1):
        list_cell = sheet.iter_rows(min_col=start_col, max_col=stop_col,
                                    min_row=row, max_row=row,
                                    values_only=True)
        new_list_row = []
        for cell in list_cell.__next__():
            if cell is None:
                new_list_row.append(0)
            else:
                new_list_row.append(cell)
        if cells is not None:
            new_list_row = [new_list_row[x] for x in cells]
        result.append(new_list_row)
    return result


def recording_in_db(data: List[list], table_name):
    fields = [field.name for field in table_name._meta.fields]
    check_column = len(fields) == len(data[0])
    if check_column:
        for element in data:
            model = [table_name]*len(fields)
            run = map(setattr, model, fields, element)
            for item in element:
                run.__next__()
    return print(fields, check_column, table_name)
