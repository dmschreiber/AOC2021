if [ "$#" -eq 1 ]
then
	echo "" > ./data/day$1.txt
	echo "" > ./data/day$1_test.txt
	cp ./day.py ./day$1.py
else
	echo "Need which day"
	exit 1
fi

