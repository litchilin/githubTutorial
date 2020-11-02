#!/mnt/lustre2/BI_Tools/tools/anaconda2/bin/python
import re
##from datetime import datetime
##startTime=datetime.now()

#fpath='/mnt/lustre2/BI_Analysis/Training/jean/ref/chroms/hg38.fa'
fpath='C:/Users/Min-Chin/Desktop/toyForM.fa'
with open(fpath, 'r') as fa:
	faCon=fa.read()
noN=re.sub('\n','',faCon)
print(noN+'\n')
noM=re.sub('>chrM\w*>{1}','>',noN)
print(noM+'\n')
seq=re.sub('>\w+\d+','',noM)
#\w all characters marked as letters in Unicode
print(seq)
#test github     
##
##nuts=['[Aa]', '[Tt]', '[Cc]', '[Gg]']#element==regx
##nutA=len(re.findall(nuts[0], seq))
##nutT=len(re.findall(nuts[1], seq))
##nutC=len(re.findall(nuts[2], seq))
##nutG=len(re.findall(nuts[3], seq))
##slashN=seq.count('\n')
##
##wbp=len(seq)-slashN
##freqA=format(nutA/wbp*100, '.10f')
##freqT=format(nutT/wbp*100, '.10f')
##freqC=format(nutC/wbp*100, '.10f')
##freqG=format(nutG/wbp*100, '.10f')
##print([type(nutA), nutT, nutC, nutG, slashN])
##print([freqA, freqT, freqC, freqG, type(wbp)])
##
##print(datetime.now()-startTime)
