import json
import os


def get_json_from_csv(filename: str) -> dict[str, (dict[str, list]), (str, int)]:
    path = os.path.abspath(filename)
    with open(path, 'r') as f:
        data = f.read().split("\n")[1:]
    json_data: dict[str, (dict[str, list]), (str, int)] = {}
    for line in data:
        line = line.split(',')
        # This check help with whitespace in file
        if line[0] == '' or line[1] == '':
            continue
        # Add person to existing country object
        elif line[0] in json_data:
            json_data[line[0]]['people'].append(line[1])
            json_data[line[0]]['count'] += 1
        # Add first country with line
        else:
            json_data[line[0]] = {'people': [line[1]], 'count': 1}

    return json.dumps(json_data, indent=2)


if __name__ == '__main__':
    print(get_json_from_csv('task_1/data.csv'))
