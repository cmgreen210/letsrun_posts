from pyspark.sql import SQLContext
import codecs


def get_sql_context(sc):
    return SQLContext(sc)


def get_posts(path, sc):
    sql_context = get_sql_context(sc)
    return sql_context.jsonFile(path)


def create_author_map(posts):
    id_2_idx = {}
    idx_2_id = {}
    id_count = 0
    for x in posts.collect():
        if x.post_author not in id_2_idx:
            id_2_idx[x.post_author] = id_count
            idx_2_id[id_count] = x.post_author
            id_count += 1

    return id_2_idx, idx_2_id


def create_reply_graph(path, posts, auth2id):
    with open(path, 'w') as fp:
        for post in posts.collect():
            if post.reply_to_author is not None:
                if post.reply_to_author in auth2id:
                    fp.write('{0}\t{1}\n'.format(
                        auth2id[post.post_author],
                        auth2id[post.reply_to_author]
                    ))
    fp.close()


def write_dictionary(path, d, sep=u'\t'):
    with codecs.open(path, 'w', 'utf8') as fp:
        for k, v in d.iteritems():
            fp.write(u'{0}'.format(k) + sep + u'{0}'.format(v))
