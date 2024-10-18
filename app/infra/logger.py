# -*- coding: utf-8 -*-

import logging
from pathlib import Path
from typing import Any, Callable, Optional
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from enum import Enum


BASE_PATH = str(Path(__file__).resolve().parent.parent)


class LogLevel(Enum):
    NOTSET: int = 0
    DEBUG: int = 10
    INFO: int = 20
    WARNING: int = 30
    ERROR: int = 40
    CRITICAL: int = 50


class Logger:

    DEFAULT_LOG_PATH = BASE_PATH + r"/logs/log.log"

    @staticmethod
    def create_folder_if_not_exists(filepath: str) -> None:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        if not Path(filepath).exists():
            Path(filepath).touch()

    def __init__(
        self,
        lvl: Optional[Any] = LogLevel.INFO,
        filepath: Optional[str] = DEFAULT_LOG_PATH,
        encoding: Optional[str] = "utf-8",
        terminal_level: Optional[LogLevel] = None,
    ) -> None:
        self.logging = logging

        terminal_level = terminal_level.value if terminal_level else lvl.value

        self.create_folder_if_not_exists(filepath)

        file_handler = TimedRotatingFileHandler(
            filename=filepath,
            backupCount=3365,
            encoding=encoding,
            when="midnight",
        )
        file_handler.setLevel(lvl.value)
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s"
            )
        )

        terminal_handler = logging.StreamHandler()
        terminal_handler.setLevel(terminal_level)
        self.logging.basicConfig(
            level=terminal_level,
            format="* %(levelname)-8s :%(message)s",
            encoding=encoding,
            handlers=[file_handler, terminal_handler],
        )

    def log(self, msg: str, lvl: LogLevel = LogLevel.INFO) -> None:
        return self.logging.log(lvl.value, msg)

    def function_log(self, arg: str = "") -> Callable:
        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs):
                base_msg = (
                    f"[{arg}.{func.__name__}]" if isinstance(arg, str) else f"[{func.__name__}]"
                )
                try:
                    self.info(f'{base_msg} STARTED IN: "{datetime.now()}"')
                    self.info(
                        f'{base_msg} function arguments: {args=} {kwargs=}'
                    )
                    self.info(f"{base_msg} function return: {func(*args, **kwargs)!r}")
                    self.info(f'{base_msg} FINISHED IN: "{datetime.now()}"')
                    return func(*args, **kwargs)
                except Exception as error:
                    self.error(f"{base_msg} ERROR DETAIL: {error}")
                    raise error

            return wrapper

        if callable(arg):
            return decorator(arg)
        return decorator

    def debug(self, msg: str) -> None:
        self.log(msg, LogLevel.DEBUG)

    def warn(self, msg: str) -> None:
        self.log(msg, LogLevel.WARNING)

    def info(self, msg: str) -> None:
        self.log(msg, LogLevel.INFO)

    def critical(self, msg: str) -> None:
        self.log(msg, LogLevel.CRITICAL)

    def error(self, msg: str) -> None:
        self.log(msg, LogLevel.ERROR)


log = Logger(
    lvl=LogLevel.DEBUG, terminal_level=LogLevel.INFO
)
