#echo $1 #command line arg
len=$(expr ${#1} - 4) # arithmetic expressions
#len = $(expr ${#1} - 4)
name=${1:0:$len}
#echo $len
ext=".cpp"
comment="_comment_removal.cpp"
process="_final_processed.cpp"



python comment_removal.py "$name$ext";
python preprocess.py "$name$comment";
python parse3.py "$name$process";
