import argparse


def get_args():
    p = argparse.ArgumentParser(
        description='fragmentation stat required arguments!')
    p.add_argument('-i', '--indir', required=True, help='indir')
    p.add_argument(
        '-sl',
        '--samples',
        required=True,
        help='sample name list:sample_name.txt')
    p.add_argument(
        '-n',
        '--threshold',
        type=int,
        default=125,
        help='mtDNA fragment long short split threshold')
    p.add_argument(
        '-suff',
        '--suffix',
        default=".bam",
        help='bam files suffix,if bam format,index before run this script.')
    p.add_argument(
        '-o',
        '--outdir',
        required=True,
        help='outdir,for example:mis_10_splitedBy125')
    p.add_argument(
        '-bz',
         '--baseline', 
         default=None, 
         help='z-scored baseline data')
    p.add_argument(
        '-bs',
        '--smothed',
        default=None,
        help=' smothed z-scored baseline data')
    p.add_argument(
        '-bp', 
        '--peaks', 
        default=None, 
        help='baseline peaks feature')
    p.add_argument(
        '-exp',
        '--exp',
        action='store_false',
        help='check what kind of input:experiment or baseline data.')

    args = p.parse_args()

    return args