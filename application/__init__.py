from flask import Flask
import os


app = Flask(__name__)


from application.controller import homer_controller