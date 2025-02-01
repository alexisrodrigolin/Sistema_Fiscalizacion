import win32com as winc

class App():
    def __init__(self):
	    self.main("info")
    def main(self,command,event=0):
        drv = winc.Dispatch("Sam4sFiscalDriver.Sam4sFiscalDriver")

        if not drv.SerialBaudSet(self.baudrate):
            print("Error: no se pudo configurar la velocidad %s", self.baudrate)
            exit(2)

        if not drv.SerialPortOpen(self.comnum):
                print("Error: no se pudo abrir el puerto serial %d" % self.comnum)
                exit(2)
        drv.IFOpBegin("DocumentoEnCurso")
        if not drv.IFOpSend(1):
            self.cmd_error("DocumentoEnCurso",drv)
        if drv.IFOpRetIntGet("CodigoTipo"):
            drv.IFOpBegin("Cancelar")
        if not drv.IFOpSend(1):
            self.cmd_error("Cancelar",drv)
	
        if command == "info": # Información del equipo
            print("Estado")
            drv.IFOpBegin("Estado")
            if not drv.IFOpSend(1):
                self.cmd_error("Estado",drv)
            print(" FechaAperturaJornada: %s" % drv.IFOpRetGet("FechaAperturaJornada"))
            print(" HoraAperturaJornada: %s" % drv.IFOpRetGet("HoraAperturaJornada"))
            print(" NumeroUltimoZ: %d" % drv.IFOpRetIntGet("NumeroUltimoZ"))
            print(" NumeroRegistro: %s" % drv.IFOpRetGet("NumeroRegistro"))
            print(" Version: %s" % drv.IFOpRetGet("Version"))

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
                self.cmd_error("CaracteristicasEquipo",drv)
            print(" AnchoTique: %d" % drv.IFOpRetIntGet("AnchoTique"))
            print(" EmiteTiqueFiscal: %s" % ("Si" if drv.IFOpRetBoolGet("EmiteTiqueFiscal") else "No"))
            print(" EmiteTiqueFactura: %s" % ("Si" if drv.IFOpRetBoolGet("EmiteTiqueFactura") else "No"))
            print(" EmiteFactura: %s" % ("Si" if drv.IFOpRetBoolGet("EmiteFactura") else "No"))
            print(" DigitosDecimales: %d" % drv.IFOpRetIntGet("DigitosDecimales"))
            print(" ModeloVersion: %s" % drv.IFOpRetGet("ModeloVersion"))

            print("DatosContribuyente")
            drv.IFOpBegin("DatosContribuyente")
            if not drv.IFOpSend(1):
                self.cmd_error("DatosContribuyente",drv)
            print(" CUIT: %s" % drv.IFOpRetGet("CUIT"))
            print(" PV: %s" % drv.IFOpRetGet("PV"))
            print(" ResponsabilidadIVA: %s" % drv.IFOpRetGet("ResponsabilidadIVA"))
            print(" IVAEstandar: %f" % drv.IFOpRetFloatGet("IVAEstandar"))
            print(" MaximoTiqueFactura: %f" % drv.IFOpRetFloatGet("MaximoTiqueFactura"))
            print(" MaximoTique: %f" % drv.IFOpRetFloatGet("MaximoTique"))
            print(" RazonSocial: %s" % drv.IFOpRetGet("RazonSocial"))
            print(" TipoHabilitacion: %s" % drv.IFOpRetGet("TipoHabilitacion"))
            print(" IngresosBrutos: %s" % drv.IFOpRetGet("IngresosBrutos"))
            print(" InicioActividades: %s" % drv.IFOpRetGet("InicioActividades"))

            print("DocumentoEnCurso")
            drv.IFOpBegin("DocumentoEnCurso")
            if not drv.IFOpSend(1):
                self.cmd_error("DocumentoEnCurso",drv)
            print(" Tipo: %s" % drv.IFOpRetGet("Tipo"))
            print(" Letra: %s" % drv.IFOpRetGet("Letra"))
            print(" CodigoTipo: %d" % drv.IFOpRetIntGet("CodigoTipo"))
            print(" Numero: %d" % drv.IFOpRetIntGet("Numero"))

            print("FechaHora")
            drv.IFOpBegin("FechaHora")
            if not drv.IFOpSend(1):
                self.cmd_error("FechaHora",drv)
            print(" Fecha: %s" % drv.IFOpRetGet("Fecha"))
            print(" Hora: %s" % drv.IFOpRetGet("Hora"))

            print("Ethernet")
            drv.IFOpBegin("Ethernet")
            if not drv.IFOpSend(1):
                self.cmd_error("Ethernet",drv)
            print(" DireccionIP: %s" % drv.IFOpRetGet("DireccionIP"))
            print(" MascaraRed: %s" % drv.IFOpRetGet("MascaraRed"))
            print(" PuertaEnlace: %s" % drv.IFOpRetGet("PuertaEnlace"))
            print(" MAC: %s" % drv.IFOpRetGet("MAC"))

            print("ConfiguracionUSB")
            drv.IFOpBegin("ConfiguracionUSB")
            if not drv.IFOpSend(1):
                self.cmd_error("ConfiguracionUSB",drv)
            print(" Modo: %s" % drv.IFOpRetGet("Modo"))

            print("DescargasPendientes")
            drv.IFOpBegin("DescargasPendientes")
            if not drv.IFOpSend(1):
                self.cmd_error("DescargasPendientes",drv)
            print(" PrimerZPendiente: %s" % drv.IFOpRetGet("PrimerZPendiente"))
            print(" FechaPrimerZPendiente: %s" % drv.IFOpRetGet("FechaPrimerZPendiente"))
            print(" HoraPrimerZPendiente: %s" % drv.IFOpRetGet("HoraPrimerZPendiente"))
            print(" UltimoZPendiente: %s" % drv.IFOpRetGet("UltimoZPendiente"))
            print(" FechaUltimoZPendiente: %s" % drv.IFOpRetGet("FechaUltimoZPendiente"))
            print(" HoraUltimoZPendiente: %s" % drv.IFOpRetGet("HoraUltimoZPendiente"))
            print(" CantidadGeneracionesNoDescargadas: %s" % drv.IFOpRetGet("CantidadGeneracionesNoDescargadas"))
            print(" PrimerGeneracionNoDescargada: %s" % drv.IFOpRetGet("PrimerGeneracionNoDescargada"))