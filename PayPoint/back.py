import mysql.connector as sql
import win32print
import win32con
import win32com.client as winc
import json
import os
import sys
from datetime import datetime, timedelta
from supabase import create_client
import threading
import time

class Logic:
    def __init__(self):
        # Get the base path for configuration files
        # Ruta a %LOCALAPPDATA%\MiApp
        local_dir = os.path.join(os.getenv("LOCALAPPDATA"), "RSystems")
        os.makedirs(local_dir, exist_ok=True)  # Crear la carpeta si no existe

        # Ruta del archivo de configuración
        config_path = os.path.join(local_dir, "Configuration.json")

        # Si no existe el archivo, crearlo con valores por defecto
        if not os.path.exists(config_path):
            default_config = {
                "Db": "localhost",
                "User": "root",
                "Password": "",
                "Font": "0.8",
                "Com": "3",
                "Escaner": "",
                "Baudrate": "9600",
                "AdminPass": "888888",
                "EntryPass": "1",
                "SuperPass": "0",
                "Printer": "",
                "Supabase_url": "",
                "Supabase_key": ""
            }
            with open(config_path, "w") as f:
                json.dump(default_config, f, indent=4)
            print(f"Archivo de configuración creado en: {config_path}")
        else:
            print(f"Archivo de configuración encontrado en: {config_path}")

        # Cargar la configuración
        with open(config_path, "r") as archivo:
            self.datos = json.load(archivo)
        
        # Initialize Supabase client (optional)
        try:
            if self.datos.get("Supabase_url") and self.datos.get("Supabase_key"):
                self.supabase = create_client(
                    self.datos["Supabase_url"],
                    self.datos["Supabase_key"]
                )
            else:
                self.supabase = None
        except Exception as e:
            print(f"Warning: Supabase configuration not loaded: {str(e)}")
            self.supabase = None
        
        self.font = float(self.datos['Font'])
        
        # Start background sync thread only if Supabase is configured
        if self.supabase:
            self.sync_thread = threading.Thread(target=self._background_sync, daemon=True)
            self.sync_thread.start()

    def _background_sync(self):
        """Background thread that periodically syncs MySQL data to Supabase"""
        while True:
            try:
                self.sync_with_supabase()
            except Exception as e:
                print(f"Error in background sync: {str(e)}")
            time.sleep(1800)  # Wait 30 minutes (1800 seconds) before next sync attempt

    def sync_with_supabase(self):
        """Synchronize MySQL data with Supabase and maintain 730 days of history"""
        # Skip if Supabase is not configured
        if not self.supabase:
            return False
            
        try:
            # Ensure database connection is established
            if not hasattr(self, 'cursor'):
                self.Conection()
            
            # First, clean up old records in Supabase (older than 730 days)
            cutoff_date = (datetime.now() - timedelta(days=1095)).strftime('%Y-%m-%d')
            self.supabase.table('daily_sales').delete().lt('date', cutoff_date).execute()
            
            # Get all records from MySQL from the last 7 days
            self.cursor.execute("""
                SELECT 
                    DATE(CONVERT_TZ(Date, @@session.time_zone, '+00:00')) as date,
                    SUM(Facturated) as facturated,
                    SUM(Non_Facturated) as non_facturated,
                    SUM(Card) as card,
                    SUM(Cash) as cash,
                    SUM(Virtualp) as virtual_total,
                    SUM(Tcard) as tcard,
                    SUM(Tcash) as tcash,
                    SUM(Tvirtual) as tvirtual,
                    SUM(TCancelled) as tcancelled,
                    SUM(Cancelled) as cancelled
                FROM Caja1 
                WHERE Date >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
                GROUP BY DATE(CONVERT_TZ(Date, @@session.time_zone, '+00:00'))
            """)
            
            mysql_records = self.cursor.fetchall()
            
            for record in mysql_records:
                try:
                    # Ensure date is in UTC and format as YYYY-MM-DD
                    date_str = record[0].strftime('%Y-%m-%d')
                    print(f"Processing date: {date_str}")  # Debug log
                    
                    # Check if record exists in Supabase
                    result = self.supabase.table('daily_sales').select('*').eq('date', date_str).execute()
                    
                    data = {
                        'invoiced_total': float(record[1]) if record[1] else 0,
                        'non_invoiced_total': float(record[2]) if record[2] else 0,
                        'card_total': float(record[3]) if record[3] else 0,
                        'cash_total': float(record[4]) if record[4] else 0,
                        'virtual_total': float(record[5]) if record[5] else 0,
                        'card_transactions': int(record[6]) if record[6] else 0,
                        'cash_transactions': int(record[7]) if record[7] else 0,
                        'virtual_transactions': int(record[8]) if record[8] else 0,
                        'cancelled_transactions': int(record[9]) if record[9] else 0,
                        'cancelled_total': float(record[10]) if record[10] else 0,
                        'updated_at': datetime.utcnow().isoformat()
                    }
                    
                    if result.data:
                        # Update existing record
                        self.supabase.table('daily_sales').update(data).eq('date', date_str).execute()
                    else:
                        # Insert new record
                        data['date'] = date_str
                        data['created_at'] = datetime.utcnow().isoformat()
                        self.supabase.table('daily_sales').insert(data).execute()
                except Exception as e:
                    print(f"Error processing record for date {date_str}: {str(e)}")
                    continue
                
            return True
        except Exception as e:
            print(f"Error syncing with Supabase: {str(e)}")
            return False

    def writeCfg(self):
        # Get the base path for configuration files
        local_dir = os.path.join(os.getenv("LOCALAPPDATA"), "RSystems")
        os.makedirs(local_dir, exist_ok=True)
        
        # Ruta del archivo de configuración
        config_path = os.path.join(local_dir, "Configuration.json")
        
        # Guardar la configuración actualizada
        with open(config_path, "w") as f:
            json.dump(self.datos, f, indent=4)
        
        # Reinicializar Supabase si las credenciales están presentes
        try:
            if self.datos.get("Supabase_url") and self.datos.get("Supabase_key"):
                self.supabase = create_client(
                    self.datos["Supabase_url"],
                    self.datos["Supabase_key"]
                )
                # Reiniciar el hilo de sincronización si es necesario
                if not hasattr(self, 'sync_thread') or not self.sync_thread.is_alive():
                    self.sync_thread = threading.Thread(target=self._background_sync, daemon=True)
                    self.sync_thread.start()
            else:
                self.supabase = None
        except Exception as e:
            print(f"Warning: Failed to reinitialize Supabase: {str(e)}")
            self.supabase = None

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
        
    
    def imprimir_ticket(self,productos, nombre_impresora=None):
        # Configuración precis
        ANCHO_TICKET = 47
        PRICE_WIDTH = 11   # Ancho fijo para precios
        DESC_WIDTH = ANCHO_TICKET - PRICE_WIDTH - 1  # 35 caracteres
        TRUNCATE_LENGTH = DESC_WIDTH - 3  # 32 caracteres antes de "..."
    # Obtener la fecha y hora actual
        now = datetime.now()

        # Formatear la fecha y hora en un formato compacto
        
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  
        ticket = []
        ticket.append("\x1B@")  # Inicializar impresora
        ticket.append("\x1B!\x02")  # Fuente pequeña
        
        # Encabezado
        ticket.append("\x1B\x61\x01")  # Centrado
        ticket.append("SUPERMERCADO \n")
        ticket.append("\x1B\x61\x00")  # Alinear izquierda
        ticket.append("=" * ANCHO_TICKET + "\n")
        ticket.append(f"{formatted_time}\n\n")
        # Función de truncamiento exacto
        def truncar_descripcion(texto):
            if len(texto) > DESC_WIDTH:
                return texto[:TRUNCATE_LENGTH] + "..."
            return texto.ljust(DESC_WIDTH)  # Rellena con espacios si es corto
        
        # Procesar productos
        for desc, precio_unitario, cantidad in productos:
            total = precio_unitario * cantidad
            
            # Línea de cantidad y precio unitario
            if cantidad > 1:
                linea_cantidad = f"{cantidad}x ${precio_unitario:>10,.2f}"
                ticket.append(linea_cantidad.ljust(ANCHO_TICKET) + "\n")
            
            # Línea de descripción y precio
            desc_truncada = truncar_descripcion(desc)
            precio_str = f"${total:>{PRICE_WIDTH-1},.2f}" if cantidad > 1 else f"${precio_unitario:>{PRICE_WIDTH-1},.2f}"
            linea_producto = f"{desc_truncada} {precio_str}"
            ticket.append(linea_producto + "\n")

        ticket.append("=" * ANCHO_TICKET + "\n")   
        # Total general
        total_general = sum(p[1] * p[2] for p in productos)
        ticket.append(f"{'TOTAL:'.ljust(DESC_WIDTH)} ${total_general:>{PRICE_WIDTH-1},.2f}\n")
        
        # Pie del ticket
        ticket.append("\n\x1B\x61\x01")  # Centrado
        ticket.append("GRACIAS POR SU COMPRA\n")
        ticket.append("\n" * 5)  # Espacio para corte
        ticket.append("\x1D\x56\x41\x05")  # Corte parcial
        
        # Impresión
        if not nombre_impresora:
            nombre_impresora = win32print.GetDefaultPrinter()
        
        hprinter = win32print.OpenPrinter(nombre_impresora)
        try:
            win32print.StartDocPrinter(hprinter, 1, ("Ticket", None, "RAW"))
            win32print.StartPagePrinter(hprinter)
            contenido = "".join(ticket).encode('cp850', 'replace')
            win32print.WritePrinter(hprinter, contenido)
        finally:
            win32print.EndPagePrinter(hprinter)
            win32print.EndDocPrinter(hprinter)
            win32print.ClosePrinter(hprinter)
            
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

    def update_caja1(self, facturated=0, non_facturated=0, card=0, cash=0, virtual=0, tcard=0, tcash=0, tvirtual=0, tcancelled=0, cancelled=0):
        try:
            print(f"Intentando actualizar Caja1 con valores: facturated={facturated}, non_facturated={non_facturated}, card={card}, cash={cash}, virtual={virtual}, tcard={tcard}, tcash={tcash}, tvirtual={tvirtual}, tcancelled={tcancelled}, cancelled={cancelled}")
            
            # Verificar si la tabla existe
            self.cursor.execute("SHOW TABLES LIKE 'Caja1'")
            if not self.cursor.fetchone():
                print("La tabla Caja1 no existe, creándola...")
                self.cursor.execute("""
                    CREATE TABLE Caja1 (
                        Date DATETIME PRIMARY KEY,
                        Facturated DECIMAL(10,2),
                        Non_Facturated DECIMAL(10,2),
                        Card DECIMAL(10,2),
                        Cash DECIMAL(10,2),
                        virtualp DECIMAL(10,2),
                        Tcard INT,
                        Tcash INT,
                        Tvirtual INT,
                        TCancelled INT,
                        Cancelled DECIMAL(10,2)
                    )
                """)
                print("Tabla Caja1 creada exitosamente")
            
            # Eliminar registros antiguos
            self.cursor.execute("DELETE FROM Caja1 WHERE Date < DATE_SUB(NOW(), INTERVAL 7 DAY)")
            print("Registros antiguos eliminados")
            
            # Verificar si ya existe un registro para la fecha actual
            self.cursor.execute("SELECT * FROM Caja1 WHERE DATE(Date) = CURDATE()")
            existing_record = self.cursor.fetchone()
            
            if existing_record:
                print("Actualizando registro existente")
                # Actualizar el registro existente
                self.cursor.execute("""
                    UPDATE Caja1 
                    SET Facturated = Facturated + %s,
                        Non_Facturated = Non_Facturated + %s,
                        Card = Card + %s,
                        Cash = Cash + %s,
                        virtualp = virtualp + %s,
                        Tcard = Tcard + %s,
                        Tcash = Tcash + %s,
                        Tvirtual = Tvirtual + %s,
                        TCancelled = TCancelled + %s,
                        Cancelled = Cancelled + %s
                    WHERE DATE(Date) = CURDATE()
                """, (facturated, non_facturated, card, cash, virtual, tcard, tcash, tvirtual, tcancelled, cancelled))
            else:
                print("Insertando nuevo registro")
                # Insertar nuevo registro
                self.cursor.execute("""
                    INSERT INTO Caja1 (Date, Facturated, Non_Facturated, Card, Cash, virtualp, Tcard, Tcash, Tvirtual, TCancelled, Cancelled)
                    VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (facturated, non_facturated, card, cash, virtual, tcard, tcash, tvirtual, tcancelled, cancelled))
            
            print("Commit de la transacción")
            self.mydb.commit()
            
            # Intentar sincronizar con Supabase si está configurado
            try:
                if self.supabase:
                    print("Intentando sincronizar con Supabase")
                    self.sync_with_supabase()
                else:
                    print("Supabase no está configurado")
            except Exception as e:
                print(f"Error al sincronizar con Supabase: {str(e)}")
                
        except Exception as e:
            print(f"Error en update_caja1: {str(e)}")
            raise

    def cmd_error (self,cmdname,drv):
        "Manejo error en comando"
        err = drv.IFOpErrorGet()
        errdesc = drv.IFOpErrorDescGet()
        print("Error %d en comando %s: %s" % (err, cmdname, errdesc))
        exit()
    def main(self,command,status=0, extra=0, extra1=0, event=0, iva=0):
        
        drv = winc.Dispatch("Sam4sFiscalDriver.Sam4sFiscalDriver")
        try:
            if not drv.SerialBaudSet(self.baudrate):
                print("Error: no se pudo configurar la velocidad %s", self.baudrate)
                exit()

            if not drv.SerialPortOpen(self.comnum):
                    print("Error: no se pudo abrir el puerto serial %d" % self.comnum)
                    exit()
        except:
            print("error")
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
                iva_s= format(iva, '.2f')
                l=25-len(iva_s)
                x= "-"
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 11)
                drv.IFOpParamSet("Texto", 40*x)
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 12)
                drv.IFOpParamSet("Texto", "REGIMEN DE TRANSPARENCIA FISCAL AL")
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 13)
                drv.IFOpParamSet("Texto", "CONSUMIDOR (LEY 27.743)")
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 14)
                drv.IFOpParamSet("Texto", f"IVA CONTENIDO{l*' '}$ {iva_s}")
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 15)
                drv.IFOpParamSet("Texto", "OTROS IMPUESTOS NACIONALES INDIRECTOS")
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 16)
                drv.IFOpParamSet("Texto", "Imp. Internos Importados          $ 0.00")
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 17)
                drv.IFOpParamSet("Texto", 'LOS IMPUESTOS INFORMADOS SON SOLO LOS')
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 18)
                drv.IFOpParamSet("Texto", 'QUE CORRESPONDEN A NIVEL NACIONAL')
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
                drv.IFOpBegin("EstablecerEncabezadoCola")
                drv.IFOpParamIntSet("Numero", 19)
                drv.IFOpParamSet("Texto", 40*x)
                if not drv.IFOpSend(1):
                    self.cmd_error("EstablecerEncabezadoCola",drv)
    
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
            elif command == "AbrirC": # Informe de Auditoría resumido
                drv.IFOpBegin("AbrirCajon")
                if not drv.IFOpSend(1):
                    self.cmd_error("AbrirCajon",drv)

        except:
            return  drv.IFOpErrorDescGet()
        finally:
            drv.SerialPortClose()
    

Logic()