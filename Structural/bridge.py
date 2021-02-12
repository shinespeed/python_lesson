from __future__ import annotations
from abc import ABC, abstractmethod


class View:
    def __init__(self, view_impl: ViewImpl):
        self.view_impl = view_impl

    def draw_text(self):
        return (f"View: "
                f"{self.view_impl.draw_text()}")

    def draw_line(self):
        return (f"View: "
                f"{self.view_impl.draw_line()}")


class ViewContent(View):
    def draw_paragraph(self):
        print(self.draw_line())
        print(self.draw_text())


class ViewTable(View):
    def draw_cell(self):
        print(self.draw_text())
        print(self.draw_line())


class ViewImpl(ABC):
    @abstractmethod
    def draw_text(self):
        pass

    @abstractmethod
    def draw_line(self):
        pass


class ViewCLI(ViewImpl):
    def draw_text(self):
        return "draw text in cli"

    def draw_line(self):
        return "draw line in cli"


class ViewJson(ViewImpl):
    def draw_text(self):
        return "draw text in json"

    def draw_line(self):
        return "draw line in json"



if __name__ == "__main__":
    impl_1 = ViewCLI()
    impl_2 = ViewJson()
    view = ViewContent(impl_1)
    view.draw_paragraph()

    print("\n")
    view = ViewTable(impl_2)
    view.draw_cell()