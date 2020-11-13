from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty, abstractstaticmethod
from collections.abc import MutableMapping

class FirebaseObject(MutableMapping):

    _data_types = {"string": str, "int": int, "array": list}
    
    @property
    @abstractmethod
    def _type_defs(self):
        pass

    def __init__(self):
        super().__init__()

    def to_dict(self):
        return dict(self)

    def from_dict(self, dict_data):
        """ Creates an object of the type from the dictionary.
        Will check each property first to see if it's a valid property,

        """
        # loop through all the passed in attributes
        # check if they're in the definitions, 
        for key, value in dict_data.items():
            # defs = self._type_defs
            # print("KEY:" + key)
            # print("VALUE:" + str(value))
            # if key in defs:
            #     key_type = defs[key]
            #     print("KEY TYPE:" + str(key_type))
            #     attribute_type = self._data_types[key_type]
            #     print("ATTRIBUTE_TYPE:" + str(attribute_type))
            #     if value is None or isinstance(value, attribute_type):
            #         setattr(self, key, value)
            #     else:
            #         raise TypeError(str(value) + " received for " + key + " attribute requiring type " + str(attribute_type))
            # else:
            #     raise AttributeError(key + " is not a valid attribute of this object")

            setattr(self, key, value)
        return self


    def validate(self):

        for type_def in self._type_defs.items():
            field = type_def[0]
            field_type = type_def[1]

            actual_field = getattr(self, field)

            # isinstance doesn't work right here
            if isinstance(actual_field, field_type):
                print("Yes, " + field + " is a " + field_type)
            else:
                print("OH NO!")
                print(actual_field + "is not a " + self._data_types[field_type])


    