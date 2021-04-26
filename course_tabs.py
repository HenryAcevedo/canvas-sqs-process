#
# Henry Acevedo
#
# Purpose: Set default course navigation
#

from canvasapi import Canvas
from canvasapi import exceptions
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
MYURL = config.get('instance', 'prod')
MYTOKEN = config.get('auth', 'token')

canvas = Canvas(MYURL, MYTOKEN)


def set_default_navigation(course_id):
    pos = 2
    try:
        course = canvas.get_course(course_id)
    except exceptions.ResourceDoesNotExist as e:
        return

    tabs = course.get_tabs()
    for tab in tabs:
        # print(tab.id)
        if tab.id == 'home' or tab.id == 'settings':
            pass
        elif tab.id == 'announcements' or tab.id == 'modules' or tab.id == 'grades' or tab.id == 'people':
            tab.update(hidden=False, position=pos)
            pos += 1
        else:
            tab.update(hidden=True)


def main():
    print("Running as main")


if __name__ == "__main__":
    main()
