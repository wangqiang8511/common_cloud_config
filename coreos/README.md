# Introduction

Cloud Config file for coreos.

Setup docker, fannel on coreos.

Tested with coreos 522.6.0, flannel 0.2.0.


# How to use.

Replace the following settings in cloud\_config\_flannel.

etcd\_server: your productio etcd server
etcd\_port: your production etcd server port
cluster\_name: name of your cluster, will be registered in etcd for flannel
flannel\_download\_uri: download url for your built flannel 
cluster\_cidr: cidr used for your cluster. Example: 10.244.0.0/16
