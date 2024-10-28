from app import process_query


def test_knows_about_dinosaurs():
    dino = "Dinosaurs ruled the Earth 200 million years ago"
    assert process_query("dinosaurs") == dino


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_query_return_name():
    assert process_query("What is your name?") == "The Scottish Swiss German"


def test_query_addition():
    assert process_query("What is 2 plus 4?") == 6