# ISR Technical Exam

## Pre-requisites

- [Python 3.x](https://www.python.org/downloads/)

### Install dependencies

Create a virtual environment and install all python dependencies for development.

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Install the driver/s for the browser/s you want to test

You can use seleniumbase to do this, or you can manually download using the links below.

```bash
# Examples
seleniumbase install chromedriver latest
seleniumbase install geckodriver
seleniumbase install chromedriver 89
seleniumbase install chromedriver 89.0.4389.23
seleniumbase install chromedriver latest
```

### Google WebDriver

https://sites.google.com/a/chromium.org/chromedriver/downloads

### Running the test

SeleniumBase provides additional `pytest` command-line options for tests. You can go to [this link](https://github.com/seleniumbase/SeleniumBase) to learn more about SeleniumBase.

```bash
# Run the test inside the `tests/test.py` file in GUI mode. By default, without the `--gui` option, Linux will run this in headless mode.
pytest tests/test.py --inputs=inputs/isr-012.json --gui
# Use a different inputs JSON file
pytest tests/test.py --inputs=inputs/isr-010.json --gui