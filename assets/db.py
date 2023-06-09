
record = {  
    'id': 32985,
    'salon_name': 'BeautyCity Пушкинская',
    'salon_address': 'ул. Пушкинская, д. 78А',
    'service_name': 'Дневной макияж',
    'price': 750,
    'master_name': 'Елена Грибнова',
    'master_photo': '/static/img/masters/avatar/vizajist1.svg',
    'date': '18 ноября',
    'time': '11:00',
    'active': False,
    'payment_id': '',
    'paid': False
}

salons = [
    {
        'name': 'BeautyCity Пушкинская',
        'address': 'ул. Пушкинская, д. 78А',
        'image': '/static/img/salons/salon1.svg',
        'working_time': 'с 10:00 до 20:00 без выходных',
    },
    {
        'name': 'BeautyCity Ленина',
        'address': 'ул. Ленина, д. 211',
        'image': '/static/img/salons/salon2.svg',
        'working_time': 'с 10:00 до 20:00 без выходных',
    },
    {
        'name': 'BeautyCity Красная',
        'address': 'ул. Красная, д. 10',
        'image': '/static/img/salons/salon3.svg',
        'working_time': 'с 10:00 до 20:00 без выходных',
    },
]

services = [
    {
        'name': 'Макияж',
        'services':
        [
            {
                'name': 'Дневной макияж',
                'price': '1 400',
                'image': '/static/img/services/service1.svg'
            },
            {
                'name': 'Вечерний макияж',
                'price': '1 400',
                'image': '/static/img/services/service1.svg'
            },
            {
                'name': 'Свадебный макияж',
                'price': '1 400',
                'image': '/static/img/services/service1.svg'
            },
        ],
    },
    {
    'name': 'Ногтевой сервис',
    'services':
        [
            {
                'name': 'Маникюр. Классический. Гель',
                'price': '2 000',
                'image': '/static/img/services/service2.svg'
            },
            {
                'name': 'Педикюр',
                'price': '1 000',
                'image': '/static/img/services/service5.svg'
            },
            {
                'name': 'Наращиание ногтей',
                'price': '1 000',
                'image': '/static/img/services/service5.svg'
            },
        ],
    },
    {
    'name': 'Парикмахерские услуги',
    'services':
        [
            {
                'name': 'Укладка волос',
                'price': '1 500',
                'image': '/static/img/services/service3.svg'
            },
            {
                'name': 'Укладка волос',
                'price': '3 000',
                'image': '/static/img/services/service4.svg'
            },
            {
                'name': 'Окрашивание волос',
                'price': '5 000',
                'image': '/static/img/services/service6.svg'
            },
        ],
    },
]
reviews = [
    {
        'name': 'Светлана Г.',
        'text': 'Отличное место для красоты, очень доброжелательный и отзывчивый персонал, девочки заботливые, аккуратные и большие профессионалы. Посещаю салон с самого начала, но он не теряет своей привлекательности, как в обслуживании.',
        'date': '12 ноября 2022'
    },
    {
        'name': 'Ольга Н.',
        'text': 'Мне всё лень было отзыв писать, но вот "руки дошли". Несколько раз здесь стриглась, мастера звали, кажется, Катя. Все было отлично, приятная молодая женщина и по стрижке вопросов не было)',
        'date': '5 ноября 2022'
    },
    {
        'name': 'Елена В.',
        'text': 'Делала процедуру микротоки у мастера Светланы . Светлана внимательная, приветливая, ненавязчивая. Рекомендую и мастера, и процедуру. Еще делала бровки у Татьяны , я в восторге , брови просто идеально сдеданы',
        'date': '28 октября 2022'
    },
    {
        'name': 'Виктория Г.',
        'text': 'Была на педикюре у Ольги. Очень понравилось. Все инструменты стерильные, упакованы в крафт-пакет. Для меня очень важно было. Оборудование новое.',
        'date': '13 октября 2022'
    },
]
   
masters = [
    {
        'fullname': 'Елизавета Лапина',
        'review_count': 24,
        'profession': 'Мастер маникюра',
        'work_duration': '3 г. 10 мес.',
        'photo': '/static/img/masters/master1.svg' 
    },
    {
        'fullname': 'Анастасия Сергеева',
        'review_count': 96,
        'profession': 'Парикмахер',
        'work_duration': '4 г. 9 мес.', 
        'photo': '/static/img/masters/master2.svg' 
    },
    {
        'fullname': 'Ева Колесова',
        'review_count': 18,
        'profession': 'Визажист',
        'work_duration': '1 г. 2 мес.',
        'photo': '/static/img/masters/master3.svg' 
    },
    {
        'fullname': 'Мария Суворова',
        'review_count': 32,
        'profession': 'Стилист',
        'work_duration': '1 г. 1 мес.',
        'photo': '/static/img/masters/master4.svg' 
    },
    {
        'fullname': 'Мария Суворова',
        'review_count': 32,
        'profession': 'Стилист',
        'work_duration': '1 г. 1 мес.',
        'photo': '/static/img/masters/master4.svg' 
    },
]