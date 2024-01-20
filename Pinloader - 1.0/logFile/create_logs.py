def write_logs_file(log_text: str):
    logs = open("logs/logs.txt", "w")
    logs.write(log_text)


def write_logs(url: str, request_code: int, board_id: str, pin_count: str,  result: list, errors: list):
    """
    пишет логи
    :param url: URL доски пользователя
    :param request_code: Код ответа от сервера
    :param board_id: ID доски пользователя
    :param pin_count: Количество пинов в доске пользователя
    :param result: результат выполенения программы
    """
    text = (f"URL: {url}\n"
            f"REQUEST CODE: {request_code}\n"
            f"BOARD ID : {board_id}\n"
            f"PINS COUNT: {pin_count}\n")
    if errors is [] or errors == [None, None, None, None, None, None, None]:
        text += "ERRORS: None"
    else:
        text += "ERRORS:"
        for value in errors:
            if value is not None:
                text += f"\n{value}"

    if result is not None:
        text += f"\nWAS PARCED: {len(result)}\n"
        text += "\nRESULT: "
        for value in result:
            text += f"\n{value}"
    else:
        text += "RESULT: None"
    write_logs_file(log_text=text)


