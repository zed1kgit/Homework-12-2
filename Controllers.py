class ArticleController:
    def __init__(self, model):
        self.model = model

    def get_default_info(self):
        info = self.model.get_info()
        result = f"Название статьи: {info["title"]},\nАвтор: {info["author"]}"
        return result

    def get_all_info(self):
        info = self.model.get_info()
        result = (f"Название статьи: {info["title"]}\n"
                  f"Автор: {info["author"]}\n"
                  f"Количество символов: {info["symbols"]}\n"
                  f"Впервые опубликована: {info["site"]}\n"
                  f"Краткое описание: {info["description"]}")
        return result

    def change_data(self, type_of_data, data, permission):
        if permission in ["admin", "author"]:
            self.model.change_data(type_of_data, data)
            return "Статья изменена"
        else:
            return "Нет прав"


class FilmController:
    def __init__(self, model):
        self.model = model

    def get_default_info(self):
        info = self.model.get_info()
        result = f"Название фильма: {info["title"]} ({info["year"]}),\nРежиссер: {info["director"]}"
        return result

    def get_all_info(self):
        info = self.model.get_info()

        result = (f"Название фильма: {info["title"]}\n"
                  f"Режиссер: {info["director"]}\n"
                  f"год: {info["year"]}\n"
                  f"Длительность: {info["duration"]}\n"
                  f"Студия: {info["studio"]}\n"
                  f"Актеры: {", ".join(list(map(lambda x: f"{x[0]} в роли {x[1]}", info["actors"])))}")
        return result

    def change_data(self, type_of_data, data, permission):
        if permission in ["admin", "editor"]:
            self.model.change_data(type_of_data, data)
            return "Информация о фильме изменена"
        else:
            return "Нет прав"

    def add_actor(self, name, role, permission):
        if permission in ["admin", "editor"]:
            self.model.add_actor(name, role)
            return "Актер добавлен"
        else:
            return "Нет прав"
