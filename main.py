from Models import ArticleModel, FilmModel
from Controllers import ArticleController, FilmController
from View import View

article_model = ArticleModel("t_title", "t_author", 300, "t_site", "t_description")
article_controller = ArticleController(article_model)
article_view = View(article_controller)

article_view.print_default_info()
print()
article_view.print_all_info()
print()

input()
film_model = FilmModel("Интерстеллар", "Кристофер Нолан", 2014, "2 ч 49 мин", "Paramount Pictures")
film_controller = FilmController(film_model)
film_view = View(film_controller)

film_controller.add_actor("Мэттью Макконахи", "Cooper", "editor")
film_controller.add_actor("Энн Хэтэуэй", "Brand", "editor")
film_controller.add_actor("Джессика Честейн", "Murph", "editor")

film_view.print_default_info()
print()
film_view.print_all_info()

