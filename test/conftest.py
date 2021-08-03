def pytest_addoption(parser):
    parser.addoption("--inputs", action="store", default="input.json")