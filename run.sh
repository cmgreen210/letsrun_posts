$SPARK_HOME/bin/spark-submit \
     --master local[4] \
     spark/python/post_script.py

 cd spark/scala
 sbt package

 $SPARK_HOME/bin/spark-submit \
     --class "LetsRunGraph" \
     --master local[4] \
     target/scala-2.10/letsrun-pagerank_2.10-1.0.jar
