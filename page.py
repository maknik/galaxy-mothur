import sys, shutil
import os, os.path
import tempfile

f1=open(sys.argv[1])
f2=open(sys.argv[2])
f3=sys.argv[3]
f4=sys.argv[4]
f5=sys.argv[5]
f6=sys.argv[6]
f7=open(sys.argv[7])
output_extra_html=sys.argv[8]
output_extra_path = sys.argv[9]
tmp_dir = tempfile.mkdtemp()

def open_binary_data(inp,name):
	filename = os.path.join( tmp_dir, '%s' % name )
	out=open(filename, 'w')
	tmp=open(inp, 'rb')
	for line in tmp:
		out.write(line)
	out.close()
	
def string(string,out):
	out.write(string)

def summary(inp, s1, s2, ns,out):
	tmp=[]
	for line in inp:
		tmp.append(line)
	
	tmp[40]=tmp[40].split(	)[0]+"\t\t"+tmp[40].split(	)[1]+"\t"+tmp[40].split(	)[2]+"\t"+tmp[40].split(	)[3]+"\t"+tmp[40].split(	)[4]+"\t"+tmp[40].split(	)[5]+"\n"

	l_sekw=tmp[41].split(	)[ns]
	string("<h2>"+s1,out)
	string(l_sekw,out)
	string(s2+"</h2>\n",out)

	for i in tmp[32:42]:
		string(i,out)

def data(inp,title,out):
	string("<h2><a href="+inp+" style='text-decoration: none'>"+title+"</a></h2>",out)

out_html=open(output_extra_html, 'w')
os.mkdir( output_extra_path )

string('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">',out_html)
string('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pl" lang="pl"><head><title>Mothur analysis page</title></head>\n\n<body>\n\n<pre>\n',out_html)
string("<h1>Prezentacja przeprowadzonej analizy</h1>\n",out_html)

name1='tree.svg'
name2='taxonomy.txt'
name3='otu_tax_summary.txt'
name4='rarefacion_curve.pdf'


open_binary_data(f3,name1)
open_binary_data(f4,name2)
open_binary_data(f5,name3)
open_binary_data(f6,name4)

summary(f1, "Summary.seqs on primary dataset containing ", " sequences", 3,out_html)
summary(f2, "Summary.seqs on dataset containing ", " sequences after removing errors", 4,out_html)

string("<a>The summary.seqs command summarize the quality of sequences.</a>")

for filename in sorted( os.listdir( tmp_dir ) ):
        shutil.move( os.path.join( tmp_dir, filename ), os.path.join( output_extra_path, filename ) )

data(name1,"Phylogenetic tree",out_html)

string("<a>Neighbor joining tree.</a>")

data(name2,"Sequence Taxonomy",out_html)

string("<a>File contains a taxonomy string for each sequence</a>")

data(name3,"Summary of OTU Taxonomy",out_html)

string("<a>The first column indicates the taxonomic level in the outline. Obviously, the Root is the highest one can go. The second column indicates the 'pedigree' for each lineage. The third column is the name of the lineage. Column four indicates the number of children lineages that the current lineage has. Finally, the last column indicates the number of sequences that were found in that lineage.</a>")

data(name4,"Rarefaction curve",out_html)

string("<a>Curve describing the number of OTUs observed as a function of sampling effort</a>")

string("<h2>Summary.single with rate of coverage and biodiversity</h2>\n",out_html)

for line in f7:
	string(line,out_html)

string("<a>Table containing the sample coverage and the invsimpson diversity estimate</a>")

string("</pre>\n</body>\n</html>\n",out_html)

out_html.close()
os.rmdir( tmp_dir )
