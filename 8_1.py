# ------------- LESSON 8, EXERCISE 1 -------------------

text = ''' 
[Section1]
key1=value1
key2=value2

[Section2]
key3=value3
key4=value4
key5=value5
'''


class ConfigParser:
    def __init__(self, data: str):
        """

        :param data: received string of config file
        """
        self.strng = data
        self.rslt = self.dict()

    def __str__(self) -> str:
        """ Format dict to str

        :return: string
        """
        res = ['\n'.join(['[' + i[0] + ']', '\n'.join([f'{key}={value}' for key, value in i[1].items()])]) for i in self.rslt.items()]
        return '\n'.join(res)

    def dict(self) -> dict[str: dict[str: str]]:
        """ From config file make dictionary

        :return: dict where values are dictionaries
        """
        lst = [((i.strip()).replace(']', '').split('\n')) for i in self.strng.split('[') if ']' in i]
        dct = {i[0]: {key: value for key, value in [j.split('=') for j in i[1:]]} for i in lst}
        return dct

    def get(self, sect_name: str, param: str) -> str:
        """ Get value from dict

        :param sect_name: key from external dict
        :param param: key from internal dict
        :return: value from internal dict
        """
        dct = self.rslt
        if param in dct[sect_name]:
            return dct[sect_name][param]
        else:
            raise ValueError

    def add_section(self, sect_name: str) -> str:
        """ Add new section to dict

        :param sect_name: name of section in dictionary
        :return: string of success
        """
        dct = self.rslt
        if sect_name not in dct:
            dct.setdefault(sect_name, {})
            return f'Section {sect_name} is added'
        else:
            raise ValueError

    def add_param(self, sect_name: str, param: str, value: str) -> str:
        """ Add new param to section in dict

        :return: string of success
        """
        dct = self.rslt
        if sect_name not in dct:
            raise ValueError

        dct[sect_name][param] = value
        return f'Value {value} for {param} in {sect_name} is added successfully'

    def has_section(self, sect_name: str) -> bool:
        """
        :return: if dict has section
        """
        return sect_name in self.rslt

    def has_param(self, sect_name: str, param: str) -> bool:
        """
        :return: if section in dict has param
        """
        if sect_name not in self.rslt:
            raise ValueError

        return param in self.rslt[sect_name]

    def del_section(self, sect_name: str) -> str:
        """ Delete section from dict

        :return: string of success
        """
        if sect_name in self.rslt:
            self.rslt.pop(sect_name)
            return f'Section {sect_name} deleted successfully'

    def del_param(self, sect_name: str, param: str) -> str:
        """ Delete parameter from section in dict

        :return: string of success
        """
        if param in self.rslt[sect_name]:
            self.rslt[sect_name].pop(param)
            return f'Parameter {param} from section {sect_name} deleted successfully'


data = ConfigParser(text)
print(data.get('Section1', 'key1'))
print(data.add_section('abc'))
data.add_param('Section1', 'aaa', 'ab')
data.del_section('Section2')
data.del_param('Section1', 'key1')
data.add_param('abc', 'name', 'surname')
print(data.has_section('Section1'), data.has_param('Section1', 'aaa'))
print(data.rslt)
print(data)
