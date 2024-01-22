class FormatData:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def prepare(self):
        result = ''
        for item in self.raw_data:
            new_line = ';'.join(
                (
                    item['name'],
                    item['last_name'],
                    item['age']
                )
            )
            result += f'{new_line}\n'
        return result


class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, data):
        with open(self.file_name, 'w', encoding='UTF8') as f:
            f.write(data)


data = [
    {
        'name': 'Ivannnn',
        'last_name': 'Ivanovvvv',
        'age': '28'
    },
    {
        'name': 'Petrrrr',
        'last_name': 'Petrovvvv',
        'age': '29'
    }
]

formatter = FormatData(data)
formatted_data = formatter.prepare()

writer = FileWriter('out.txt')
writer.write_file(formatted_data)

