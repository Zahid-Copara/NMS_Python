from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.proto.api import v2c

snmpEngine = engine.SnmpEngine()
parte2 = " "

config.addTransport(
    snmpEngine,
    udp.domainName,
    udp.UdpTransport().openServerMode(('192.168.100.7', 162))
)

# Configuracion del usuario SNMPv3
config.addV3User(
    snmpEngine, 'grupo1u1',
    config.usmHMACMD5AuthProtocol, 'redes2022',
    securityEngineId=v2c.OctetString(hexValue='80001f888078930a5bb6f6d26200000000')
)

config.addV3User(
    snmpEngine, 'grupo1u2',
    config.usmHMACSHAAuthProtocol, 'redes2022',
    config.usmDESPrivProtocol, 'redes2022',
    securityEngineId=v2c.OctetString(hexValue='80001f888078930a5bb6f6d26200000000')
)


def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    global parte2
    parte1 = ('Notificación del ContextEngineId "%s", Context Name "%s"' % (contextEngineId.prettyPrint(),
                                                                            contextName.prettyPrint()))
    for name, val in varBinds:
        parte2 = ('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
    mensajeTotal = parte1 + parte2
    return mensajeTotal


ntfrcv.NotificationReceiver(snmpEngine, cbFun)
snmpEngine.transportDispatcher.jobStarted(1)

try:
    snmpEngine.transportDispatcher.runDispatcher()
finally:
    snmpEngine.transportDispatcher.closeDispatcher()
