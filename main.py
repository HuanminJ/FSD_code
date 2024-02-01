import os,sys,argparse,subprocess, glob
import pysam
from myargs_parse import get_args
from sam_split_depth_cal import long_short_split
import pandas as pd
from functools import reduce
import numpy as np
import fsd_feature_cal
from fsd_cal import FSD_Cal

def run_all():
    #run args_get()
    print("Arguments parsing>>>>")
    args = get_args()
    print("Done!")
    #run long shang short fragment split 
    print("Starting split fragments and compute depth>>>")
    long_short_split(sample_path=args.indir,sample_name_list=args.samples,suffix =args.suffix,n=args.threshold,outdir=args.outdir)
    #compute fsd and fsd_feature
    print("Done!")
    print("Starting compute fsd and features>>>")
    my_fsd_feature = FSD_Cal(sample_path=args.indir,target_path=args.outdir,n=args.threshold)
    my_fsd_feature.runAll(bz=args.baseline,bs=args.smothed,bp=args.peaks,exp=args.exp)
    print("Finished!!!")

if __name__ == "__main__":
    run_all()
