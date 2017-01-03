#This is the driver script for all the  models in basemoel.py for 8760
import pandas as pd
import numpy as np
import functions as fn
import basemodel as bm
import sys, os

if __name__ == '__main__':
    modelnames = {0:'Arnold'}

    if (len(sys.argv) < 2): #Check for user input error and provide usage info
        print("python3 main.py <model name>")
        print("Models:")
        for i in range(len(modelnames)):
            print(i,"-->",modelnames[i])
        raise ValueError("Exiting, not enough inputs")
    else:
        if(not(sys.argv[1] in modelnames.values())):
            raise ValueError("Model Name Not Valid")

    #load tmy data for location
    #fn.tmy(30.0,30.0)
    #fn.tmy(30.0,30.0)
