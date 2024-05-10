import pandas
from lib import path

PATH = path.OBSIDIAN

a = pandas.read_html(PATH/"inbox"/"Idea"/"eq.md")
