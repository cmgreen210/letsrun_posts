import org.apache.spark._
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import org.apache.spark.SparkConf
import java.nio.file.{Paths, Files}
import java.nio.charset.StandardCharsets

object LetsRunGraph {
    def main(args: Array[String]) {
        val graph_path = "/home/christopher/letsrun_posts/output/post_graph.txt";
        val author_path = "/home/christopher/letsrun_posts/output/idx2auth.txt";
        val rank_out = "/home/christopher/letsrun_posts/output/rank.txt";

        val conf = new SparkConf().setAppName("LetsRun Graph")
        val sc = new SparkContext(conf)

        val g = GraphLoader.edgeListFile(sc, graph_path)

        val ranks = g.pageRank(0.0001).vertices

        val authors = sc.textFile(author_path).map { line =>
            val fields = line.split("\t")
            (fields(0).toLong, fields.slice(1, fields.length).mkString("\t"))
        }

        val authorRank = authors.join(ranks).map {
            case (id, (author, rank)) => (author, rank)
        }

        val sortAuthorRank = authorRank.sortBy(c => c._2, false)
        println(sortAuthorRank.collect.slice(0, 20).mkString("\n"))

        Files.write(Paths.get(rank_out), sortAuthorRank.collect.mkString("\n").getBytes(StandardCharsets.UTF_8))
    }
}
