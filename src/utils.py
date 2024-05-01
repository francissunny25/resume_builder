import os
import sys

from src.logger import logging
from src.exception import CustomException

from bs4.element import Doctype, NavigableString

def html_to_json(tag):
    try:
        if not tag:
            return None
        if isinstance(tag, slice):
            return {
                
            }
        if isinstance(tag, Doctype):
            return {
                "type": "doctype",
                "name": tag.name,
            }
        if isinstance(tag, NavigableString):
            return str(tag)
        return {
            "tag": tag.name,
            "attrs": dict(tag.attrs),
            "text": tag.string,
            "children": [html_to_json(child) for child in tag.children]
        }
    except Exception as e:
        raise CustomException(e,sys)
    