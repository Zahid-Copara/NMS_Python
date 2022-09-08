from pysnmp.hlapi import *
from pysnmp.hlapi import UsmUserData

salida = " "
iterator = " "


# //Funciones para enviar una peticion GET
# Funcion para nivel de seguridad noAuthNoPriv
def getSNMPv3noAuthNoPriv(usuario, host, oid):
    global salida
    global iterator
    iterator = getCmd(
        SnmpEngine(),
        UsmUserData(usuario),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida


# Funcion para nivel de seguridad noAuthNoPriv
def getSNMPv3AuthNoPriv(usuario, host, oid, protocoloAuth, llaveAuth):
    global salida
    global iterator
    if protocoloAuth == "MD5":
        iterator = getCmd(
            SnmpEngine(),
            UsmUserData(usuario, llaveAuth),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
    elif protocoloAuth == "SHA":
        iterator = getCmd(
            SnmpEngine(),
            UsmUserData(usuario, llaveAuth, authProtocol=usmHMACSHAAuthProtocol),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida


# Funcion para get SNMP v3 authPriv
def getSNMPv3AuthPriv(usuario, host, oid, protocoloAuth, llaveAuth, protocoloPriv, llavePriv):
    global salida
    global iterator
    if protocoloAuth == "MD5":
        if protocoloPriv == "DES":
            iterator = getCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACMD5AuthProtocol,
                            privProtocol=usmDESPrivProtocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )
        elif protocoloPriv == "AES":
            iterator = getCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACMD5AuthProtocol,
                            privProtocol=usmAesCfb128Protocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )
    elif protocoloAuth == "SHA":
        if protocoloPriv == "DES":
            iterator = getCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACSHAAuthProtocol,
                            privProtocol=usmDESPrivProtocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )
        elif protocoloPriv == "AES":
            iterator = getCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACSHAAuthProtocol,
                            privProtocol=usmAesCfb128Protocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida


# //Funciones para enviar una peticion GET NEXT
# Funcion para nivel de seguridad noAuthNoPriv
def getNextSNMPv3noAuthNoPriv(usuario, host, oid):
    global salida
    global iterator
    iterator = nextCmd(
        SnmpEngine(),
        UsmUserData(usuario),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida


# Funcion para nivel de seguridad noAuthNoPriv
def getNextSNMPv3AuthNoPriv(usuario, host, oid, protocoloAuth, llaveAuth):
    global salida
    global iterator
    if protocoloAuth == "MD5":
        iterator = nextCmd(
            SnmpEngine(),
            UsmUserData(usuario, llaveAuth),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
    elif protocoloAuth == "SHA":
        iterator = nextCmd(
            SnmpEngine(),
            UsmUserData(usuario, llaveAuth, authProtocol=usmHMACSHAAuthProtocol),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida


# Funcion para get SNMP v3 authPriv
def getNextSNMPv3AuthPriv(usuario, host, oid, protocoloAuth, llaveAuth, protocoloPriv, llavePriv):
    global salida
    global iterator
    if protocoloAuth == "MD5":
        if protocoloPriv == "DES":
            iterator = nextCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACMD5AuthProtocol,
                            privProtocol=usmDESPrivProtocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )
        elif protocoloPriv == "AES":
            iterator = nextCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACMD5AuthProtocol,
                            privProtocol=usmAesCfb128Protocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )
    elif protocoloAuth == "SHA":
        if protocoloPriv == "DES":
            iterator = nextCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACSHAAuthProtocol,
                            privProtocol=usmDESPrivProtocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )
        elif protocoloPriv == "AES":
            iterator = nextCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACSHAAuthProtocol,
                            privProtocol=usmAesCfb128Protocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid))
            )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida


# //Funciones para enviar una peticion SET
# Funcion para nivel de seguridad noAuthNoPriv
def setSNMPv3noAuthNoPriv(usuario, host, oid, valor):
    global salida
    global iterator
    iterator = setCmd(
        SnmpEngine(),
        UsmUserData(usuario),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid), valor)
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida


# Funcion para nivel de seguridad noAuthNoPriv
def setSNMPv3AuthNoPriv(usuario, host, oid, protocoloAuth, llaveAuth, valor):
    global salida
    global iterator
    if protocoloAuth == "MD5":
        iterator = setCmd(
            SnmpEngine(),
            UsmUserData(usuario, llaveAuth),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid), valor)
        )
    elif protocoloAuth == "SHA":
        iterator = setCmd(
            SnmpEngine(),
            UsmUserData(usuario, llaveAuth, authProtocol=usmHMACSHAAuthProtocol),
            UdpTransportTarget((host, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid), valor)
        )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida


# Funcion para get SNMP v3 authPriv
def setSNMPv3AuthPriv(usuario, host, oid, protocoloAuth, llaveAuth, protocoloPriv, llavePriv, valor):
    global salida
    global iterator
    if protocoloAuth == "MD5":
        if protocoloPriv == "DES":
            iterator = setCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACMD5AuthProtocol,
                            privProtocol=usmDESPrivProtocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid), valor)
            )
        elif protocoloPriv == "AES":
            iterator = setCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACMD5AuthProtocol,
                            privProtocol=usmAesCfb128Protocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid), valor)
            )
    elif protocoloAuth == "SHA":
        if protocoloPriv == "DES":
            iterator = setCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACSHAAuthProtocol,
                            privProtocol=usmDESPrivProtocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid), valor)
            )
        elif protocoloPriv == "AES":
            iterator = setCmd(
                SnmpEngine(),
                UsmUserData(usuario,
                            llaveAuth,
                            llavePriv,
                            authProtocol=usmHMACSHAAuthProtocol,
                            privProtocol=usmAesCfb128Protocol),
                UdpTransportTarget((host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid), valor)
            )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        salida = errorIndication

    elif errorStatus:
        salida = ('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            salida = (' = '.join([x.prettyPrint() for x in varBind]))
    return salida
