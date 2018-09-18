for file in `ls ./content`
do
 cat ./templates/top.html ./templates/header.html ./content/$file ./templates/bottom.html > ./docs/$file
done
echo "done"