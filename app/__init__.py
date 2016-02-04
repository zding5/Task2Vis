from flask import Flask
import os
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

import csv

lda_path = os.path.join(basedir, "app/data/myd_LDA.csv")
pltm_path = os.path.join(basedir, "app/data/myd_PLTM.csv")
nb_path = os.path.join(basedir, "app/data/myd_NBB.csv")

with open(lda_path, "rb") as myd_LDA:
	reader = csv.reader(myd_LDA, delimiter=',')
	next(reader)
	lda = list(reader)

with open(pltm_path, "rb") as myd_PLTM:
	reader = csv.reader(myd_PLTM, delimiter=',')
	next(reader)
	pltm = list(reader)

with open(nb_path, "rb") as myd_NB:
	reader = csv.reader(myd_NB, delimiter=',')
	next(reader)
	nb = list(reader)


from app import views