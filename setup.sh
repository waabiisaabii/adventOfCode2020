DAY=${1:=0}
DIR="day_$DAY"

mkdir $DIR
touch $DIR/input.txt
touch $DIR/sample.txt
touch $DIR/README.md
touch $DIR/solve.py

echo "- [ ] [$DIR]($DIR)" >> README.md
