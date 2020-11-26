import json
import os
import time

from jsonschema import Draft7Validator
from jsonschema.exceptions import SchemaError


def open_json_file(file_path):
    try:
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError as er:
        return er

    return json_data


def get_json_data(f):
    json_data = open_json_file(f.path)

    if json_data is None:
        return None, "ERROR: The file is empty."

    if not isinstance(json_data, dict):
        return None, "ERROR: Invalid data format in the file."

    return json_data, None


def get_schema(json_data):
    event = json_data.get("event")

    if not event:
        return None, "ERROR: There is no 'event' in the file."

    schema = open_json_file(SCHEMA_PATH + event + ".schema")

    if isinstance(schema, FileNotFoundError):
        return None, "ERROR: The schema for the file was not found."

    return schema, None


def check_json_data(schema, json_data):
    try:
        Draft7Validator.check_schema(schema)
    except SchemaError as error:
        return "ERROR: Invalid schema:\n" + error.message

    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(json_data))

    if errors:
        errors = [error.message for error in errors]
        return "ERRORS IN JSON DATA:\n" + "\n".join(errors)

    return "OK: No errors found."


def check_file(f, log_file):
    json_data, error_message = get_json_data(f)

    if error_message:
        return error_message

    schema, error_message = get_schema(json_data)

    if error_message:
        return error_message

    return check_json_data(schema, json_data)


if __name__ == "__main__":
    JSON_PATH = "task_folder/event/"
    SCHEMA_PATH = "task_folder/schema/"
    SEPARATOR = "\n" + "-" * 20 + "\n\n"

    now = time.time()
    file_name = "JSON_debug_" + time.strftime(
        "%d-%m-%Y-%H-%M-%S", time.localtime(now)
    )

    with open(file_name, "w") as log_file:
        for i, f in enumerate(os.scandir(JSON_PATH)):
            if f.is_file() and os.path.splitext(f.path)[1] == ".json":
                log_file.write(
                    f"#{i+1}. Checking the file: {f.name}\n"
                    + check_file(f, log_file)
                    + SEPARATOR
                )
