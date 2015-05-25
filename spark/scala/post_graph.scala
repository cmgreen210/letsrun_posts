import org.apache.spark._
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD

val graph_path = "/home/christopher/letsrun_posts/output/post_graph.txt"
val g = GraphLoader.edgeListFile(sc, graph_path)

val ranks = g.pageRank(0.0001).vertices

val author_path = "/home/christopher/letsrun_posts/output/idx2auth.txt"
val authors = sc.textFile(author_path).map { line =>
    val fields = line.split("\t")
    (fields(0).toLong, fields.slice(1, fields.length).mkString("\t"))
}