class ExportTxt:
    def __init__(self, raw_data):
        self.data = self.prepare(raw_data)

    def prepare(self, raw_data):
        result = ''
        for item in raw_data:
            new_line = ';'.join(
                (
                    item['name'],
                    item['last_name'],
                    item['age']
                )
            )
            result += f'{new_line}\n'
        return result

    def write_file(self, file_name):
        with open(file_name, 'w', encoding='UTF8') as f:
            f.write(self.data)


data = [
    {
        'name': 'Ivan',
        'last_name': 'Ivanov',
        'age': '18'
    },
    {
        'name': 'Petr',
        'last_name': 'Petrov',
        'age': '19'
    }
]

exporter = ExportTxt(data)
exporter.write_file('out.txt')

