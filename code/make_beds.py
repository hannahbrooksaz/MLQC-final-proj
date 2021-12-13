import re

###
dataset_path = './canonical_dataset.txt'
###

def makeBeds(which):
    
    if which == 'train':
        suffix = 'train'
        CHROM_GROUP = ['chr11', 'chr13', 'chr15', 'chr17', 'chr19', 'chr21',
                       'chr2', 'chr4', 'chr6', 'chr8', 'chr10', 'chr12',
                       'chr14', 'chr16', 'chr18', 'chr20', 'chr22', 'chrX', 'chrY']
    elif which == 'test':
        suffix = 'test'
        CHROM_GROUP = ['chr1', 'chr3', 'chr5', 'chr7', 'chr9']
    else:
        suffix = 'all'
        CHROM_GROUP = ['chr1', 'chr3', 'chr5', 'chr7', 'chr9',
                       'chr11', 'chr13', 'chr15', 'chr17', 'chr19', 'chr21',
                       'chr2', 'chr4', 'chr6', 'chr8', 'chr10', 'chr12',
                       'chr14', 'chr16', 'chr18', 'chr20', 'chr22', 'chrX', 'chrY']
        
    roi_out = open('roi_'+suffix+'.bed', 'w')
    sites_out = open('sites_'+suffix+'.bed', 'w')

    with open(dataset_path) as f:
        for line in f.readlines():
            data = re.split('\n|\t', line)

            if (data[2] in CHROM_GROUP and data[1] == '1'):
                roi_out.write(data[2]+'\t'+data[4]+'\t'+data[5]+'\n')

                for start_coord_set in data[6::2]:
                    if len(start_coord_set) > 0:
                        for start_coord in start_coord_set.split(','):
                            if len(start_coord) > 0:
                                sites_out.write(data[2]+'\t'+
                                                str(int(start_coord))+'\t'+
                                                str(int(start_coord)+1)+'\t'+
                                                '.\t1\n')

                for end_coord_set in data[7::2]:
                    if len(end_coord_set) > 0:
                        for end_coord in end_coord_set.split(','):
                            if len(end_coord) > 0:
                                sites_out.write(data[2]+'\t'+
                                                str(int(end_coord))+'\t'+
                                                str(int(end_coord)+1)+'\t'+
                                                '.\t2\n')
        
    roi_out.close()
    sites_out.close()

    print('done with '+suffix)

makeBeds('train')
makeBeds('test')
