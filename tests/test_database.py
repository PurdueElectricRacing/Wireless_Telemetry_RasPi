import sys
import os
import pytest
import mysql.connector
import pathmagic  # noqa
from database import Database


db = Database()


class TestDatabase:

    # Ensure the connection can be made to the database
    def test_connection(self):
        db.connect()

    def test_cursor(self):
        db.get_cursor()
