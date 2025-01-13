# -*	- coding: utf-8 -*-
"""
	Ejemplo de uso de Sam4sFiscalDriver.dll
	Para Windows
	2019-04-03
"""

import argparse
from ctypes import windll, c_int, c_double, c_char_p

def driver_load ():
	"Carga la DLL en forma dinámica"
	dll = windll.LoadLibrary("Sam4sFiscalDriver.dll")

	dll.SerialPortOpen.restype = c_int
	dll.SerialPortOpen.argtypes = (c_int,)
	dll.SerialBaudSet.restype = c_int
	dll.SerialBaudSet.argtypes = (c_int,)
	dll.SerialPortClose.restype = c_int
	dll.SerialPortClose.argtypes = ()
	dll.IFOpBegin.restype = c_int
	dll.IFOpBegin.argtypes = (c_char_p,)
	dll.IFOpSend.restype = c_int
	dll.IFOpSend.argtypes = (c_int,)
	dll.IFOpWaitingIs.restype = c_int
	dll.IFOpWaitingIs.argtypes = ()
	dll.IFOpAbort.restype = c_int
	dll.IFOpAbort.argtypes = ()
	dll.IFOpParamSet.restype = c_int
	dll.IFOpParamSet.argtypes = (c_char_p, c_char_p,)
	dll.IFOpParamGet.restype = c_char_p
	dll.IFOpParamGet.argtypes = (c_char_p,)
	dll.IFOpParamIntSet.restype = c_int
	dll.IFOpParamIntSet.argtypes = (c_char_p, c_int,)
	dll.IFOpParamIntGet.restype = c_int
	dll.IFOpParamIntGet.argtypes = (c_char_p,)
	dll.IFOpParamFloatSet.restype = c_int
	dll.IFOpParamFloatSet.argtypes = (c_char_p, c_double,)
	dll.IFOpParamFloatGet.restype = c_double
	dll.IFOpParamFloatGet.argtypes = (c_char_p,)
	dll.IFOpParamBoolSet.restype = c_int
	dll.IFOpParamBoolSet.argtypes = (c_char_p, c_int,)
	dll.IFOpParamBoolGet.restype = c_int
	dll.IFOpParamBoolGet.argtypes = (c_char_p,)
	dll.IFOpCmdOkIs.restype = c_int
	dll.IFOpCmdOkIs.argtypes = ()
	dll.IFOpErrorGet.restype = c_int
	dll.IFOpErrorGet.argtypes = ()
	dll.IFOpErrorDescGet.restype = c_char_p
	dll.IFOpErrorDescGet.argtypes = ()
	dll.IFOpStateGet.restype = c_int
	dll.IFOpStateGet.argtypes = (c_char_p,)
	dll.IFOpRetGet.restype = c_char_p
	dll.IFOpRetGet.argtypes = (c_char_p,)
	dll.IFOpRetIntGet.restype = c_int
	dll.IFOpRetIntGet.argtypes = (c_char_p,)
	dll.IFOpRetFloatGet.restype = c_double
	dll.IFOpRetFloatGet.argtypes = (c_char_p,)
	dll.IFOpRetBoolGet.restype = c_int
	dll.IFOpRetBoolGet.argtypes = (c_char_p,)
	dll.IFOpListGet.restype = c_char_p
	dll.IFOpListGet.argtypes = (c_int,)
	dll.IFOpParamListGet.restype = c_char_p
	dll.IFOpParamListGet.argtypes = (c_int,)
	dll.IFOpRetListGet.restype = c_char_p
	dll.IFOpRetListGet.argtypes = (c_int,)
	dll.IFOpStateListGet.restype = c_char_p
	dll.IFOpStateListGet.argtypes = (c_int,)

	return dll

def cmd_error (cmdname,drv):
	"Manejo error en comando"
	err = drv.IFOpErrorGet()
	errdesc = drv.IFOpErrorDescGet()
	print("Error %d en comando %s: %s" % (err, cmdname, errdesc))
	exit(1)

def main ():
	"Programa de prueba"
	parser = argparse.ArgumentParser(description='Sam4sFiscalDriver Test')
	parser.add_argument('comnum', type=int, help=u"Número de puerto serial")
	parser.add_argument('baudrate', type=int, help=u"Velocidad puerto serial (ej.: 9600, 115200)")
	parser.add_argument('testname', type=str, help=u"Prueba a realizar: info tique tnc factura credito debito recibo generico interno voucher remitor remitox recibox presupuesto donacion tiqueinfo printertest reimprimir cancel totalestique config x z auditoria misc eventlog rptpend rptzdown")
	parser.add_argument('extra1', type=str, nargs='?', default="")
	parser.add_argument('extra2', type=str, nargs='?', default="")
	args = parser.parse_args()

	drv = driver_load()

	if not drv.SerialBaudSet(args.baudrate):
		print("Error: no se pudo configurar la velocidad %s", args.baudrate)
		exit(2)

	if not drv.SerialPortOpen(args.comnum):
		print("Error: no se pudo abrir el puerto serial %s" % args.comnum)
		exit(2)

	drv.IFOpBegin("DocumentoEnCurso")
	if not drv.IFOpSend(1):
		cmd_error("DocumentoEnCurso",drv)
	if drv.IFOpRetIntGet("CodigoTipo"):
		drv.IFOpBegin("Cancelar")
		if not drv.IFOpSend(1):
			cmd_error("Cancelar",drv)

	if args.testname == "info": # Información del equipo
		print("Estado")
		drv.IFOpBegin("Estado")
		if not drv.IFOpSend(1):
			cmd_error("Estado",drv)
		print(" FechaAperturaJornada: %s" % drv.IFOpRetGet("FechaAperturaJornada").decode('latin1'))
		print(" HoraAperturaJornada: %s" % drv.IFOpRetGet("HoraAperturaJornada").decode('latin1'))
		print(" NumeroUltimoZ: %d" % drv.IFOpRetIntGet("NumeroUltimoZ"))
		print(" NumeroRegistro: %s" % drv.IFOpRetGet("NumeroRegistro").decode('latin1'))
		print(" Version: %s" % drv.IFOpRetGet("Version").decode('latin1'))

		print("*Estado Impresora*")
		print(" FallaImpresora: %s" % ("Si" if drv.IFOpStateGet("FallaImpresora") else "No"))
		print(" OffLine: %s" % ("Si" if drv.IFOpStateGet("OffLine") else "No"))
		print(" PocoPapel: %s" % ("Si" if drv.IFOpStateGet("PocoPapel") else "No"))
		print(" GavetaAbierta: %s" % ("Si" if drv.IFOpStateGet("GavetaAbierta") else "No"))
		print(" SinPapel: %s" % ("Si" if drv.IFOpStateGet("SinPapel") else "No"))
		print(" ErrorImpresora: %s" % ("Si" if drv.IFOpStateGet("ErrorImpresora") else "No"))

		print("*Estado Fiscal*")
		print(" MemoriaFiscalLlena: %s" % ("Si" if drv.IFOpStateGet("MemoriaFiscalLlena") else "No"))
		print(" MemoriaFiscalCasiLlena: %s" % ("Si" if drv.IFOpStateGet("MemoriaFiscalCasiLlena") else "No"))
		print(" Certificada: %s" % ("Si" if drv.IFOpStateGet("Certificada") else "No"))
		print(" Fiscalizada: %s" % ("Si" if drv.IFOpStateGet("Fiscalizada") else "No"))
		print(" DocumentoAbierto: %s" % ("Si" if drv.IFOpStateGet("DocumentoAbierto") else "No"))
		print(" DocumentoNoFiscalAbierto: %s" % ("Si" if drv.IFOpStateGet("DocumentoNoFiscalAbierto") else "No"))
		print(" FacturaAbierta: %s" % ("Si" if drv.IFOpStateGet("FacturaAbierta") else "No"))
		print(" ErrorFiscal: %s" % ("Si" if drv.IFOpStateGet("ErrorFiscal") else "No"))

		print("CaracteristicasEquipo")
		drv.IFOpBegin("CaracteristicasEquipo")
		if not drv.IFOpSend(1):
			cmd_error("CaracteristicasEquipo",drv)
		print(" AnchoTique: %d" % drv.IFOpRetIntGet("AnchoTique"))
		print(" EmiteTiqueFiscal: %s" % ("Si" if drv.IFOpRetBoolGet("EmiteTiqueFiscal") else "No"))
		print(" EmiteTiqueFactura: %s" % ("Si" if drv.IFOpRetBoolGet("EmiteTiqueFactura") else "No"))
		print(" EmiteFactura: %s" % ("Si" if drv.IFOpRetBoolGet("EmiteFactura") else "No"))
		print(" DigitosDecimales: %d" % drv.IFOpRetIntGet("DigitosDecimales"))
		print(" ModeloVersion: %s" % drv.IFOpRetGet("ModeloVersion").decode('latin1'))

		print("DatosContribuyente")
		drv.IFOpBegin("DatosContribuyente")
		if not drv.IFOpSend(1):
			cmd_error("DatosContribuyente",drv)
		print(" CUIT: %s" % drv.IFOpRetGet("CUIT").decode('latin1'))
		print(" PV: %s" % drv.IFOpRetGet("PV").decode('latin1'))
		print(" ResponsabilidadIVA: %s" % drv.IFOpRetGet("ResponsabilidadIVA").decode('latin1'))
		print(" IVAEstandar: %f" % drv.IFOpRetFloatGet("IVAEstandar"))
		print(" MaximoTiqueFactura: %f" % drv.IFOpRetFloatGet("MaximoTiqueFactura"))
		print(" MaximoTique: %f" % drv.IFOpRetFloatGet("MaximoTique"))
		print(" RazonSocial: %s" % drv.IFOpRetGet("RazonSocial").decode('latin1'))
		print(" TipoHabilitacion: %s" % drv.IFOpRetGet("TipoHabilitacion").decode('latin1'))
		print(" IngresosBrutos: %s" % drv.IFOpRetGet("IngresosBrutos").decode('latin1'))
		print(" InicioActividades: %s" % drv.IFOpRetGet("InicioActividades").decode('latin1'))

		print("DocumentoEnCurso")
		drv.IFOpBegin("DocumentoEnCurso")
		if not drv.IFOpSend(1):
			cmd_error("DocumentoEnCurso",drv)
		print(" Tipo: %s" % drv.IFOpRetGet("Tipo").decode('latin1'))
		print(" Letra: %s" % drv.IFOpRetGet("Letra").decode('latin1'))
		print(" CodigoTipo: %d" % drv.IFOpRetIntGet("CodigoTipo"))
		print(" Numero: %d" % drv.IFOpRetIntGet("Numero"))

		print("FechaHora")
		drv.IFOpBegin("FechaHora")
		if not drv.IFOpSend(1):
			cmd_error("FechaHora",drv)
		print(" Fecha: %s" % drv.IFOpRetGet("Fecha").decode('latin1'))
		print(" Hora: %s" % drv.IFOpRetGet("Hora").decode('latin1'))

		print("Ethernet")
		drv.IFOpBegin("Ethernet")
		if not drv.IFOpSend(1):
			cmd_error("Ethernet",drv)
		print(" DireccionIP: %s" % drv.IFOpRetGet("DireccionIP").decode('latin1'))
		print(" MascaraRed: %s" % drv.IFOpRetGet("MascaraRed").decode('latin1'))
		print(" PuertaEnlace: %s" % drv.IFOpRetGet("PuertaEnlace").decode('latin1'))
		print(" MAC: %s" % drv.IFOpRetGet("MAC").decode('latin1'))

		print("ConfiguracionUSB")
		drv.IFOpBegin("ConfiguracionUSB")
		if not drv.IFOpSend(1):
			cmd_error("ConfiguracionUSB",drv)
		print(" Modo: %s" % drv.IFOpRetGet("Modo").decode('latin1'))

		print("DescargasPendientes")
		drv.IFOpBegin("DescargasPendientes")
		if not drv.IFOpSend(1):
			cmd_error("DescargasPendientes",drv)
		print(" PrimerZPendiente: %s" % drv.IFOpRetGet("PrimerZPendiente").decode('latin1'))
		print(" FechaPrimerZPendiente: %s" % drv.IFOpRetGet("FechaPrimerZPendiente").decode('latin1'))
		print(" HoraPrimerZPendiente: %s" % drv.IFOpRetGet("HoraPrimerZPendiente").decode('latin1'))
		print(" UltimoZPendiente: %s" % drv.IFOpRetGet("UltimoZPendiente").decode('latin1'))
		print(" FechaUltimoZPendiente: %s" % drv.IFOpRetGet("FechaUltimoZPendiente").decode('latin1'))
		print(" HoraUltimoZPendiente: %s" % drv.IFOpRetGet("HoraUltimoZPendiente").decode('latin1'))
		print(" CantidadGeneracionesNoDescargadas: %s" % drv.IFOpRetGet("CantidadGeneracionesNoDescargadas").decode('latin1'))
		print(" PrimerGeneracionNoDescargada: %s" % drv.IFOpRetGet("PrimerGeneracionNoDescargada").decode('latin1'))

	elif args.testname == "tique": # Tique
		print("AbrirTique")
		drv.IFOpBegin("AbrirTique")
		if not drv.IFOpSend(1):
			cmd_error("AbrirTique",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 1.2345)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoProducto", "7791234567898")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

		print("AbrirCajon")
		drv.IFOpBegin("AbrirCajon")
		if not drv.IFOpSend(1):
			cmd_error("AbrirCajon",drv)

	elif args.testname == "tnc": # Tique Nota de Credito
		print("ComprobanteAsociado")
		drv.IFOpBegin("ComprobanteAsociado")
		drv.IFOpParamIntSet("CodigoTipo", 83)
		drv.IFOpParamIntSet("PV", 12345)
		drv.IFOpParamIntSet("Numero", 12345678)
		if not drv.IFOpSend(1):
			cmd_error("ComprobanteAsociado",drv)

		print("AbrirTiqueNotaCredito")
		drv.IFOpBegin("AbrirTiqueNotaCredito")
		if not drv.IFOpSend(1):
			cmd_error("AbrirTiqueNotaCredito",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n extra del \xedtem'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 3.0)
		drv.IFOpParamFloatSet("Precio", 1.2345)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoProducto", "6935750533048")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n extra del \xedtem'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("ItemRetorno")
		drv.IFOpBegin("ItemRetorno")
		drv.IFOpParamSet("Descripcion", u'Item de prueba'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 2.0)
		drv.IFOpParamFloatSet("Precio", 1.2345)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoProducto", "6935750533048")
		if not drv.IFOpSend(1):
			cmd_error("ItemRetorno",drv)

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "factura": # Factura
		print("AbrirFactura")
		drv.IFOpBegin("AbrirFactura")
		drv.IFOpParamSet("ClienteResponsabilidad", "I")
		drv.IFOpParamSet("ClienteRazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("ClienteTipoDocumento", "CUIT")
		drv.IFOpParamSet("ClienteNumeroDocumento", "11111111113")
		drv.IFOpParamSet("ClienteDomicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("AbrirFactura",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 1'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 3.0)
		drv.IFOpParamFloatSet("Precio", 1.2345)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 2'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 1.0)
		drv.IFOpParamFloatSet("Precio", 1.2)
		drv.IFOpParamFloatSet("IVA", 10.5)
		drv.IFOpParamSet("CodigoInterno", "1002")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 3'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 1.3)
		drv.IFOpParamFloatSet("IVA", 0.0)
		drv.IFOpParamSet("CodigoInterno", "1003")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 4'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 1.4)
		drv.IFOpParamSet("IVA", "E")
		drv.IFOpParamSet("CodigoInterno", "1004")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 5'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 1.5)
		drv.IFOpParamSet("IVA", "N")
		drv.IFOpParamSet("CodigoInterno", "1005")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 6'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 1.6)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamFloatSet("MontoImpIntFijo", 0.6)
		drv.IFOpParamSet("CodigoInterno", "1006")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 7'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 1.7)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamFloatSet("TasaAjuste", 0.14893617)
		drv.IFOpParamSet("CodigoInterno", "1007")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("SubtotalImpreso")
		drv.IFOpBegin("SubtotalImpreso")
		if not drv.IFOpSend(1):
			cmd_error("SubtotalImpreso",drv)
		print(" CantidadItems: %s" % drv.IFOpRetGet("CantidadItems").decode('latin1'))
		print(" Total: %f" % drv.IFOpRetFloatGet("Total"))
		print(" IVA: %f" % drv.IFOpRetFloatGet("IVA"))
		print(" Pagado: %f" % drv.IFOpRetFloatGet("Pagado"))
		print(" ImpIntPorc: %f" % drv.IFOpRetFloatGet("ImpIntPorc"))
		print(" ImpIntFijo: %f" % drv.IFOpRetFloatGet("ImpIntFijo"))
		print(" Neto: %f" % drv.IFOpRetFloatGet("Neto"))

		print("ItemBonificacion")
		drv.IFOpBegin("ItemBonificacion")
		drv.IFOpParamSet("Descripcion", u'Decuento articulo'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 3.0)
		drv.IFOpParamFloatSet("Precio", 0.12345)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoInterno", "1001b")
		if not drv.IFOpSend(1):
			cmd_error("ItemBonificacion",drv)

		print("ItemRetornoBonificacion")
		drv.IFOpBegin("ItemRetornoBonificacion")
		drv.IFOpParamSet("Descripcion", u'Decuento articulo'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 1.0)
		drv.IFOpParamFloatSet("Precio", 0.12345)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoInterno", "1001b")
		if not drv.IFOpSend(1):
			cmd_error("ItemRetornoBonificacion",drv)

		print("OtroTributo")
		drv.IFOpBegin("OtroTributo")
		drv.IFOpParamIntSet("CodigoTipo", 7)
		drv.IFOpParamFloatSet("Monto", 5.0)
		if not drv.IFOpSend(1):
			cmd_error("OtroTributo",drv)

		print("Pago")
		drv.IFOpBegin("Pago")
		drv.IFOpParamFloatSet("Monto", 50.0)
		drv.IFOpParamIntSet("CodigoTipo", 8)
		if not drv.IFOpSend(1):
			cmd_error("Pago",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

		print("SubtotalInfo")
		drv.IFOpBegin("SubtotalInfo")
		if not drv.IFOpSend(1):
			cmd_error("SubtotalInfo",drv)
		print(" CantidadItems: %s" % drv.IFOpRetGet("CantidadItems").decode('latin1'))
		print(" Total: %f" % drv.IFOpRetFloatGet("Total"))
		print(" IVA: %f" % drv.IFOpRetFloatGet("IVA"))
		print(" Pagado: %f" % drv.IFOpRetFloatGet("Pagado"))
		print(" ImpIntPorc: %f" % drv.IFOpRetFloatGet("ImpIntPorc"))
		print(" ImpIntFijo: %f" % drv.IFOpRetFloatGet("ImpIntFijo"))
		print(" Neto: %f" % drv.IFOpRetFloatGet("Neto"))

	elif args.testname == "credito": # Nota de Crédito
		print("AbrirNotaCredito")
		drv.IFOpBegin("AbrirNotaCredito")
		drv.IFOpParamSet("ClienteResponsabilidad", "M")
		drv.IFOpParamSet("ClienteRazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("ClienteTipoDocumento", "CUIT")
		drv.IFOpParamSet("ClienteNumeroDocumento", "11111111113")
		drv.IFOpParamSet("ClienteDomicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("AbrirNotaCredito",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 3.0)
		drv.IFOpParamFloatSet("Precio", 1.5)
		drv.IFOpParamFloatSet("IVA", 10.5)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemSena")
		drv.IFOpBegin("ItemSena")
		drv.IFOpParamSet("Descripcion", u'Item de se\xf1a'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 3.0)
		drv.IFOpParamFloatSet("Precio", 3.2)
		drv.IFOpParamFloatSet("IVA", 0.0)
		drv.IFOpParamSet("CodigoInterno", "2001")
		if not drv.IFOpSend(1):
			cmd_error("ItemSena",drv)

		print("ItemRetornoSena")
		drv.IFOpBegin("ItemRetornoSena")
		drv.IFOpParamSet("Descripcion", u'Item de se\xf1a'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", -2.0)
		drv.IFOpParamFloatSet("Precio", -3.2)
		drv.IFOpParamFloatSet("IVA", 0.0)
		drv.IFOpParamSet("CodigoInterno", "2001")
		if not drv.IFOpSend(1):
			cmd_error("ItemRetornoSena",drv)

		print("DescuentoGeneral")
		drv.IFOpBegin("DescuentoGeneral")
		drv.IFOpParamSet("Descripcion", u'Oferta del d\xeda'.encode('latin1'))
		drv.IFOpParamFloatSet("Monto", 2.4)
		if not drv.IFOpSend(1):
			cmd_error("DescuentoGeneral",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Pago")
		drv.IFOpBegin("Pago")
		drv.IFOpParamFloatSet("Monto", 20.0)
		if not drv.IFOpSend(1):
			cmd_error("Pago",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "debito": # Nota de Débito
		print("AbrirNotaDebito")
		drv.IFOpBegin("AbrirNotaDebito")
		drv.IFOpParamSet("ClienteResponsabilidad", "F")
		drv.IFOpParamSet("ClienteRazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("ClienteTipoDocumento", "DNI")
		drv.IFOpParamSet("ClienteNumeroDocumento", "11222333")
		drv.IFOpParamSet("ClienteDomicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("AbrirNotaDebito",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 1'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 1.5)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 2'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 0.5)
		drv.IFOpParamFloatSet("IVA", 10.5)
		drv.IFOpParamSet("CodigoInterno", "1002")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("RecargoGeneral")
		drv.IFOpBegin("RecargoGeneral")
		drv.IFOpParamSet("Descripcion", u'Recargo administrativo'.encode('latin1'))
		drv.IFOpParamFloatSet("Monto", 2.0)
		if not drv.IFOpSend(1):
			cmd_error("RecargoGeneral",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Pago")
		drv.IFOpBegin("Pago")
		drv.IFOpParamSet("Descripcion", u'CTA 123458'.encode('latin1'))
		drv.IFOpParamFloatSet("Monto", 20.0)
		drv.IFOpParamIntSet("CodigoTipo", 6)
		drv.IFOpParamSet("TextoLibre", u'Vencimiento XX/XX/XXXX'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("Pago",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "recibo": # Recibo
		print("AbrirRecibo")
		drv.IFOpBegin("AbrirRecibo")
		drv.IFOpParamSet("ClienteResponsabilidad", "I")
		drv.IFOpParamSet("ClienteRazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("ClienteTipoDocumento", "CUIT")
		drv.IFOpParamSet("ClienteNumeroDocumento", "11111111113")
		drv.IFOpParamSet("ClienteDomicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("AbrirRecibo",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 2.5)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("Pago")
		drv.IFOpBegin("Pago")
		drv.IFOpParamSet("Descripcion", u'Tarjeta XXXX'.encode('latin1'))
		drv.IFOpParamFloatSet("Monto", 5.0)
		drv.IFOpParamIntSet("CodigoTipo", 20)
		drv.IFOpParamSet("Cuotas", u'12'.encode('latin1'))
		drv.IFOpParamSet("Cupones", u'XXX-XX-XXXX'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("Pago",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "generico": # Documento Generico
		print("AbrirDocGenerico")
		drv.IFOpBegin("AbrirDocGenerico")
		if not drv.IFOpSend(1):
			cmd_error("AbrirDocGenerico",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'L\xednea de texto no fiscal'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "abc \\R\\Resaltado\\f\\ def")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "abc \\A\\Doble alto\\f\\ def")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "abc \\N\\Doble ancho\\f\\ def")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "abc \\S\\Subrayado\\f\\ def")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "abc \\AN\\Doble A&A\\f\\ def")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "CODE 39 \\xE1\\A1+-.$/%\\xE0\\")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "Interleaved \\xE3\\1122334455\\xE0\\")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "UPC A \\xE5\\123456789012\\xE0\\")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "EAN 13 \\xE7\\123456789012\\xE0\\")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "EAN 8 \\xEA\\12345678\\xE0\\")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", "CODABAR \\xEC\\D164-$:/.+B-\\xE0\\")
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "interno": # Documento de Uso Interno
		print("AbrirDocInterno")
		drv.IFOpBegin("AbrirDocInterno")
		if not drv.IFOpSend(1):
			cmd_error("AbrirDocInterno",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'L\xednea de texto no fiscal'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "voucher": # Voucher de Tarjeta de Crédito
		print("AbrirDNFH")
		drv.IFOpBegin("AbrirDNFH")
		drv.IFOpParamIntSet("CodigoTipo", 922)
		drv.IFOpParamSet("Atributos", "difat")
		if not drv.IFOpSend(1):
			cmd_error("AbrirDNFH",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 1)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 2)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 3)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'09/14'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 4)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 5)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'L\xednea libre 1 (opcional)'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 19)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'L\xednea libre 2 (opcional)'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 20)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'L\xednea libre 3 (opcional)'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 21)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 6)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 7)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 8)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 9)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 10)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 11)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 12)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'L\xednea libre 4 (opcional)'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 22)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'L\xednea libre 5 (opcional)'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 23)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'L\xednea libre 6 (opcional)'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 24)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 13)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 14)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 15)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 16)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 17)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("TextoNoFiscal")
		drv.IFOpBegin("TextoNoFiscal")
		drv.IFOpParamSet("Texto", u'Dato libre'.encode('latin1'))
		drv.IFOpParamIntSet("Tipo", 18)
		if not drv.IFOpSend(1):
			cmd_error("TextoNoFiscal",drv)

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "remitor": # Remito R
		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "0")
		drv.IFOpParamSet("Responsabilidad", "I")
		drv.IFOpParamSet("RazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("TipoDocumento", "CUIT")
		drv.IFOpParamSet("NumeroDocumento", "11111111113")
		drv.IFOpParamSet("Domicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "2")
		drv.IFOpParamSet("Responsabilidad", "I")
		drv.IFOpParamSet("RazonSocial1", "Razon social transportista")
		drv.IFOpParamSet("TipoDocumento", "CUIT")
		drv.IFOpParamSet("NumeroDocumento", "99999999995")
		drv.IFOpParamSet("Domicilio1", "Domicilio transportista")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "3")
		drv.IFOpParamSet("Responsabilidad", "F")
		drv.IFOpParamSet("RazonSocial1", "Nombre Chofer")
		drv.IFOpParamSet("TipoDocumento", "DNI")
		drv.IFOpParamSet("NumeroDocumento", "11222333")
		drv.IFOpParamSet("Domicilio1", "Patente 1")
		drv.IFOpParamSet("Domicilio2", "Patente 2")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("AbrirRemitoR")
		drv.IFOpBegin("AbrirRemitoR")
		if not drv.IFOpSend(1):
			cmd_error("AbrirRemitoR",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 1'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 2.0)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 2'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 3.0)
		drv.IFOpParamSet("CodigoInterno", "1002")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "remitox": # Remito X
		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "0")
		drv.IFOpParamSet("Responsabilidad", "I")
		drv.IFOpParamSet("RazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("TipoDocumento", "CUIT")
		drv.IFOpParamSet("NumeroDocumento", "11111111113")
		drv.IFOpParamSet("Domicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "2")
		drv.IFOpParamSet("Responsabilidad", "I")
		drv.IFOpParamSet("RazonSocial1", "Razon social transportista")
		drv.IFOpParamSet("TipoDocumento", "CUIT")
		drv.IFOpParamSet("NumeroDocumento", "99999999995")
		drv.IFOpParamSet("Domicilio1", "Domicilio transportista")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "3")
		drv.IFOpParamSet("Responsabilidad", "F")
		drv.IFOpParamSet("RazonSocial1", "Nombre Chofer")
		drv.IFOpParamSet("TipoDocumento", "DNI")
		drv.IFOpParamSet("NumeroDocumento", "11222333")
		drv.IFOpParamSet("Domicilio1", "Patente 1")
		drv.IFOpParamSet("Domicilio2", "Patente 2")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("AbrirRemitoX")
		drv.IFOpBegin("AbrirRemitoX")
		if not drv.IFOpSend(1):
			cmd_error("AbrirRemitoX",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 1'.encode('latin1'))
		drv.IFOpParamFloatSet("Cantidad", 12.345678)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 2'.encode('latin1'))
		drv.IFOpParamSet("CodigoInterno", "1002")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "recibox": # Recibo X
		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "0")
		drv.IFOpParamSet("Responsabilidad", "I")
		drv.IFOpParamSet("RazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("TipoDocumento", "CUIT")
		drv.IFOpParamSet("NumeroDocumento", "11111111113")
		drv.IFOpParamSet("Domicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("AbrirReciboX")
		drv.IFOpBegin("AbrirReciboX")
		if not drv.IFOpSend(1):
			cmd_error("AbrirReciboX",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n l\xednea 1'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n l\xednea 2'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n l\xednea 3'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n l\xednea 4'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Descripci\xf3n l\xednea 5'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 12.34)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("Pago")
		drv.IFOpBegin("Pago")
		drv.IFOpParamFloatSet("Monto", 50.0)
		drv.IFOpParamIntSet("CodigoTipo", 8)
		if not drv.IFOpSend(1):
			cmd_error("Pago",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "presupuesto": # Presupuesto
		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "0")
		drv.IFOpParamSet("Responsabilidad", "I")
		drv.IFOpParamSet("RazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("TipoDocumento", "CUIT")
		drv.IFOpParamSet("NumeroDocumento", "11111111113")
		drv.IFOpParamSet("Domicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("AbrirPresupuesto")
		drv.IFOpBegin("AbrirPresupuesto")
		if not drv.IFOpSend(1):
			cmd_error("AbrirPresupuesto",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 1'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 12.34)
		drv.IFOpParamFloatSet("IVA", 21.0)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Item de prueba 2'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 5.0)
		drv.IFOpParamFloatSet("IVA", 10.5)
		drv.IFOpParamSet("CodigoInterno", "1002")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("DescuentoGeneral")
		drv.IFOpBegin("DescuentoGeneral")
		drv.IFOpParamSet("Descripcion", u'Oferta del d\xeda'.encode('latin1'))
		drv.IFOpParamFloatSet("Monto", 2.34)
		if not drv.IFOpSend(1):
			cmd_error("DescuentoGeneral",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "donacion": # Documento Donación
		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "0")
		drv.IFOpParamSet("Responsabilidad", "I")
		drv.IFOpParamSet("RazonSocial1", "Razon social cliente")
		drv.IFOpParamSet("TipoDocumento", "CUIT")
		drv.IFOpParamSet("NumeroDocumento", "11111111113")
		drv.IFOpParamSet("Domicilio1", "Domicilio cliente")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("DatosTercero")
		drv.IFOpBegin("DatosTercero")
		drv.IFOpParamSet("Tipo", "1")
		drv.IFOpParamSet("Responsabilidad", "I")
		drv.IFOpParamSet("RazonSocial1", "Razon social beneficiario")
		drv.IFOpParamSet("TipoDocumento", "CUIT")
		drv.IFOpParamSet("NumeroDocumento", "99999999995")
		drv.IFOpParamSet("Domicilio1", "Domicilio beneficiario")
		if not drv.IFOpSend(1):
			cmd_error("DatosTercero",drv)

		print("AbrirDonacion")
		drv.IFOpBegin("AbrirDonacion")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n l\xednea 1'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("AbrirDonacion",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n l\xednea 2'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n l\xednea 3'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("TextoFiscal")
		drv.IFOpBegin("TextoFiscal")
		drv.IFOpParamSet("Texto", u'Descripci\xf3n l\xednea 4'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("TextoFiscal",drv)

		print("ItemVenta")
		drv.IFOpBegin("ItemVenta")
		drv.IFOpParamSet("Descripcion", u'Descripci\xf3n l\xednea 5'.encode('latin1'))
		drv.IFOpParamFloatSet("Precio", 12.34)
		drv.IFOpParamSet("CodigoInterno", "1001")
		if not drv.IFOpSend(1):
			cmd_error("ItemVenta",drv)

		print("Pago")
		drv.IFOpBegin("Pago")
		drv.IFOpParamFloatSet("Monto", 50.0)
		drv.IFOpParamIntSet("CodigoTipo", 8)
		if not drv.IFOpSend(1):
			cmd_error("Pago",drv)
		print(" MontoFaltaPagar: %f" % drv.IFOpRetFloatGet("MontoFaltaPagar"))

		print("Cerrar")
		drv.IFOpBegin("Cerrar")
		if not drv.IFOpSend(1):
			cmd_error("Cerrar",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo").decode('latin1'))

	elif args.testname == "tiqueinfo": # Tique de Información del Equipo
		print("ImprimirInformacion")
		drv.IFOpBegin("ImprimirInformacion")
		if not drv.IFOpSend(1):
			cmd_error("ImprimirInformacion",drv)

	elif args.testname == "printertest": # Prueba Mecanismo Impresor
		print("ImprimirPruebaImpresora")
		drv.IFOpBegin("ImprimirPruebaImpresora")
		if not drv.IFOpSend(1):
			cmd_error("ImprimirPruebaImpresora",drv)

	elif args.testname == "reimprimir": # Reimpresión Tique 1
		print("Reimprimir")
		drv.IFOpBegin("Reimprimir")
		drv.IFOpParamIntSet("CodigoTipo", 83)
		drv.IFOpParamIntSet("Numero", 1)
		if not drv.IFOpSend(1):
			cmd_error("Reimprimir",drv)

	elif args.testname == "cancel": # Cancelación
		print("AbrirTique")
		drv.IFOpBegin("AbrirTique")
		if not drv.IFOpSend(1):
			cmd_error("AbrirTique",drv)

		print("Cancelar")
		drv.IFOpBegin("Cancelar")
		if not drv.IFOpSend(1):
			cmd_error("Cancelar",drv)

	elif args.testname == "totalestique": # Obtiene totales de jornada para Tique
		print("Contadores")
		drv.IFOpBegin("Contadores")
		drv.IFOpParamIntSet("CodigoTipo", 83)
		if not drv.IFOpSend(1):
			cmd_error("Contadores",drv)
		print(" NumeroUltimoZ: %d" % drv.IFOpRetIntGet("NumeroUltimoZ"))
		print(" NumeroUltimoCambioFechaHora: %d" % drv.IFOpRetIntGet("NumeroUltimoCambioFechaHora"))
		print(" NumeroUltimoInformeAuditoria: %d" % drv.IFOpRetIntGet("NumeroUltimoInformeAuditoria"))
		print(" NumeroUltimoDocumento: %d" % drv.IFOpRetIntGet("NumeroUltimoDocumento"))

		print("TotalesJornada")
		drv.IFOpBegin("TotalesJornada")
		drv.IFOpParamIntSet("CodigoTipo", 83)
		if not drv.IFOpSend(1):
			cmd_error("TotalesJornada",drv)
		print(" FechaAperturaJornada: %s" % drv.IFOpRetGet("FechaAperturaJornada").decode('latin1'))
		print(" HoraAperturaJornada: %s" % drv.IFOpRetGet("HoraAperturaJornada").decode('latin1'))
		print(" NumeroUltimoZ: %d" % drv.IFOpRetIntGet("NumeroUltimoZ"))
		print(" NecesitaZ: %s" % ("Si" if drv.IFOpRetBoolGet("NecesitaZ") else "No"))
		print(" CantidadEmitidos: %d" % drv.IFOpRetIntGet("CantidadEmitidos"))
		print(" CantidadCancelados: %d" % drv.IFOpRetIntGet("CantidadCancelados"))
		print(" Total: %f" % drv.IFOpRetFloatGet("Total"))
		print(" TotalIva: %f" % drv.IFOpRetFloatGet("TotalIva"))
		print(" TotalImpIntFijo: %f" % drv.IFOpRetFloatGet("TotalImpIntFijo"))
		print(" TotalImpIntPorc: %f" % drv.IFOpRetFloatGet("TotalImpIntPorc"))
		print(" TotalOtroTributo: %f" % drv.IFOpRetFloatGet("TotalOtroTributo"))

		print("TotalesJornadaIva")
		drv.IFOpBegin("TotalesJornadaIva")
		drv.IFOpParamIntSet("CodigoTipo", 83)
		if not drv.IFOpSend(1):
			cmd_error("TotalesJornadaIva",drv)
		print(" TotalIva: %f" % drv.IFOpRetFloatGet("TotalIva"))
		print(" TasaIva1: %f" % drv.IFOpRetFloatGet("TasaIva1"))
		print(" TotalIva1: %f" % drv.IFOpRetFloatGet("TotalIva1"))
		print(" TotalVentaIva1: %f" % drv.IFOpRetFloatGet("TotalVentaIva1"))
		print(" TotalImpIntFijoIva1: %f" % drv.IFOpRetFloatGet("TotalImpIntFijoIva1"))
		print(" TotalImpIntPorcIva1: %f" % drv.IFOpRetFloatGet("TotalImpIntPorcIva1"))
		print(" TasaIva2: %f" % drv.IFOpRetFloatGet("TasaIva2"))
		print(" TotalIva2: %f" % drv.IFOpRetFloatGet("TotalIva2"))
		print(" TotalVentaIva2: %f" % drv.IFOpRetFloatGet("TotalVentaIva2"))
		print(" TotalImpIntFijoIva2: %f" % drv.IFOpRetFloatGet("TotalImpIntFijoIva2"))
		print(" TotalImpIntPorcIva2: %f" % drv.IFOpRetFloatGet("TotalImpIntPorcIva2"))
		print(" TasaIva3: %f" % drv.IFOpRetFloatGet("TasaIva3"))
		print(" TotalIva3: %f" % drv.IFOpRetFloatGet("TotalIva3"))
		print(" TotalVentaIva3: %f" % drv.IFOpRetFloatGet("TotalVentaIva3"))
		print(" TotalImpIntFijoIva3: %f" % drv.IFOpRetFloatGet("TotalImpIntFijoIva3"))
		print(" TotalImpIntPorcIva3: %f" % drv.IFOpRetFloatGet("TotalImpIntPorcIva3"))
		print(" TasaIva4: %f" % drv.IFOpRetFloatGet("TasaIva4"))
		print(" TotalIva4: %f" % drv.IFOpRetFloatGet("TotalIva4"))
		print(" TotalVentaIva4: %f" % drv.IFOpRetFloatGet("TotalVentaIva4"))
		print(" TotalImpIntFijoIva4: %f" % drv.IFOpRetFloatGet("TotalImpIntFijoIva4"))
		print(" TotalImpIntPorcIva4: %f" % drv.IFOpRetFloatGet("TotalImpIntPorcIva4"))
		print(" TasaIva5: %f" % drv.IFOpRetFloatGet("TasaIva5"))
		print(" TotalIva5: %f" % drv.IFOpRetFloatGet("TotalIva5"))
		print(" TotalVentaIva5: %f" % drv.IFOpRetFloatGet("TotalVentaIva5"))
		print(" TotalImpIntFijoIva5: %f" % drv.IFOpRetFloatGet("TotalImpIntFijoIva5"))
		print(" TotalImpIntPorcIva5: %f" % drv.IFOpRetFloatGet("TotalImpIntPorcIva5"))
		print(" TasaIva6: %f" % drv.IFOpRetFloatGet("TasaIva6"))
		print(" TotalIva6: %f" % drv.IFOpRetFloatGet("TotalIva6"))
		print(" TotalVentaIva6: %f" % drv.IFOpRetFloatGet("TotalVentaIva6"))
		print(" TotalImpIntFijoIva6: %f" % drv.IFOpRetFloatGet("TotalImpIntFijoIva6"))
		print(" TotalImpIntPorcIva6: %f" % drv.IFOpRetFloatGet("TotalImpIntPorcIva6"))

		print("TotalesJornadaOtroTributo")
		drv.IFOpBegin("TotalesJornadaOtroTributo")
		drv.IFOpParamIntSet("CodigoTipo", 83)
		drv.IFOpParamIntSet("IndiceOtroTributo", 1)
		if not drv.IFOpSend(1):
			cmd_error("TotalesJornadaOtroTributo",drv)
		print(" TotalOtroTributoGeneral: %f" % drv.IFOpRetFloatGet("TotalOtroTributoGeneral"))
		print(" TotalOtroTributo07: %f" % drv.IFOpRetFloatGet("TotalOtroTributo07"))
		print(" TotalOtroTributo06: %f" % drv.IFOpRetFloatGet("TotalOtroTributo06"))
		print(" TotalOtroTributo09: %f" % drv.IFOpRetFloatGet("TotalOtroTributo09"))
		print(" CantidadEnJornada: %d" % drv.IFOpRetIntGet("CantidadEnJornada"))
		print(" TotalOtroTributo: %f" % drv.IFOpRetFloatGet("TotalOtroTributo"))
		print(" CodigoOtroTributo: %d" % drv.IFOpRetIntGet("CodigoOtroTributo"))

	elif args.testname == "config": # Configuración
		print("EstablecerOpcion")
		drv.IFOpBegin("EstablecerOpcion")
		drv.IFOpParamIntSet("Numero", 242)
		drv.IFOpParamIntSet("Valor", 1)
		if not drv.IFOpSend(1):
			cmd_error("EstablecerOpcion",drv)

		print("Opcion")
		drv.IFOpBegin("Opcion")
		drv.IFOpParamIntSet("Numero", 242)
		if not drv.IFOpSend(1):
			cmd_error("Opcion",drv)
		print(" Valor: %s" % drv.IFOpRetGet("Valor").decode('latin1'))

		print("EstablecerEncabezadoCola")
		drv.IFOpBegin("EstablecerEncabezadoCola")
		drv.IFOpParamIntSet("Numero", 79)
		drv.IFOpParamSet("Texto", u'Encabezado libre 9'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("EstablecerEncabezadoCola",drv)

		print("EncabezadoCola")
		drv.IFOpBegin("EncabezadoCola")
		drv.IFOpParamIntSet("Numero", 79)
		if not drv.IFOpSend(1):
			cmd_error("EncabezadoCola",drv)
		print(" Numero: %d" % drv.IFOpRetIntGet("Numero"))
		print(" Texto: %s" % drv.IFOpRetGet("Texto").decode('latin1'))

		print("EstablecerEncabezadoCola")
		drv.IFOpBegin("EstablecerEncabezadoCola")
		drv.IFOpParamIntSet("Numero", 19)
		drv.IFOpParamSet("Texto", u'Cola libre 9'.encode('latin1'))
		if not drv.IFOpSend(1):
			cmd_error("EstablecerEncabezadoCola",drv)

		print("EncabezadoCola")
		drv.IFOpBegin("EncabezadoCola")
		drv.IFOpParamIntSet("Numero", 19)
		if not drv.IFOpSend(1):
			cmd_error("EncabezadoCola",drv)
		print(" Numero: %d" % drv.IFOpRetIntGet("Numero"))
		print(" Texto: %s" % drv.IFOpRetGet("Texto").decode('latin1'))

	elif args.testname == "x": # Informe X
		print("InformeXNoImpreso")
		drv.IFOpBegin("InformeXNoImpreso")
		if not drv.IFOpSend(1):
			cmd_error("InformeXNoImpreso",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CantidadDocFiscalCancel: %s" % drv.IFOpRetGet("CantidadDocFiscalCancel").decode('latin1'))
		print(" CantidadDocNoFiscal: %s" % drv.IFOpRetGet("CantidadDocNoFiscal").decode('latin1'))
		print(" CantidadDocGenerico: %s" % drv.IFOpRetGet("CantidadDocGenerico").decode('latin1'))
		print(" CantidadTique: %s" % drv.IFOpRetGet("CantidadTique").decode('latin1'))
		print(" CantidadFacturaA: %s" % drv.IFOpRetGet("CantidadFacturaA").decode('latin1'))
		print(" NumeroUltimoTique: %s" % drv.IFOpRetGet("NumeroUltimoTique").decode('latin1'))
		print(" MontoVenta: %f" % drv.IFOpRetFloatGet("MontoVenta"))
		print(" MontoIVAVenta: %f" % drv.IFOpRetFloatGet("MontoIVAVenta"))
		print(" MontoOtrosTributosVenta: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosVenta"))
		print(" NumeroFacturaA: %s" % drv.IFOpRetGet("NumeroFacturaA").decode('latin1'))
		print(" NumeroCreditoA: %s" % drv.IFOpRetGet("NumeroCreditoA").decode('latin1'))
		print(" NumeroCreditoB: %s" % drv.IFOpRetGet("NumeroCreditoB").decode('latin1'))
		print(" MontoCredito: %f" % drv.IFOpRetFloatGet("MontoCredito"))
		print(" MontoIVACredito: %f" % drv.IFOpRetFloatGet("MontoIVACredito"))
		print(" MontoOtrosTributosCredito: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosCredito"))

		print("InformeXResumido")
		drv.IFOpBegin("InformeXResumido")
		if not drv.IFOpSend(1):
			cmd_error("InformeXResumido",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CantidadDocFiscalCancel: %s" % drv.IFOpRetGet("CantidadDocFiscalCancel").decode('latin1'))
		print(" CantidadDocNoFiscal: %s" % drv.IFOpRetGet("CantidadDocNoFiscal").decode('latin1'))
		print(" CantidadDocGenerico: %s" % drv.IFOpRetGet("CantidadDocGenerico").decode('latin1'))
		print(" CantidadTique: %s" % drv.IFOpRetGet("CantidadTique").decode('latin1'))
		print(" CantidadFacturaA: %s" % drv.IFOpRetGet("CantidadFacturaA").decode('latin1'))
		print(" NumeroUltimoTique: %s" % drv.IFOpRetGet("NumeroUltimoTique").decode('latin1'))
		print(" MontoVenta: %f" % drv.IFOpRetFloatGet("MontoVenta"))
		print(" MontoIVAVenta: %f" % drv.IFOpRetFloatGet("MontoIVAVenta"))
		print(" MontoOtrosTributosVenta: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosVenta"))
		print(" NumeroFacturaA: %s" % drv.IFOpRetGet("NumeroFacturaA").decode('latin1'))
		print(" NumeroCreditoA: %s" % drv.IFOpRetGet("NumeroCreditoA").decode('latin1'))
		print(" NumeroCreditoB: %s" % drv.IFOpRetGet("NumeroCreditoB").decode('latin1'))
		print(" MontoCredito: %f" % drv.IFOpRetFloatGet("MontoCredito"))
		print(" MontoIVACredito: %f" % drv.IFOpRetFloatGet("MontoIVACredito"))
		print(" MontoOtrosTributosCredito: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosCredito"))

		print("InformeXDetallado")
		drv.IFOpBegin("InformeXDetallado")
		if not drv.IFOpSend(1):
			cmd_error("InformeXDetallado",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CantidadDocFiscalCancel: %s" % drv.IFOpRetGet("CantidadDocFiscalCancel").decode('latin1'))
		print(" CantidadDocNoFiscal: %s" % drv.IFOpRetGet("CantidadDocNoFiscal").decode('latin1'))
		print(" CantidadDocGenerico: %s" % drv.IFOpRetGet("CantidadDocGenerico").decode('latin1'))
		print(" CantidadTique: %s" % drv.IFOpRetGet("CantidadTique").decode('latin1'))
		print(" CantidadFacturaA: %s" % drv.IFOpRetGet("CantidadFacturaA").decode('latin1'))
		print(" NumeroUltimoTique: %s" % drv.IFOpRetGet("NumeroUltimoTique").decode('latin1'))
		print(" MontoVenta: %f" % drv.IFOpRetFloatGet("MontoVenta"))
		print(" MontoIVAVenta: %f" % drv.IFOpRetFloatGet("MontoIVAVenta"))
		print(" MontoOtrosTributosVenta: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosVenta"))
		print(" NumeroFacturaA: %s" % drv.IFOpRetGet("NumeroFacturaA").decode('latin1'))
		print(" NumeroCreditoA: %s" % drv.IFOpRetGet("NumeroCreditoA").decode('latin1'))
		print(" NumeroCreditoB: %s" % drv.IFOpRetGet("NumeroCreditoB").decode('latin1'))
		print(" MontoCredito: %f" % drv.IFOpRetFloatGet("MontoCredito"))
		print(" MontoIVACredito: %f" % drv.IFOpRetFloatGet("MontoIVACredito"))
		print(" MontoOtrosTributosCredito: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosCredito"))

	elif args.testname == "z": # Cierre Z
		print("CierreZ")
		drv.IFOpBegin("CierreZ")
		if not drv.IFOpSend(1):
			cmd_error("CierreZ",drv)
		print(" Numero: %s" % drv.IFOpRetGet("Numero").decode('latin1'))
		print(" CantidadDocFiscalCancel: %s" % drv.IFOpRetGet("CantidadDocFiscalCancel").decode('latin1'))
		print(" CantidadDocNoFiscal: %s" % drv.IFOpRetGet("CantidadDocNoFiscal").decode('latin1'))
		print(" CantidadDocGenerico: %s" % drv.IFOpRetGet("CantidadDocGenerico").decode('latin1'))
		print(" CantidadTique: %s" % drv.IFOpRetGet("CantidadTique").decode('latin1'))
		print(" CantidadFacturaA: %s" % drv.IFOpRetGet("CantidadFacturaA").decode('latin1'))
		print(" NumeroUltimoTique: %s" % drv.IFOpRetGet("NumeroUltimoTique").decode('latin1'))
		print(" MontoVenta: %f" % drv.IFOpRetFloatGet("MontoVenta"))
		print(" MontoIVAVenta: %f" % drv.IFOpRetFloatGet("MontoIVAVenta"))
		print(" MontoOtrosTributosVenta: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosVenta"))
		print(" NumeroFacturaA: %s" % drv.IFOpRetGet("NumeroFacturaA").decode('latin1'))
		print(" NumeroCreditoA: %s" % drv.IFOpRetGet("NumeroCreditoA").decode('latin1'))
		print(" NumeroCreditoB: %s" % drv.IFOpRetGet("NumeroCreditoB").decode('latin1'))
		print(" MontoCredito: %f" % drv.IFOpRetFloatGet("MontoCredito"))
		print(" MontoIVACredito: %f" % drv.IFOpRetFloatGet("MontoIVACredito"))
		print(" MontoOtrosTributosCredito: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosCredito"))

	elif args.testname == "auditoria": # Informe de Auditoría resumido
		print("ImprimirAuditoriaResumidaPorZ")
		drv.IFOpBegin("ImprimirAuditoriaResumidaPorZ")
		drv.IFOpParamSet("ZInicial", "1")
		drv.IFOpParamSet("ZFinal", "9999")
		if not drv.IFOpSend(1):
			cmd_error("ImprimirAuditoriaResumidaPorZ",drv)

	elif args.testname == "misc": # Miscelaneos
		print("AbrirCajon")
		drv.IFOpBegin("AbrirCajon")
		if not drv.IFOpSend(1):
			cmd_error("AbrirCajon",drv)

		print("AvanzarPapel")
		drv.IFOpBegin("AvanzarPapel")
		drv.IFOpParamSet("Lineas", "5")
		if not drv.IFOpSend(1):
			cmd_error("AvanzarPapel",drv)

		print("CortarPapel")
		drv.IFOpBegin("CortarPapel")
		if not drv.IFOpSend(1):
			cmd_error("CortarPapel",drv)

		print("AbrirCajon2")
		drv.IFOpBegin("AbrirCajon2")
		if not drv.IFOpSend(1):
			cmd_error("AbrirCajon2",drv)

	elif args.testname == "eventlog": # Descarga log de eventos
		print("ComenzarDescargaEventLog")
		drv.IFOpBegin("ComenzarDescargaEventLog")
		if not drv.IFOpSend(1):
			cmd_error("ComenzarDescargaEventLog",drv)

		fout = open("eventlog.txt", "wb")
		bloop = True
		while bloop:
			print("DescargarBloque")
			drv.IFOpBegin("DescargarBloque")
			if not drv.IFOpSend(1):
				cmd_error("DescargarBloque",drv)
			data = drv.IFOpRetGet("Datos")
			fout.write(data)
#			print(" Datos: %s" % data.decode('latin1'))
			bloop = drv.IFOpRetBoolGet("Continuar")
#			print(" Continuar: %s" % ("Si" if bloop else "No"))
		fout.close()

	elif args.testname == "rptpend": # Descarga reportes ya generados y no descargados
		while True:
			print("DescargasPendientes")
			drv.IFOpBegin("DescargasPendientes")
			if not drv.IFOpSend(1):
				cmd_error("DescargasPendientes",drv)
			npend = drv.IFOpRetIntGet("CantidadGeneracionesNoDescargadas")
			print(" CantidadGeneracionesNoDescargadas: %s" % npend)
			ipend = drv.IFOpRetIntGet("PrimerGeneracionNoDescargada")
			print(" PrimerGeneracionNoDescargada: %s" % ipend)

			if not ipend:
				break

			for rpttype in (1, 2, 3):
				print("ComenzarDescargaReporte")
				drv.IFOpBegin("ComenzarDescargaReporte")
				drv.IFOpParamIntSet("TipoReporte", rpttype)
				drv.IFOpParamIntSet("NumeroGeneracion", ipend)
				if not drv.IFOpSend(1):
					cmd_error("ComenzarDescargaReporte",drv)
				filename = drv.IFOpRetGet("NombreArchivo").decode('latin1')
				print(" NombreArchivo: %s" % filename)

				fout = open(filename, "wb")
				bloop = True
				while bloop:
					print("DescargarBloque")
					drv.IFOpBegin("DescargarBloque")
					if not drv.IFOpSend(1):
						cmd_error("DescargarBloque",drv)
					data = drv.IFOpRetGet("Datos")
					fout.write(data)
#					print(" Datos: %s" % data.decode('latin1'))
					bloop = drv.IFOpRetBoolGet("Continuar")
#					print(" Continuar: %s" % ("Si" if bloop else "No"))
				fout.close()

	elif args.testname == "rptzdown": # Genera y descarga reportes por rango de Z
		print("GenerarReportesPorZ desde %s hasta %s" % (args.extra1, args.extra2))
		drv.IFOpBegin("GenerarReportesPorZ")
		drv.IFOpParamSet("ZInicial", args.extra1)
		drv.IFOpParamSet("ZFinal", args.extra2)
		if not drv.IFOpSend(1):
			cmd_error("GenerarReportesPorZ",drv)
		print(" NumeroGeneracion: %s" % drv.IFOpRetIntGet("NumeroGeneracion"))

		for rpttype in (1, 2, 3):
			print("ComenzarDescargaReporte")
			drv.IFOpBegin("ComenzarDescargaReporte")
			drv.IFOpParamIntSet("TipoReporte", rpttype)
			if not drv.IFOpSend(1):
				cmd_error("ComenzarDescargaReporte",drv)
			filename = drv.IFOpRetGet("NombreArchivo").decode('latin1')
			print(" NombreArchivo: %s" % filename)

			fout = open(filename, "wb")
			bloop = True
			while bloop:
				print("DescargarBloque")
				drv.IFOpBegin("DescargarBloque")
				if not drv.IFOpSend(1):
					cmd_error("DescargarBloque",drv)
				data = drv.IFOpRetGet("Datos")
				fout.write(data)
#				print(" Datos: %s" % data.decode('latin1'))
				bloop = drv.IFOpRetBoolGet("Continuar")
#				print(" Continuar: %s" % ("Si" if bloop else "No"))
			fout.close()

	elif args.testname == "docdown": # Descarga xml de un documento emitido
		print("ComenzarDescargaDocumento %s %s" % (args.extra1, args.extra2))
		drv.IFOpBegin("ComenzarDescargaDocumento")
		drv.IFOpParamSet("CodigoTipo", args.extra1)
		drv.IFOpParamSet("Numero", args.extra2)
		if not drv.IFOpSend(1):
			cmd_error("ComenzarDescargaDocumento",drv)

		fout = open("doc.xml", "wb")
		bloop = True
		while bloop:
			print("DescargarBloque")
			drv.IFOpBegin("DescargarBloque")
			if not drv.IFOpSend(1):
				cmd_error("DescargarBloque",drv)
			data = drv.IFOpRetGet("Datos")
			fout.write(data)
#			print(" Datos: %s" % data.decode('latin1'))
			bloop = drv.IFOpRetBoolGet("Continuar")
#			print(" Continuar: %s" % ("Si" if bloop else "No"))
		fout.close()

	else:
		print("Error: prueba desconocida: %s" % args.testname)
		exit(3)

if __name__ == "__main__":
	main()
