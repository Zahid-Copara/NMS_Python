from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.carrier.asyncore.dgram import udp
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
from pysnmp.proto.api import v2c


def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Version %s SNMP no soportada!' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message()
        )
        print('Trap proveniente de %s:%s: ' % (transportDomain, transportAddress))

        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                print('Enterprise: %s' % (pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()))
                print('Agent Address: %s' % (pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()))
                print('Generic Trap: %s' % (pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()))
                print('Specific Trap: %s' % (pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()))
                print('Uptime: %s' % (pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()))
                print('-------------------------------------------------------------------------------')
                varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
            else:
                varBinds = pMod.apiPDU.getVarBinds(reqPDU)
            print('Var-binds: ')

            for oid, val in varBinds:
                print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))
        return wholeMsg


transportDispatcher = AsyncoreDispatcher()
transportDispatcher.registerRecvCbFun(cbFun)

transportDispatcher.registerTransport(
    udp.domainName, udp.UdpSocketTransport().openServerMode(('192.168.100.7', 162))
)

transportDispatcher.jobStarted(1)

try:
    # Dispatcher will never finish as job#1 never reaches zero
    transportDispatcher.runDispatcher()

finally:
    transportDispatcher.closeDispatcher()