from nameko.standalone.rpc import ClusterRpcProxy

from project import settings


broker_cfg = {'AMQP_URI': settings.AMQP_URI}

with ClusterRpcProxy(broker_cfg) as rpc:
    # Async
    rpc.mail.send.call_async(["dyohan9@gmail.com"], "testing", "Just testing")
    # Sync
    # rpc.mail.send(["dyohan9@gmail.com"], "testing", "Just testing")
