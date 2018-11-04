# use shell script to move all practice code to single file
for (( i = 1; i <= 10; i++ )); do
	cat adrian-$i.py >> summary.py
done