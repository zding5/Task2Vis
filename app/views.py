from flask import render_template, flash, redirect, url_for
from app import app, lda, pltm, nb

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html', LDAlist=lda, PLTMlist=pltm, NBlist=nb)