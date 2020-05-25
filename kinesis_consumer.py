import time
from kinesis_create_stream import Kinesis

k_client = Kinesis().kinesis

 
shard_id = 'shardId-000000000000' # we only have one shard!
shard_it = k_client.get_shard_iterator(StreamName="ba-d",
                                       ShardId=shard_id,
                                       ShardIteratorType="LATEST")["ShardIterator"]

while True:
    out = k_client.get_records(ShardIterator = shard_it, Limit=2)

    shard_it = out["NextShardIterator"]
    print (out)
    time.sleep(0.2)
