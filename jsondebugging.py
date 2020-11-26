import json
import os
import re
import time

from jsonschema import Draft7Validator
from jsonschema.exceptions import SchemaError


JSON_PATH = "task_folder/event/"
SCHEMA_PATH = "task_folder/schema/"

FILE_SEPARATOR = "\n\n" + "*" * 20 + "\n\n"
ERROR_SEPARATOR = "-" * 20 + "\n"
E = ERROR_SEPARATOR + "ERROR: "
S = "SOLUTION: "


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
        message = (
            f"{E}The file is empty.\n" f"{S}Add data to JSON file: {f.name}."
        )
        return None, message

    if not isinstance(json_data, dict):
        message = (
            f"{E}Invalid data format in the file.\n"
            f"{S}Check the data in JSON file: {f.name}."
        )
        return (None,)

    return json_data, None


def get_schema(json_data):
    event = json_data.get("event")

    if not event:
        message = (
            f"{E}There is no 'event' in the JSON file.\n"
            f"{S}Add 'event' property to JSON file."
        )
        return None, message

    schema = open_json_file(SCHEMA_PATH + event + ".schema")

    if isinstance(schema, FileNotFoundError):
        message = (
            f"{E}The schema for the file was not found.\n"
            f"{S}Add '{event}.schema' file to folder '{SCHEMA_PATH}'."
        )
        return None, message

    return schema, None


def error_solution(error):
    field = re.search("'(.+?)'", error.message).group(0)

    # TODO add a solution for all errors
    add_solution = "The solution will be updated."
    
    solution = {
        "$ref": add_solution,
        "additionalItems": add_solution,
        "additionalProperties": add_solution,
        "allOf": add_solution,
        "anyOf": add_solution,
        "const": add_solution,
        "contains": add_solution,
        "dependencies": add_solution,
        "enum": add_solution,
        "exclusiveMaximum": add_solution,
        "exclusiveMinimum": add_solution,
        "format": add_solution,
        "if": add_solution,
        "items": add_solution,
        "maxItems": add_solution,
        "maxLength": add_solution,
        "maxProperties": add_solution,
        "maximum": add_solution,
        "minItems": add_solution,
        "minLength": add_solution,
        "minProperties": add_solution,
        "minimum": add_solution,
        "multipleOf": add_solution,
        "oneOf": add_solution,
        "not": add_solution,
        "pattern": add_solution,
        "patternProperties": add_solution,
        "properties": add_solution,
        "propertyNames": add_solution,
        "required": f"Аdd the {field} property to JSON data",
        "type": f"Add a value with the correct data type: {field}",
        "uniqueItems": add_solution,
    }
    message = f"{E}{error.message}.\n{S}{solution[error.validator]}."
    return message


def check_json_data(schema, json_data):
    try:
        Draft7Validator.check_schema(schema)
    except SchemaError as error:
        return E + "Invalid schema:\n" + error.message + S + "Fix the schema."

    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(json_data["data"]))

    if errors:
        errors = [error_solution(error) for error in errors]
        return "\n".join(errors)

    return "OK: No errors found."


def check_file(f):
    json_data, error_message = get_json_data(f)

    if error_message:
        return error_message

    schema, error_message = get_schema(json_data)

    if error_message:
        return error_message

    return check_json_data(schema, json_data)


if __name__ == "__main__":
    now = time.time()
    file_name = "JSON_debug_" + time.strftime(
        "%d-%m-%Y-%H-%M-%S", time.localtime(now)
    )

    with open(file_name, "w") as log_file:
        for i, f in enumerate(os.scandir(JSON_PATH)):
            if f.is_file() and os.path.splitext(f.path)[1] == ".json":
                log_file.write(
                    f"#{i+1}. Checking the file: {f.name}\n"
                    + check_file(f)
                    + FILE_SEPARATOR
                )
