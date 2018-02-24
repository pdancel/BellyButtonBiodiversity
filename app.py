# import necessary libraries
from sqlalchemy import func
import datetime as dt
import numpy as np
import pandas as pd
import json

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__, static_folder="static")

#################################################
# Flask Routes
#################################################

# Names route
@app.route("/names")
def names():
    data_samples = pd.read_csv('DataSets/belly_button_biodiversity_samples.csv')
    data_samples.reset_index(drop=True)
    sample_names = data_samples.drop('otu_id', 1)
    sample_names_list = list(sample_names.columns.values)
    return jsonify(sample_names_list)


#OTU Descriptions Route
@app.route('/otu')  
def otu():
    data_otu_id = pd.read_csv('DataSets/belly_button_biodiversity_otu_id.csv')
    data_otu_id.set_index('otu_id')
    otu_description = data_otu_id['lowest_taxonomic_unit_found']
    otu_description_list = otu_description.tolist()
    return jsonify(otu_description_list)
 

#MetaData Route
#@app.route('/metadata/<sample>')
@app.route('/metadata')
def meta():
    data_meta = pd.read_csv('DataSets/Belly_Button_Biodiversity_Metadata.csv')
    data_meta_list = data_meta[['AGE', 'BBTYPE', 'ETHNICITY', 'GENDER', 'LOCATION', 'SAMPLEID']].values.tolist()
    return jsonify(data_meta_list)


# @app.route('/wfreq/<sample>')  
@app.route('/wfreq')   
def wfreq():
    data_wfreq = data_meta['WFREQ']
    data_wfreq_dropna = data_wfreq[data_wfreq > 0]
    data_wfreq_list = data_wfreq_dropna.tolist()
    return jsonify(data_wfreq_list)


