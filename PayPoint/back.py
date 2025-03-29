
import mysql.connector as sql
# import win32com.client as winc
import json
class Logic:
    def __init__(self):
        with open("Configuration.json", "r") as archivo:
            self.datos = json.load(archivo)
        self.font= float(self.datos['Font'])

    def writeCfg(self):
        with open("Configuration.json","w") as archivo:
            json.dump(self.datos,archivo, indent=4)
    def Conection(self):

        self.mydb = sql.connect( 
        host=f"{self.datos['Db']}",
        user=f"{self.datos['User']}",
        password=f"{self.datos['Password']}",
        database= "TEST",
        autocommit=True,
         
        )

        if not self.mydb.is_connected(): exit()
        self.cursor= self.mydb.cursor()   
        self.subtotal= 0.00
        self.cant=0
        self.tique=[]
        self.internal=[]
        self.comnum= int(self.datos["Com"])
        self.baudrate= int(self.datos["Baudrate"])
        self.valid_users = {
            "Tec":"2505",
            "admin": '888888',
            "1": "1",  
        }
        self.nitem=0
        
        
    def suma(self,Descripcion='',Plu='',Precio= 0,Cantidad=0 , cantOF=1, refresh= 0):
        
        if refresh ==1:
            self.subtotal=0.00
            self.cant=0
            self.nitem=0
            self.tique.clear()
            self.internal.clear()
        else:
            self.subtotal+= Precio*Cantidad
            self.cant+= Cantidad
            self.nitem+=1 
            item=(Descripcion,Precio,Plu,Cantidad)
            inter=(Descripcion,Precio,Plu,Cantidad, cantOF,self.nitem)
            if Cantidad>0: self.internal.append(inter)
            self.tique.append(item)
            print(self.internal)
            


    def validate_user(self, username, password):
        return self.valid_users.get(username) == password
        
    def item(self,PLU):
        instruction= f'SELECT SQL_NO_CACHE Marca, Descripcion, Tipo_Sabor, Cantidad, Unidad, Precio, Cant1, Precio1, Cant2, Precio2, Cant3, Precio3 FROM Art WHERE PLU= {PLU}'
        instruction2= f'SELECT SQL_NO_CACHE Marca, Descripcion, Tipo_Sabor, Cantidad, Unidad, Precio, Cant1, Precio1, Cant2, Precio2, Cant3, Precio3 FROM Art WHERE PLU2= {PLU}'
        self.cursor.execute(instruction)
        result= self.cursor.fetchone()
        self.cursor.execute(instruction2)
        result2=self.cursor.fetchone()
        if result:
          
            return result
            
        elif result2:
            return result2
        else:
            return 0
    def table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        """ + ", ".join([f"item_{i} VARCHAR(40)" for i in range(1, 101)]) + """)""")
        self.mydb.commit()
    def cmd_error (self,cmdname,drv):
        "Manejo error en comando"
        err = drv.IFOpErrorGet()
        errdesc = drv.IFOpErrorDescGet()
        print("Error %d en comando %s: %s" % (err, cmdname, errdesc))
        exit()
    def main(self,command,status=0, extra=0, extra1=0, event=0):

        drv = winc.Dispatch("Sam4sFiscalDriver.Sam4sFiscalDriver")
        try:
            if not drv.SerialBaudSet(self.baudrate):
                print("Error: no se pudo configurar la velocidad %s", self.baudrate)
                exit()

            if not drv.SerialPortOpen(self.comnum):
                    print("Error: no se pudo abrir el puerto serial %d" % self.comnum)
                    exit()
        except:
            return "Error de Comunicación"
        try:
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

            elif command == "tiqueinfo": # Tique de Información del Equipo 
                print("ImprimirInformacion")
                drv.IFOpBegin("ImprimirInformacion")
                if not drv.IFOpSend(1):
                    self.cmd_error("ImprimirInformacion",drv)
            elif command == "z": # Cierre Z
                print("CierreZ")
                drv.IFOpBegin("CierreZ")
                if not drv.IFOpSend(1):
                    self.cmd_error("CierreZ",drv)
                print(" Numero: %s" % drv.IFOpRetGet("Numero"))
                print(" CantidadDocFiscalCancel: %s" % drv.IFOpRetGet("CantidadDocFiscalCancel"))
                print(" CantidadDocNoFiscal: %s" % drv.IFOpRetGet("CantidadDocNoFiscal"))
                print(" CantidadDocGenerico: %s" % drv.IFOpRetGet("CantidadDocGenerico"))
                print(" CantidadTique: %s" % drv.IFOpRetGet("CantidadTique"))
                print(" CantidadFacturaA: %s" % drv.IFOpRetGet("CantidadFacturaA"))
                print(" NumeroUltimoTique: %s" % drv.IFOpRetGet("NumeroUltimoTique"))
                print(" MontoVenta: %f" % drv.IFOpRetFloatGet("MontoVenta"))
                print(" MontoIVAVenta: %f" % drv.IFOpRetFloatGet("MontoIVAVenta"))
                print(" MontoOtrosTributosVenta: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosVenta"))
                print(" NumeroFacturaA: %s" % drv.IFOpRetGet("NumeroFacturaA"))
                print(" NumeroCreditoA: %s" % drv.IFOpRetGet("NumeroCreditoA"))
                print(" NumeroCreditoB: %s" % drv.IFOpRetGet("NumeroCreditoB"))
                print(" MontoCredito: %f" % drv.IFOpRetFloatGet("MontoCredito"))
                print(" MontoIVACredito: %f" % drv.IFOpRetFloatGet("MontoIVACredito"))
                print(" MontoOtrosTributosCredito: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosCredito"))
            elif command == "x": 
                drv.IFOpBegin("InformeXDetallado")
                if not drv.IFOpSend(1):
                    self.cmd_error("InformeXDetallado",drv)
                print(" Numero: %s" % drv.IFOpRetGet("Numero"))
                print(" CantidadDocFiscalCancel: %s" % drv.IFOpRetGet("CantidadDocFiscalCancel"))
                print(" CantidadDocNoFiscal: %s" % drv.IFOpRetGet("CantidadDocNoFiscal"))
                print(" CantidadDocGenerico: %s" % drv.IFOpRetGet("CantidadDocGenerico"))
                print(" CantidadTique: %s" % drv.IFOpRetGet("CantidadTique"))
                print(" CantidadFacturaA: %s" % drv.IFOpRetGet("CantidadFacturaA"))
                print(" NumeroUltimoTique: %s" % drv.IFOpRetGet("NumeroUltimoTique"))
                print(" MontoVenta: %f" % drv.IFOpRetFloatGet("MontoVenta"))
                print(" MontoIVAVenta: %f" % drv.IFOpRetFloatGet("MontoIVAVenta"))
                print(" MontoOtrosTributosVenta: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosVenta"))
                print(" NumeroFacturaA: %s" % drv.IFOpRetGet("NumeroFacturaA"))
                print(" NumeroCreditoA: %s" % drv.IFOpRetGet("NumeroCreditoA"))
                print(" NumeroCreditoB: %s" % drv.IFOpRetGet("NumeroCreditoB"))
                print(" MontoCredito: %f" % drv.IFOpRetFloatGet("MontoCredito"))
                print(" MontoIVACredito: %f" % drv.IFOpRetFloatGet("MontoIVACredito"))
                print(" MontoOtrosTributosCredito: %f" % drv.IFOpRetFloatGet("MontoOtrosTributosCredito"))
            elif command == "tique": 
                
                print("AbrirTique")
                drv.IFOpBegin("AbrirTique")
                if not drv.IFOpSend(1):
                    self.cmd_error("AbrirTique",drv)
                    exit()
                for x in self.tique:
                    if x[3]<0:
                        drv.IFOpBegin("ItemRetorno")
                        drv.IFOpParamSet("Descripcion", f'{x[0]}')
                        drv.IFOpParamFloatSet("Precio", abs(x[1]))
                        drv.IFOpParamFloatSet("IVA", 21.0)
                        drv.IFOpParamSet("CodigoProducto", f"{x[2]}")
                        drv.IFOpParamFloatSet("Cantidad", abs(x[3]))
                        if not drv.IFOpSend(1):
                            self.cmd_error("ItemRetorno",drv)
                            exit()
                    else:
                        drv.IFOpBegin("ItemVenta")
                        drv.IFOpParamSet("Descripcion", f'{x[0]}')
                        drv.IFOpParamFloatSet("Precio", x[1])
                        drv.IFOpParamFloatSet("IVA", 21.0)
                        drv.IFOpParamSet("CodigoProducto", f"{x[2]}")
                        drv.IFOpParamFloatSet("Cantidad", x[3])
                        if not drv.IFOpSend(1):
                            self.cmd_error("ItemVenta",drv)
                            exit()
                if extra:
                    drv.IFOpBegin("DescuentoGeneral")
                    drv.IFOpParamSet("Descripcion", "Bonificación:")
                    drv.IFOpParamFloatSet("Monto", extra)  
                    if not drv.IFOpSend(1):
                        self.cmd_error("DescuentoGeneral",drv)
                        exit()           
                if extra1:
                    drv.IFOpBegin("RecargoGeneral")
                    drv.IFOpParamSet("Descripcion", "Recargo:")
                    drv.IFOpParamFloatSet("Monto", extra1)  
                    if not drv.IFOpSend(1):
                        self.cmd_error("RecargoGeneral",drv)
                        exit()             
                print("Cerrar")
                drv.IFOpBegin("Cerrar")
                if not drv.IFOpSend(1):
                    self.cmd_error("Cerrar",drv)
                    exit()
                print(" Numero: %s" % drv.IFOpRetGet("Numero"))
                print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo"))
                print("AbrirCajon")
                drv.IFOpBegin("AbrirCajon")
                if not drv.IFOpSend(1):
                    self.cmd_error("AbrirCajon",drv)
                

            elif command == "tnc": # Tique Nota de Credito

                print("ComprobanteAsociado")
                drv.IFOpBegin("ComprobanteAsociado")
                drv.IFOpParamIntSet("CodigoTipo", 83)
                drv.IFOpParamIntSet("PV", 12345)
                drv.IFOpParamIntSet("Numero", 12345678)
                if not drv.IFOpSend(1):
                    self.cmd_error("ComprobanteAsociado",drv)

                print("AbrirTiqueNotaCredito")
                drv.IFOpBegin("AbrirTiqueNotaCredito")
                if not drv.IFOpSend(1):
                    self.cmd_error("AbrirTiqueNotaCredito",drv)

                print("TextoFiscal")
                drv.IFOpBegin("TextoFiscal")
                drv.IFOpParamSet("Texto", u'Descripci\xf3n extra del \xedtem')
                if not drv.IFOpSend(1):
                    self.cmd_error("TextoFiscal",drv)

                print("ItemVenta")
                drv.IFOpBegin("ItemVenta")
                drv.IFOpParamSet("Descripcion", u'Item de prueba')
                drv.IFOpParamFloatSet("Cantidad", 3.0)
                drv.IFOpParamFloatSet("Precio", 1.2345)
                drv.IFOpParamFloatSet("IVA", 21.0)
                drv.IFOpParamSet("CodigoProducto", "6935750533048")
                if not drv.IFOpSend(1):
                    self.cmd_error("ItemVenta",drv)

                print("TextoFiscal")
                drv.IFOpBegin("TextoFiscal")
                drv.IFOpParamSet("Texto", u'Descripci\xf3n extra del \xedtem')
                if not drv.IFOpSend(1):
                    self.cmd_error("TextoFiscal",drv)

                print("ItemRetorno")
                drv.IFOpBegin("ItemRetorno")
                drv.IFOpParamSet("Descripcion", u'Item de prueba')
                drv.IFOpParamFloatSet("Cantidad", 2.0)
                drv.IFOpParamFloatSet("Precio", 1.2345)
                drv.IFOpParamFloatSet("IVA", 21.0)
                drv.IFOpParamSet("CodigoProducto", "6935750533048")
                if not drv.IFOpSend(1):
                    self.cmd_error("ItemRetorno",drv)

                print("Cerrar")
                drv.IFOpBegin("Cerrar")
                if not drv.IFOpSend(1):
                    self.cmd_error("Cerrar",drv)
                print(" Numero: %s" % drv.IFOpRetGet("Numero"))
                print(" CodigoTipo: %s" % drv.IFOpRetGet("CodigoTipo"))
            elif command == "AuditoriaZ": # Informe de Auditoría resumido
                print("ImprimirAuditoriaResumidaPorZ")
                drv.IFOpBegin("ImprimirAuditoriaResumidaPorZ")
                drv.IFOpParamSet("ZInicial", f"{extra}")
                drv.IFOpParamSet("ZFinal", f"{extra1}")
                if not drv.IFOpSend(1):
                    self.cmd_error("ImprimirAuditoriaResumidaPorZ",drv)
            elif command == "AuditoriaF": # Informe de Auditoría resumido
                print("ImprimirAuditoriaResumidaPorFecha")
                drv.IFOpBegin("ImprimirAuditoriaResumidaPorFecha")
                drv.IFOpParamSet("FechaInicial", f"{extra}")
                drv.IFOpParamSet("FechaFinal", f"{extra1}")
                if not drv.IFOpSend(1):
                    self.cmd_error("ImprimirAuditoriaResumidaPorFecha",drv)
            elif command == "AuditoriaDZ": # Informe de Auditoría resumido
                print("ImprimirAuditoriaDetalladaPorZ")
                drv.IFOpBegin("ImprimirAuditoriaDetalladaPorZ")
                drv.IFOpParamSet("ZInicial", f"{extra}")
                drv.IFOpParamSet("ZFinal", f"{extra1}")
                if not drv.IFOpSend(1):
                    self.cmd_error("ImprimirAuditoriaDetalladaPorZ",drv)
            elif command == "AuditoriaDF": # Informe de Auditoría resumido
                print("ImprimirAuditoriaDetalladaPorFecha")
                drv.IFOpBegin("ImprimirAuditoriaDetalladaPorFecha")
                drv.IFOpParamSet("FechaInicial", f"{extra}")
                drv.IFOpParamSet("FechaFinal", f"{extra1}")
                if not drv.IFOpSend(1):
                    self.cmd_error("ImprimirAuditoriaDetalladaPorFecha",drv)
        except:
            return  drv.IFOpErrorDescGet()
        finally:
            drv.SerialPortClose()
Logic()