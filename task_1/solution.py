import json
import os


def get_json_from_csv(filename: str) -> dict[str, (dict[str, list]), (str, int)] :
    path = os.path.abspath(filename)
    with open(path, 'r') as f:
        data = f.read().split("\n")[1:]
    json_data: dict[str, (dict[str, list]), (str, int)] = {}
    for person in data:
        person = person.split(',')
        # This check help with whitespace in file
        if person[0] == '':
            continue
        # Add person to existing country object
        elif person[0] in json_data:
            json_data[person[0]]['people'].append(person[1])
            json_data[person[0]]['count'] = len(json_data[person[0]]['people'])
        # Add first country with person
        else:
            json_data[person[0]] = {'people': [person[1]], 'count': 1}

    return json.dumps(json_data, indent=2)


if __name__ == '__main__':
    print(get_json_from_csv('task_1/data.csv'))
