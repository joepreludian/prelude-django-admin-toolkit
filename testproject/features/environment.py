import os
from splinter import Browser


def before_all(context):

    is_headless = True if os.environ.get('HEADLESS', False) is not False else False

    context.browser = Browser('firefox', headless=is_headless)
    context.server_url = 'http://localhost:8000'

def after_all(context):
    context.browser.quit()
