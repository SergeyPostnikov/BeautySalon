from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Salon(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    address = models.CharField(
        'адрес',
        max_length=100,
    )
    working_time_from = models.TimeField(
        'работает с',
    )
    working_time_to = models.TimeField(
        'работает по',
    )
    image = models.ImageField(
        'картинка'
    )

    class Meta:
        verbose_name = 'салон'
        verbose_name_plural = 'салоны'
    
    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(
        'название',
        max_length=100
    )

    class Meta:
        verbose_name = 'проффесия'
        verbose_name_plural = 'проффесии'
    
    def __str__(self):
        return self.name


class Master(models.Model):
    fullname = models.CharField(
        'полное имя',
        max_length=100
    )
    profession = models.ForeignKey(
        Profession,
        verbose_name='проффесия',
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        'фото'
    )
    work_duration = models.DurationField(
        'стаж работы',
    )

    class Meta:
        verbose_name = 'мастер'
        verbose_name_plural = 'мастера'
    
    def __str__(self):
        return f'{self.fullname}, {self.profession}'


class Service(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    description = models.TextField(
        'описание',
        max_length=400,
        blank=True,
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    image = models.ImageField(
        'картинка'
    )
    master = models.ManyToManyField(
        Master,
        related_name='servises'
    )

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
    
    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(
        'имя',
        max_length=50
    )
    phone = PhoneNumberField(
        'телефон'
    )

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
    
    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.ForeignKey(
        Client,
        verbose_name='клиент',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        'отзыв',
        max_length=400,
    )
    date = models.DateField(
        'дата отзыва',
        auto_now=True
    )
    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
    
    def __str__(self):
        return f'от {self.name}, оставлен {self.date}'


class Order(models.Model):
    client = models.ForeignKey(
        Client,
        verbose_name='клиент',
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service,
        verbose_name='услуга',
        on_delete=models.CASCADE
    )
    date = models.DateField(
        'день'
    )
    time = models.TimeField(
        'время'
    )

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
    
    def __str__(self):
        return f'от {self.name}, оставлен {self.service}'
