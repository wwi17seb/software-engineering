from abc import ABC, abstractmethod
from typing import Any


class Handler(ABC):
    """
    Define an interface for handling requests.
    Implement method to set next handler.
    """

    _next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    @abstractmethod
    def approve_request(self, request: Any):
        pass

"""
Concrete Handler handle request, otherwise forward it to next handler.
"""

class ManagerHandler(Handler):

    def approve_request(self, request):
        if request <= 200:
            print(f"{request}$ are approved by Manager.")
        elif self._next is not None:
            self._next.approve_request(request)


class HeadOfDepartmentHandler(Handler):

    def approve_request(self, request):
        if request > 200 and request <= 1000:
            print(f"{request}$ are approved by Head of Department.")
        elif self._next is not None:
            self._next.approve_request(request)
            
            
class BusinessUnitManagerHandler(Handler):

    def approve_request(self, request):
        if request > 1000 and request <= 5000:
            print(f"{request}$ are approved by Business Unit Manager.")
        elif self._next is not None:
            self._next.approve_request(request)
            
            
class ExecutiveBoardHandler(Handler):

    def approve_request(self, request):
        if request > 5000:
            print(f"{request}$ approved by Executive Board.")
        elif self._next is not None:
            self._next.approve_request(request)


def main():
    # create objects of concrete handler
    manager = ManagerHandler()
    headOfDepartment = HeadOfDepartmentHandler()
    businessUnitManager = BusinessUnitManagerHandler()
    executiveBoard = ExecutiveBoardHandler()
    
    # set chain of responsibility
    manager.set_next(headOfDepartment).set_next(businessUnitManager).set_next(executiveBoard) 
    
    # send request for approval
    manager.approve_request(500)
    manager.approve_request(100)
    manager.approve_request(6000)
    manager.approve_request(2500)
    manager.approve_request(700)
       


if __name__ == "__main__":
    main()

