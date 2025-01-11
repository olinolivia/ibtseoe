import json
from pyperclip import copy

with open('config.json', 'rt') as f:
    config = json.loads(f.read())

with open(config['project_path']['value'], 'rt') as f:
    project_data = json.loads(f.read())

with open('objects.json', 'rt') as f:
    lookup = json.loads(f.read())

value_separator = ','
obj_separator = ';'
room_separator = '&'
value_separate_after = False
obj_separate_after = True
room_separate_after = False


def format_value(value):

    # escape
    if isinstance(value, str):
        for char in [value_separator, obj_separator, room_separator, '\\']:
            value = value.replace(char, '\\' + char)

    # format None
    elif value is None:
        value = '(null)'

    return value


def macro(value, fields: dict):
    if isinstance(value, str) and value[0] == '$':
        value = fields[value[1:]]
    return value


class Obj:

    def __init__(self, entity_instance: dict):

        pos = entity_instance['px']
        # account for different level and object origin, and flipped y axis
        pos[0] -= 232
        pos[1] = -pos[1] + 172

        fields = {}
        for field_instance in entity_instance['fieldInstances']:
            fields[field_instance['__identifier']] = field_instance['__value']

        self.identifier = entity_instance['__identifier']
        self.pos = pos
        self.fields = fields

    def __str__(self):
        global value_separator
        global value_separate_after

        r = ''
        r += format_value(macro(lookup[self.identifier]['sprite_id'], self.fields)) + value_separator
        r += str(self.pos[0]) + value_separator
        r += str(self.pos[1])
        for field in lookup[self.identifier]['fields']:
            r += value_separator + str(format_value(macro(field, self.fields)))
        if value_separate_after:
            r += value_separator

        return r


def get_level_id(level_instance: dict):
    return level_instance['identifier']


game_string = ''
for level in sorted(project_data['levels'], key=get_level_id):
    for layer in level['layerInstances']:
        for entity in layer['entityInstances']:
            game_string += str(Obj(entity))
            game_string += obj_separator
        if not obj_separate_after:
            game_string = game_string[:-1]
    game_string += room_separator
if not room_separate_after:
    game_string = game_string[:-1]

print('Copied game string to clipboard!\n' + game_string)
copy(game_string)
