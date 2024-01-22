from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_car(self):
        pass

    @abstractmethod
    def visit_plane(self):
        pass

    @abstractmethod
    def visit_train(self):
        pass

class Transport(ABC):
    @abstractmethod
    def on_visit(self, visitor: Visitor) -> None:
       pass 


class Plane(Transport):
    def on_visit(self, visitor: Visitor) -> None:
        visitor.visit_plane(self);

class Train(Transport):
    def on_visit(self, visitor: Visitor) -> None:
        visitor.visit_train(self);

class Car(Transport):
    def on_visit(self, visitor: Visitor) -> None:
        visitor.visit_car(self);


class Visitor_Exporter(Visitor):
    def visit_car(self):
        print("car")

    def visit_plane(self):
        print("plane")

    def visit_train(self):
        print("train")

if __name__ == "__main__":
    vis_ex = Visitor_Exporter
    [trans.on_visit(vis_ex) for trans in [Plane(), Train(), Car()]]

