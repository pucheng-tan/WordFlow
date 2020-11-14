from abc import ABC
from context_service import ContextService


class ApplicationManagement(ABC):

    _context = ContextService.get_instance()
