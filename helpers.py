from bs4 import BeautifulSoup
import os
import requests

def case_name_to_folder(name):
    """Convert name of case to case folder."""
    return name.replace('/', '_')

def case_folder_to_name(folder_name):
    """Convert name of case folder to case name."""

    return folder_name.replace('_', '/')
def create_folder_if_not_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def crawl(url):
    """Crawl a specific url and return the soup.
    """
    req = requests.get(url)
    req.encoding = 'utf-8' # force utf-8 encoding
    soup = BeautifulSoup(req.text, 'html.parser')
    return soup

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        response.raise_for_status()

def strip_js_window_open(js):
    """Strips the javascript window.open function from 
    a link.
    """
    function_start = js.find('window.open(')
    function_end = js.find(');')
    arguments = js[function_start:function_end]
    broken = arguments.split(',')
    link = broken[0].split('(')[1:]
    link = '('.join(link)
    link = link[1:-1]
    return link