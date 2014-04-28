#$HADOOP_HOME/bin/hadoop fs -get /tmp/enron/output3/values/part-m-000$n .
for ((  i = 12 ;  i <= 65;  i++  ))
do
  $HADOOP_HOME/bin/hadoop fs -get /tmp/enron/output3/values/part-m-000$i .
done
