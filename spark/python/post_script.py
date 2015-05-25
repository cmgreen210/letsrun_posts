from post_graph import *
from pyspark import SparkContext
from os.path import join as pjoin


input = "/home/christopher/letsrun_posts_20150525.json"
outdir = "/home/christopher/letsrun_posts/output/"

sc = SparkContext()
posts = get_posts(input, sc)

auth2idx, idx2auth = create_author_map(posts)

write_dictionary(pjoin(outdir, 'auth2idx.txt'), auth2idx)
write_dictionary(pjoin(outdir, 'idx2auth.txt'), idx2auth)

create_reply_graph(pjoin(outdir, 'post_graph.txt'), posts, auth2idx)
