import pandas as pandas
import numpy as numpy
import os
import re
from neo4j import GraphDatabase
from neo4j_connection import *
from preprocessing_human import *



def create_request():
	return 0



def clear_csv(file_name):
	file_path=get_path()+'/data/'+file_name
	uncleared_links=pd.read_csv(file_path)
	





if __name__ == '__main__':