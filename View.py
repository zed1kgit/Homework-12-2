class View:
    def __init__(self, controller):
        self.controller = controller

    def print_default_info(self):
        print(self.controller.get_default_info())

    def print_all_info(self):
        print(self.controller.get_all_info())
