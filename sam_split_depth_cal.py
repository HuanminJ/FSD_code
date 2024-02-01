import os, sys, subprocess
import pysam


def long_short_split(sample_path, sample_name_list, suffix, n, outdir):
    output1 = os.path.join(sample_path, outdir, 'splited_sam_file')
    output2 = os.path.join(sample_path, outdir, 'depth_file')
    os.makedirs(output1, exist_ok=True)
    os.makedirs(output2, exist_ok=True)
    sample_name_list_path = os.path.join(sample_path, sample_name_list)
    f = open(sample_name_list_path)
    sample_names = f.readlines()
    total_sample = 0
    for i in sample_names:
        i = i.strip()
        if os.path.getsize(os.path.join(sample_path, i, i + suffix)) > 1:
            item_sam_file_path = os.path.join(sample_path, i, i + suffix)
            print(i + suffix)
            shortr = os.path.join(output1, i + f'.S{n}.sam')
            longr = os.path.join(output1, i + f'.L{n}.sam')
            sam_ali = pysam.AlignmentFile(item_sam_file_path, 'rb')

            sam_S = pysam.AlignmentFile(shortr, 'w', template=sam_ali)
            sam_L = pysam.AlignmentFile(longr, 'w', template=sam_ali)
            #             sam_ali_fetch = sam_ali.fetch()
            for read in sam_ali:
                insert_size = abs(int(read.template_length))
                if insert_size < n:
                    sam_S.write(read)
                elif insert_size >= n:
                    sam_L.write(read)

            sam_ali.close()
            sam_S.close()
            sam_L.close()
            total_sample += 1
            if os.path.getsize(shortr) > 1000 and os.path.getsize(longr) > 1000:
                depth_short = os.path.join(sample_path, output2,
                                           f"{i}.S{n}.sam.txt")
                depth_long = os.path.join(sample_path, output2,
                                           f"{i}.L{n}.sam.txt")
                os.system(
                    f'samtools depth -d 500000000 -a -m 0 {shortr} > {depth_short}'
                )
                os.system(
                    f'samtools depth -d 500000000 -a -m 0 {longr} > {depth_long}'
                )
            else:
                print(f'{i}+.S{n}.sam or {i}+.S{n}.sam too small and skipped!')
        else:
            print(i + f'{suffix} too small and skipped!')
    if total_sample == len(sample_names):
        print('All samples have been processed')

    f.close()


def run():
    sample_path = sys.argv[1]
    sample_name_list = 'sample_name.txt'
    n = 125
    suffix = ".mis.10.bam"
    long_short_split(sample_path, sample_name_list, n, suffix)


if __name__ == '__main__':
    run()