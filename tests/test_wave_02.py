import pytest
from viewing_party.party import *
from tests.test_constants import *

def test_calculates_watched_average_rating():
    # Arrange
    janes_data = clean_wave_2_data()

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(3.58333)
    assert janes_data == clean_wave_2_data()


def test_empty_watched_average_rating_is_zero():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(0.0)

def test_calculates_watched_average_rating():
    # Arrange
    janes_data = {
        "watched": [{   'genre': 'Fantasy',
                       'host': 'netflix',
                       'rating':None,
                       'title': 'The Lord of the Functions: The Fellowship of '
                                'the Function'},
                   {   'genre': 'Fantasy',
                       'host': 'netflix',
                       'rating': "string",
                       'title': 'The Lord of the Functions: The Two '
                                'Parameters'},
                    { 'genre': 'Fantasy',
                       'host': 'amazon',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Return of the '
                                'Value'}]
    } 

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == 4.0
    
def test_most_watched_genre():
    # Arrange
    janes_data = clean_wave_2_data()

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Fantasy"
    assert janes_data == clean_wave_2_data()

def test_most_watched_genre_order_mixed():
    # Arrange
    janes_data = clean_wave_2b_data()

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Fantasy"
    assert janes_data == clean_wave_2b_data()

def test_genre_is_None_if_empty_watched():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == None
