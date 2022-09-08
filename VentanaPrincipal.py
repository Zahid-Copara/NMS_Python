from tkinter import *
import tkinter as tk
from tkinter import ttk
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.proto.api import v2c
from SNMPv12c import *
from getSNMPv3 import *

# Creacion de la ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("PoliSNMP")
tabControl = ttk.Notebook(ventanaPrincipal)
ventanaPrincipal.geometry('675x480')
ventanaPrincipal.resizable(False, False)
ventanaPrincipal.iconbitmap('E:/Users/Zahid/PycharmProjects/NMS_Proyecto_Administracion/icono/PoliSNMP.ico')

# Variable para los radiobutton y que su valor sea unico
snmpVar = IntVar()

# Creacion de los tabs a utilizar
tabPeticion = ttk.Frame(tabControl)
tabTraps = ttk.Frame(tabControl)
tabLogs = ttk.Frame(tabControl)

tabControl.add(tabPeticion, text='Petición')
tabControl.add(tabTraps, text='Traps')
tabControl.add(tabLogs, text='Logs')
tabControl.pack(expand=1, fill="both")
resultadoMensaje = " "


# //////////////////////////////////////////////////////////////////////
# Funciones de control
# Funcion Estado Inicial de los elementos del Frame
def estadoInicial():
    cbxAuth.set(" ")
    cbxPriv.set(" ")
    cbxNivelSeguridad.set(" ")
    cbxMensajeSNMP.set(" ")
    cbxSintaxisSet.set(" ")
    lblNivelSeguridad.grid_forget()
    cbxNivelSeguridad.grid_forget()
    lblUsuario.grid_forget()
    txtUsuario.grid_forget()
    lblAuth.grid_forget()
    cbxAuth.grid_forget()
    txtAuth.grid_forget()
    lblPrivate.grid_forget()
    cbxPriv.grid_forget()
    txtPriv.grid_forget()
    lblComunidad.grid_forget()
    txtComunidad.grid_forget()
    deshabilitarMensajeSNMP()


# ////////////Funciones para los elementos de SNMPv3////////////
# Funcion para cargar todos los elementos
def cargarTodoElementoSNMPv3():
    lblNivelSeguridad.grid(row=1, column=0)
    cbxNivelSeguridad.grid(row=1, column=1)
    lblUsuario.grid(row=2, column=0)
    txtUsuario.grid(row=2, column=1, pady=10)
    lblAuth.grid(row=1, column=3)
    cbxAuth.grid(row=1, column=4, padx=5)
    txtAuth.grid(row=1, column=5)
    lblPrivate.grid(row=2, column=3)
    cbxPriv.grid(row=2, column=4, padx=5)
    txtPriv.grid(row=2, column=5)


# // Funcion para deshabilitar Mensaje SNMP
def deshabilitarMensajeSNMP():
    lblDireccionIP.config(state="disabled")
    txtDireccionIP.config(state="disabled")
    lblMsgSNMP.config(state="disabled")
    cbxMensajeSNMP.config(state="disabled")
    lblOID.config(state="disabled")
    txtOID.config(state="disabled")
    lblAyuda.config(state="disabled")
    lblSintaxis.config(state="disabled")
    cbxSintaxisSet.config(state="disabled")
    lblValor.config(state="disabled")
    txtValor.config(state="disabled")
    btnEjecutar.config(state="disabled")


# //Funcion para habilitar Mensaje SNMP
def habilitarMensajeSNMPnoSet():
    lblDireccionIP.config(state=NORMAL)
    txtDireccionIP.config(state=NORMAL)
    lblMsgSNMP.config(state=NORMAL)
    cbxMensajeSNMP.config(state="readonly")
    lblOID.config(state=NORMAL)
    txtOID.config(state=NORMAL)
    lblAyuda.config(state=NORMAL)
    btnEjecutar.config(state=NORMAL)


# //Funciones para restringir los elementos
def deshabilitarElementosSNMPv3():
    lblNivelSeguridad.config(state="disabled")
    cbxNivelSeguridad.config(state="disabled")
    lblUsuario.config(state="disabled")
    txtUsuario.config(state="disabled")
    lblAuth.config(state="disabled")
    cbxAuth.config(state="disabled")
    txtAuth.config(state="disabled")
    lblPrivate.config(state="disabled")
    cbxPriv.config(state="disabled")
    txtPriv.config(state="disabled")


# Evento al dar clic al radiobutton
def eventRadioButton():
    radSelected = snmpVar.get()
    if radSelected == 1 or radSelected == 2:
        estadoInicial()
        lblComunidad.grid(row=1, column=0, padx=20, pady=20)
        txtComunidad.grid(row=1, column=1)
        habilitarMensajeSNMPnoSet()
    elif radSelected == 3:
        estadoInicial()
        cargarTodoElementoSNMPv3()
        deshabilitarElementosSNMPv3()
        lblNivelSeguridad.config(state=NORMAL)
        cbxNivelSeguridad.config(state="readonly")
        habilitarMensajeSNMPnoSet()


# Evento al dar clic al comboBox de Nivel Seguridad
def eventCbxNivelSeguridad(event):
    nivelSeguridadSelected = cbxNivelSeguridad.get()
    if nivelSeguridadSelected == "noAuthNoPriv":
        lblUsuario.config(state=NORMAL)
        txtUsuario.config(state=NORMAL)
    elif nivelSeguridadSelected == "authNoPriv":
        lblUsuario.config(state=NORMAL)
        txtUsuario.config(state=NORMAL)
        lblAuth.config(state=NORMAL)
        cbxAuth.config(state="readonly")
        txtAuth.config(state=NORMAL)
    elif nivelSeguridadSelected == "authPriv":
        lblUsuario.config(state=NORMAL)
        txtUsuario.config(state=NORMAL)
        lblAuth.config(state=NORMAL)
        cbxAuth.config(state="readonly")
        txtAuth.config(state=NORMAL)
        lblPrivate.config(state=NORMAL)
        cbxPriv.config(state="readonly")
        txtPriv.config(state=NORMAL)


# Evento para habilitar Set SNMP
def eventCbxMensajeSNMP(event):
    mensajeSNMPSelected = cbxMensajeSNMP.get()
    if mensajeSNMPSelected == "Get":
        deshabilitarMensajeSNMP()
        habilitarMensajeSNMPnoSet()
    elif mensajeSNMPSelected == "GetNext":
        deshabilitarMensajeSNMP()
        habilitarMensajeSNMPnoSet()
    elif mensajeSNMPSelected == "Set":
        deshabilitarMensajeSNMP()
        habilitarMensajeSNMPnoSet()
        lblSintaxis.config(state=NORMAL)
        cbxSintaxisSet.config(state="readonly")
        lblValor.config(state=NORMAL)
        txtValor.config(state=NORMAL)


mensajeProveniente = " "


# Evento para el boton Ejecutar
def eventoClickEjecutar():
    global resultadoMensaje
    global mensajeProveniente
    host = txtDireccionIP.get()
    comunidad = txtComunidad.get()
    mensajeSNMP = cbxMensajeSNMP.get()
    version = snmpVar.get()
    oid = txtOID.get()
    usuario = txtUsuario.get()
    nivelSeguridad = cbxNivelSeguridad.get()
    protocoloAuth = cbxAuth.get()
    llaveAuth = txtAuth.get()
    protocoloPriv = cbxPriv.get()
    llavePriv = txtPriv.get()
    valor = txtValor.get()

    if version == 1:
        if mensajeSNMP == "Get":
            resultadoMensaje = getSNMPv1v2c(version, comunidad, host, oid)
        elif mensajeSNMP == "GetNext":
            resultadoMensaje = getNextSNMPv1v2c(version, comunidad, host, oid)
        elif mensajeSNMP == "Set":
            resultadoMensaje = setSNMPv1v2c(version, comunidad, host, oid, valor)
    elif version == 2:
        if mensajeSNMP == "Get":
            resultadoMensaje = getSNMPv1v2c(version, comunidad, host, oid)
        elif mensajeSNMP == "GetNext":
            resultadoMensaje = getNextSNMPv1v2c(version, comunidad, host, oid)
        elif mensajeSNMP == "Set":
            resultadoMensaje = setSNMPv1v2c(version, comunidad, host, oid, valor)
    elif version == 3:
        if nivelSeguridad == "noAuthNoPriv":
            if mensajeSNMP == "Get":
                resultadoMensaje = getSNMPv3noAuthNoPriv(usuario, host, oid)
            elif mensajeSNMP == "GetNext":
                resultadoMensaje = getNextSNMPv3noAuthNoPriv(usuario, host, oid)
            elif mensajeSNMP == "Set":
                resultadoMensaje = setSNMPv3noAuthNoPriv(usuario, host, oid, valor)
        elif nivelSeguridad == "authNoPriv":
            if mensajeSNMP == "Get":
                resultadoMensaje = getSNMPv3AuthNoPriv(usuario, host, oid, protocoloAuth, llaveAuth)
            elif mensajeSNMP == "GetNext":
                resultadoMensaje = getNextSNMPv3AuthNoPriv(usuario, host, oid, protocoloAuth, llaveAuth)
            elif mensajeSNMP == "Set":
                resultadoMensaje = setSNMPv3AuthNoPriv(usuario, host, oid, protocoloAuth, llaveAuth, valor)
        elif nivelSeguridad == "authPriv":
            if mensajeSNMP == "Get":
                resultadoMensaje = getSNMPv3AuthPriv(usuario, host, oid, protocoloAuth,
                                                     llaveAuth, protocoloPriv, llavePriv)
            elif mensajeSNMP == "GetNext":
                resultadoMensaje = getNextSNMPv3AuthPriv(usuario, host, oid, protocoloAuth,
                                                         llaveAuth, protocoloPriv, llavePriv)
            elif mensajeSNMP == "Set":
                resultadoMensaje = setSNMPv3AuthPriv(usuario, host, oid, protocoloAuth,
                                                     llaveAuth, protocoloPriv, llavePriv, valor)

    rtxtRecepcionSNMP.config(state=NORMAL)
    rtxtRecepcionSNMP.delete("1.0", "end")
    rtxtRecepcionSNMP.insert(1.0, "\n")
    rtxtRecepcionSNMP.insert(1.0, resultadoMensaje)
    rtxtRecepcionSNMP.config(state=DISABLED)


# //Evento clic Recibir Traps
def eventoClicRecibirTraps():
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
        print('Notificación del ContextEngineId "%s", Context Name "%s"' % (contextEngineId.prettyPrint(),
                                                                                contextName.prettyPrint()))
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
    ntfrcv.NotificationReceiver(snmpEngine, cbFun)
    snmpEngine.transportDispatcher.jobStarted(1)

    try:
        snmpEngine.transportDispatcher.runDispatcher()
    finally:
        snmpEngine.transportDispatcher.closeDispatcher()


# //////////////////////////////////////////////////////////////////////
# Creacion de frames para utilizar como panels que contienen elementos
vSNMP = LabelFrame(tabPeticion, text="Versión SNMP")
vSNMP.pack(fill='both')

msgSNMP = LabelFrame(tabPeticion, text="Mensaje SNMP")
msgSNMP.pack(fill='both')

rcpSNMP = LabelFrame(tabPeticion, text="Recepción Mensaje SNMP")
rcpSNMP.pack(expand=True, fill='both')

# Creacion y ubicacion de elementos dentro del frame vSNMP
# Creacion de los elementos para vSNMP
# //Elementos Fijos
lblVersion = Label(vSNMP, text="Versión: ", pady=10)
rbtnSNMPv1 = Radiobutton(vSNMP, text="SNMPv1", variable=snmpVar, value=1, command=eventRadioButton)
rbtnSNMPv2c = Radiobutton(vSNMP, text="SNMPv2c", variable=snmpVar, value=2, command=eventRadioButton)
rbtnSNMPv3 = Radiobutton(vSNMP, text="SNMPv3", variable=snmpVar, value=3, command=eventRadioButton)
# //Elementos Variables
lblNivelSeguridad = Label(vSNMP, text="Nivel de Seguridad: ", padx=20)
lblComunidad = Label(vSNMP, text="Comunidad: ")
lblUsuario = Label(vSNMP, text="Usuario: ")
lblAuth = Label(vSNMP, text="Authentication: ")
lblPrivate = Label(vSNMP, text="Private: ")
txtComunidad = Entry(vSNMP)
txtUsuario = Entry(vSNMP, width=18)
txtAuth = Entry(vSNMP)
txtPriv = Entry(vSNMP)
cbxNivelSeguridad = ttk.Combobox(vSNMP,
                                 state="readonly",
                                 values=["noAuthNoPriv", "authNoPriv", "authPriv"], width=15)
cbxAuth = ttk.Combobox(vSNMP,
                       state="readonly",
                       values=["MD5", "SHA"], width=4)
cbxPriv = ttk.Combobox(vSNMP,
                       state="readonly",
                       values=["DES", "AES"], width=4)

# // Creacion de elementos para Mensaje SNMP
lblDireccionIP = Label(msgSNMP, text="Dirección IP: ")
lblMsgSNMP = Label(msgSNMP, text="Mensaje SNMP: ")
lblOID = Label(msgSNMP, text="OID: ")
lblSintaxis = Label(msgSNMP, text="Sintaxis: ")
lblValor = Label(msgSNMP, text="Valor: ")
btnEjecutar = Button(msgSNMP, text="Ejecutar", command=lambda: eventoClickEjecutar())
txtDireccionIP = Entry(msgSNMP, width=18)
cbxMensajeSNMP = ttk.Combobox(msgSNMP,
                              state="readonly",
                              values=["Get", "GetNext", "Set"], width=15)
txtOID = Entry(msgSNMP, width=18)
cbxSintaxisSet = ttk.Combobox(msgSNMP,
                              state="readonly",
                              values=["Octet String"], width=15)
txtValor = Entry(msgSNMP, width=18)
lblAyuda = Label(msgSNMP, text=" ")
# Ubicacion de los elementos dentro del frame
# //Elementos Fijos
# Version SNMP
lblVersion.grid(row=0, column=0)
rbtnSNMPv1.grid(row=0, column=1)
rbtnSNMPv2c.grid(row=0, column=2)
rbtnSNMPv3.grid(row=0, column=3, padx=20)
# Mensaje SNMP
lblDireccionIP.grid(row=0, column=0, pady=10, padx=30)
txtDireccionIP.grid(row=0, column=1)
lblMsgSNMP.grid(row=1, column=0)
cbxMensajeSNMP.grid(row=1, column=1)
lblOID.grid(row=2, column=0, pady=10)
txtOID.grid(row=2, column=1)
lblAyuda.grid(row=1, column=3, padx=40)
lblSintaxis.grid(row=1, column=4)
cbxSintaxisSet.grid(row=1, column=5)
lblValor.grid(row=2, column=4)
txtValor.grid(row=2, column=5)
btnEjecutar.grid(row=3, column=3, pady=20, padx=10)
# Texto para recibir las peticiones
rtxtRecepcionSNMP = Text(rcpSNMP)
rtxtRecepcionSNMP.pack(expand=True, fill="both")

# //Llamada a la funcion Estado Inicial para ocultar los botones al inicio
estadoInicial()
# //Llamada al evento de combobox selected Nivel Seguridad
cbxNivelSeguridad.bind("<<ComboboxSelected>>", eventCbxNivelSeguridad)
# //Llamada al evento de combobox selected Tipo de Mensaje
cbxMensajeSNMP.bind("<<ComboboxSelected>>", eventCbxMensajeSNMP)

# Elementos del las Traps
recTrapsSNMP = LabelFrame(tabTraps, text="Recepción Traps")
recTrapsSNMP.pack(expand=True, fill="both")

ctrlTrapsSNMP = LabelFrame(tabTraps)
ctrlTrapsSNMP.pack(expand=True, fill="both")

# //Agregar Elementos
# Elemento de rtxt para la recepcion de traps
rtxtRecepcionTrapsSNMP = Text(recTrapsSNMP)
rtxtRecepcionTrapsSNMP.pack(expand=True, fill="both")
# Elemento botones de control
btnEmpezarRecepcionTraps = Button(ctrlTrapsSNMP, text="Recibir", command=lambda: eventoClicRecibirTraps())
btnDetenerRecepcionTraps = Button(ctrlTrapsSNMP, text="Detener")

btnEmpezarRecepcionTraps.grid(row=3, column=3, padx=180)
btnDetenerRecepcionTraps.grid(row=3, column=4, padx=20)

ventanaPrincipal.mainloop()
