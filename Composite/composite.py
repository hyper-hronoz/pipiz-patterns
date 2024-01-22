class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'New group'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def _print(self, items, depth):
        items.append(' ' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 2)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'


class Line(GraphicObject):
    @property
    def name(self):
        return 'Line'


drawing = GraphicObject()
drawing.name = 'First picture'
drawing.children.append(Square('Red'))
drawing.children.append(Square('Blue'))

first_group = GraphicObject()
first_group.name += '1'
first_group.children.append(Circle('Yellow'))
first_group.children.append(Circle('Green'))
drawing.children.append(first_group)

second_group = GraphicObject()
second_group.name += '2'
second_group.children.append(Line('Black'))
second_group.children.append(Line('White'))
drawing.children.append(second_group)

third_group = GraphicObject()
third_group.name += '3'
third_group.children.append(Square('Red'))
third_group.children.append(Circle('Yellow'))
third_group.children.append(Line('Black'))
second_group.children.append(third_group)

print(drawing)
