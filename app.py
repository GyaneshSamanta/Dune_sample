from requests import get, post
import pandas as pd 
from credentials import keys
import os 
from flask import Flask, redirect, render_template, request, url_for 
import time 
from urlgen import make_api_url
API_key = keys()

Query_ID = "" 

BASE_URL = "https://api.dune.com/api/v1/"

app = Flask(__name__)




