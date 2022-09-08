from pysnmp.hlapi import *

iterator = " "
salida = " "


# Funcion para obtener un getSNMP v1 y v2c
def getSNMPv1v2c(version, comunidad, host, OID):
    global iterator
    global salida
    if version == 1:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=0),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID))
        )
    elif version == 2:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(comunidad),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID))
        )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))

    return salida


# Funcion para obtener un getSNMP v1 y v2c
def getNextSNMPv1v2c(version, comunidad, host, OID):
    global iterator
    global salida
    if version == 1:
        iterator = nextCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=0),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID))
        )
    elif version == 2:
        iterator = nextCmd(
            SnmpEngine(),
            CommunityData(comunidad),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID))
        )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))

    return salida


# Funcion para obtener un getSNMP v1 y v2c
def setSNMPv1v2c(version, comunidad, host, OID, valor):
    global iterator
    global salida
    if version == 1:
        iterator = setCmd(
            SnmpEngine(),
            CommunityData(comunidad, mpModel=0),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID), valor)
        )
    elif version == 2:
        iterator = setCmd(
            SnmpEngine(),
            CommunityData(comunidad),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(OID), valor)
        )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))

    return salida
