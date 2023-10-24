from abc import ABC, abstractmethod
 
class Company():
    def __init__(self) -> None:
          self.__company_id = ''
          self.__title = ''
 
    def __set_company_id(self, company_id: str) -> None:
          self.__company_id = company_id
 
    def __get_company_id(self) -> str:
          return self.__company_id
 
    def __set_title(self, title: str) -> None:
          self.__title = title
 
    def __get_title(self) -> str:
          return self.__title
 
    title = property(__get_title, __set_title)
    company_id = property(__get_company_id, __set_company_id)
 
    def properties(self) -> None:
          print(f'{self.__title} company with {self.__company_id} company_id')


class ICompanyBuilder(ABC):
    @abstractmethod
    def build(self):
        "build"


class ACompanyBuilder(ICompanyBuilder):
    __company = None
    def build(self) -> Company:
        self.__company = Company()
        self.__company.title = 'A'
        self.__company.company_id = '1'


class BCompanyBuilder(ICompanyBuilder):
    __company = None
    def build(self) -> Company:
             self.__company = Company()
             self.__company.title = 'B'
             self.__company.company_id = '2'


class CompanyFactory():
    __builder: ICompanyBuilder = None
    def set_builder(self, builder: ICompanyBuilder) -> None:
        self.__builder = builder
    def get_company(self) -> Company:
        self.__builder.build()
        company = self.__builder.__company
        return company


def test_company():
    factory = CompanyFactory()
    factory.set_builder(ACompanyBuilder())
    company = factory.get_company()
    assert company.company_id == '1'
    assert company.title == 'A'

    factory.set_builder(BCompanyBuilder())
    company = factory.get_company()
    assert company.company_id == '2'
    assert company.title == 'B'


test_company()
