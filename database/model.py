"""
Модуль для роботи з даними про країни.
Містить функції для отримання інформації про країни.
"""

# Дані про країни (може бути замінено на БД)
COUNTRIES_DATA = [
    {
        'id': 1,
        'name': 'Ukraine',
        'image': 'static\image\unnamed.jpg',
        'capital': 'Kyiv',
        'population': '41,167,000',
        'area': '603,500 km²',
        'language': 'Ukrainian',
        'description': 'Ukraine is a country in Eastern Europe with rich natural beauty and cultural heritage.'
    },
    {
        'id': 2,
        'name': 'Poland',
        'image': 'static\image\polska.jpg',
        'capital': 'Warsaw',
        'population': '37,840,000',
        'area': '312,696 km²',
        'language': 'Polish',
        'description': 'Poland is a country in Central Europe with vibrant culture and history.'
    },
    {
        'id': 3,
        'name': 'Germany',
        'image': 'images\png-transparent-flag-of-germany-german-grammar-medizin-germany-word-red.png',
        'capital': 'Berlin',
        'population': '83,370,000',
        'area': '357,022 km²',
        'language': 'German',
        'description': 'Germany is a country in Central Europe known for engineering and culture.'
    },
    {
        'id': 4,
        'name': 'France',
        'image': 'static\image\pngimg.com - flags_PNG14627.png',
        'capital': 'Paris',
        'population': '67,970,000',
        'area': '643,801 km²',
        'language': 'French',
        'description': 'France is a country in Western Europe famous for art, wine, and cuisine.'
    },
    {
        'id': 5,
        'name': 'Italy',
        'image': 'images\png-transparent-flag-of-italy-graphy-italy-flag-photography-flag-of-the-united-states-thumbnail.png',
        'capital': 'Rome',
        'population': '59,110,000',
        'area': '301,340 km²',
        'language': 'Italian',
        'description': 'Italy is a country in Southern Europe with rich history and art.'
    },
    {
        'id': 6,
        'name': 'Spain',
        'image': 'images\Flag_map_of_Spain.svg.png',
        'capital': 'Madrid',
        'population': '47,560,000',
        'area': '505,990 km²',
        'language': 'Spanish',
        'description': 'Spain is a country in Southwestern Europe with beautiful landscapes.'
    },
    {
        'id': 7,
        'name': 'United Kingdom',
        'image': 'images\png-transparent-flag-of-the-united-kingdom-england-map-england-flag-world-united-kingdom-thumbnail.png',
        'capital': 'London',
        'population': '67,530,000',
        'area': '242,495 km²',
        'language': 'English',
        'description': 'The United Kingdom is a country in Western Europe with royal heritage.'
    },
]


def get_countries():
    """
    Отримує список всіх країн.
    
    Returns:
        list: Список словників з даними про країни
    """
    return COUNTRIES_DATA


def get_country_by_id(country_id):
    """
    Отримує країну по ID.
    
    Args:
        country_id (int): ID країни
        
    Returns:
        dict: Словник з даними про країну або None якщо країна не знайдена
    """
    for country in COUNTRIES_DATA:
        if country['id'] == country_id:
            return country
    return None


def search_countries(query):
    """
    Шукає країни по назві.
    
    Args:
        query (str): Текст для пошуку
        
    Returns:
        list: Список країн що відповідають пошуку
    """
    query = query.lower()
    return [
        country for country in COUNTRIES_DATA
        if query in country['name'].lower() or query in country['description'].lower()
    ]
