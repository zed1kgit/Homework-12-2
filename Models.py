class ArticleModel:
    def __init__(self, title, author, symbols, site, description):
        self.article_info = {
            "title": title,
            "author": author,
            "symbols": symbols,
            "site": site,
            "description": description
        }

    def get_info(self):
        return self.article_info

    def change_data(self, type_of_data, data):
        if type_of_data not in self.article_info.keys():
            return "Ошибка"
        else:
            self.article_info[type_of_data] = data
            return self.article_info[type_of_data]


class FilmModel:
    def __init__(self, title, director, year, duration, studio):
        self.film_info = {
            "title": title,
            "director": director,
            "year": year,
            "duration": duration,
            "studio": studio,
            "actors": []
        }

    def get_info(self):
        return self.film_info

    def change_data(self, type_of_data, data):
        if type_of_data not in self.film_info.keys():
            return "Ошибка"
        else:
            self.film_info[type_of_data] = data
            return self.film_info[type_of_data]

    def add_actor(self, name, role):
        self.film_info["actors"].append([name, role])
