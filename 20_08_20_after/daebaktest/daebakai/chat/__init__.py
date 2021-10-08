from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash

chat = Blueprint('chat', __name__,url_prefix='/chat')

from . import routes, events
