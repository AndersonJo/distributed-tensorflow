# distributed-tensorflow
Distributed Tensorflow Example


# Example 

## Configuration
configure "config.json" file before running codes. <br>
The example requires at least two remote servers and each remote server has its own GPU. <br>

## Create TensorFlow Server

In remote server 1... 
```
python3 create_server.py --task=0
```

In remote server 2...
```
python3 create_server.py --task=1
```

## Run computation code

```
python3 compute_simple.py
```
