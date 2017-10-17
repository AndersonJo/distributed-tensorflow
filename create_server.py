import tensorflow as tf
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--task', type=int, help='The task number')
parser.add_argument('--job', type=str, default='worker', help='job name ("worker" or "host")')
args = parser.parse_args()

cluster_spec = json.load(open('config.json', 'rt'))
cluster = tf.train.ClusterSpec(cluster_spec)
server = tf.train.Server(cluster, job_name=args.job, task_index=args.task)
server.start()
server.join()
