from pipeline.load_data import load_data

def test_load_data():
    data = load_data("data/iris.csv")
    assert not data.empty
