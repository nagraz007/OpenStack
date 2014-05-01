#! /bin/bash


#ENVIRONMENT SETTINGS
HDFS_HOST=hdfs://master:54310
INPUT_DIR=$1
OUTPUT_DIR=$2
EDGE_INPUT_PATH=$HDFS_HOST$INPUT_DIR
OUTPUT_PATH=$HDFS_HOST$OUTPUT_DIR
OUTPUT_PATH_SUB_DIR=$OUTPUT_PATH/values
WORKERS=59
MEMORY=2g
ZK_LIST=master:2181
TIMEOUT=600000
ZK_TIMEOUT=600000


#VARIABLE JOB SETTINGS
#PIVOT_BATCH is a testing param that allows you to manually set the first batch of pivots to be chosen.
#PIVOT_BATCH=1,2,3
OUT_OF_CORE_GRAPH=false
OUT_OF_CORE_MESSAGES=false
SHORTEST_PATH_PHASES=1
PIVOT_BATCH_SIZE=$4
INITIAL_BATCH_SIZE=3
VERTEX_COUNT=$7
RESULT_SET_SIZE=$3
SET_STABILITY_CUTOFF=$5
SET_STABILITY_COUNTER=$6
COMPUTE_THREADS=1

#CONSTANT JOB SETTINGS
JAR=high-betweenness-set-extraction-1.0.jar
MASTER_COMPUTE=com.soteradefense.betweenness.giraph.compute.HBSEMasterCompute
VERTEX=com.soteradefense.betweenness.giraph.compute.HBSEVertexComputation
EDGE_INPUT_FORMAT=com.soteradefense.betweenness.giraph.io.HBSEEdgeInputFormat
OUTPUT_FORMAT=com.soteradefense.betweenness.giraph.io.HBSEOutputFormat

echo
echo running jar $JAR
echo computing with vertex class: $VERTEX
echo I/O input: $EDGE_INPUT_PATH output $OUTPUT_PATH
echo I/O input format: $EDGE_INPUT_FORMAT
echo I/O output format: $OUTPUT_FORMAT
echo pivot.batch.size=$PIVOT_BATCH_SIZE
echo vertex.count=$VERTEX_COUNT
echo giraph workers: $WORKERS
echo Zoo Kepper List: $ZK_LIST
echo Zoo Keeper Timeout: $ZK_TIMEOUT
echo giraph.useOutOfCoreGraph: $OUT_OF_CORE_GRAPH
echo giraph.useOutOfCoreMessages: $OUT_OF_CORE_MESSAGES

echo Deleting output directory $OUTPUT_PATH
$HADOOP_HOME/bin/hadoop fs -rmr $OUTPUT_PATH
echo

$HADOOP_HOME/bin/hadoop jar $JAR org.apache.giraph.GiraphRunner -Dgiraph.numComputeThreads=$COMPUTE_THREADS -Dgiraph.useSuperstepCounters=false -Dmapred.map.child.java.opts=-Xmx$MEMORY  -Dgiraph.useOutOfCoreGraph=$OUT_OF_CORE_GRAPH -Dgiraph.useOutOfCoreMessages=$OUT_OF_CORE_MESSAGES $VERTEX -w $WORKERS -mc $MASTER_COMPUTE -eif $EDGE_INPUT_FORMAT -eip $EDGE_INPUT_PATH -vof $OUTPUT_FORMAT -op $OUTPUT_PATH_SUB_DIR -ca betweenness.shortestpath.phases=$SHORTEST_PATH_PHASES -ca mapred.task.timeout=$TIMEOUT -ca pivot.batch.size=$PIVOT_BATCH_SIZE -ca pivot.batch.size.initial=$INITIAL_BATCH_SIZE -ca vertex.count=$VERTEX_COUNT -ca betweenness.set.maxSize=$RESULT_SET_SIZE -ca betweenness.set.stability=$SET_STABILITY_CUTOFF -ca betweenness.set.stability.counter=$SET_STABILITY_COUNTER -ca betweenness.output.dir=$OUTPUT_DIR -ca pivot.batch.string=$PIVOT_BATCH

