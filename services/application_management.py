from abc import ABC
from context_service import ContextService


class ApplicationManagement(ABC):

    _context = ContextService.get_instance()

    def _validate(self, obj):
        """
        Args:
            obj: the object to validate
            field_list: a list of the fields
                each with possible rules to test (can add more like min, max)
                "required": these fields are required
                "required|id": required for new instances (ie: no id)
        Returns:
            
        """
        # new_object = {}
        # for field in field_list:
        #     if field in obj:
        #         field_value = obj[field]  
        #     if field in field_dict: # if there's any rules:
        #         if 
        #     if allowed_types and type(field_value) != allowed_types[field]:
        #         return {"error": "Wrong type for key: " + field + " value: " + field_value}
        #     else:
        #         new_object[field] = field_value
            
        return obj