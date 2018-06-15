import natnetclient as natnet

def getObjPos(ObjName):
    client = natnet.NatClient(client_ip = '127.0.0.1', data_port = 1511, comm_port = 1510)
    obj = client.rigid_bodies[ObjName]
    if obj.tracking_valid:
        return obj.position
    else:
        return None
