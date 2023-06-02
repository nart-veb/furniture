from django.db import models


class Slide(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.CharField("Описание", max_length=300)
    button_text = models.CharField("Текст кнопки", max_length=40)
    button_path = models.CharField("Ссылка, на которую ссылается кнопка", max_length=300)
    image = models.ImageField("Картинка", upload_to="images/")
    sequence = models.IntegerField("Очередность слайда")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"

class Kitchen(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Картинка", upload_to="kitchen/")
    sequence = models.IntegerField("Очередность 'элемента'")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кухня"
        verbose_name_plural = "Кухни"

class Wardrobe(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Картинка", upload_to="wardrobe/")
    sequence = models.IntegerField("Очередность 'элемента'")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Гардеробная"
        verbose_name_plural = "Гардеробные"

class Bedroom(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Картинка", upload_to="bedroom/")
    sequence = models.IntegerField("Очередность 'элемента'")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Спальня"
        verbose_name_plural = "Спальни"


class Furniture(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Картинка", upload_to="furniture/")
    sequence = models.IntegerField("Очередность 'элемента'")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебель"




