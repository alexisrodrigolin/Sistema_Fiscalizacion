/*
	Ejemplo de uso de Sam4sFiscalDriver.dll
	2019-04-03
*/
using System;
using System.IO;
using System.Runtime.InteropServices;

namespace test
{
	class Sam4sFiscalDriver
	{
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="SerialPortOpen")]
		static extern int dllSerialPortOpen (int comnum);
		public int SerialPortOpen (int comnum) {
			return dllSerialPortOpen(comnum);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="SerialBaudSet")]
		static extern int dllSerialBaudSet (int nbaud);
		public int SerialBaudSet (int nbaud) {
			return dllSerialBaudSet(nbaud);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="SerialPortClose")]
		static extern int dllSerialPortClose ();
		public int SerialPortClose () {
			return dllSerialPortClose();
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpBegin")]
		static extern int dllIFOpBegin (string name);
		public int IFOpBegin (string name) {
			return dllIFOpBegin(name);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpSend")]
		static extern int dllIFOpSend (int wait);
		public int IFOpSend (int wait) {
			return dllIFOpSend(wait);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpWaitingIs")]
		static extern int dllIFOpWaitingIs ();
		public int IFOpWaitingIs () {
			return dllIFOpWaitingIs();
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpAbort")]
		static extern int dllIFOpAbort ();
		public int IFOpAbort () {
			return dllIFOpAbort();
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamSet")]
		static extern int dllIFOpParamSet (string name, string value);
		public int IFOpParamSet (string name, string value) {
			return dllIFOpParamSet(name, value);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamGet")]
		static extern IntPtr dllIFOpParamGet (string name);
		public string IFOpParamGet (string name) {
			return Marshal.PtrToStringAnsi(dllIFOpParamGet(name));
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamIntSet")]
		static extern int dllIFOpParamIntSet (string name, int value);
		public int IFOpParamIntSet (string name, int value) {
			return dllIFOpParamIntSet(name, value);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamIntGet")]
		static extern int dllIFOpParamIntGet (string name);
		public int IFOpParamIntGet (string name) {
			return dllIFOpParamIntGet(name);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamFloatSet")]
		static extern int dllIFOpParamFloatSet (string name, double value);
		public int IFOpParamFloatSet (string name, double value) {
			return dllIFOpParamFloatSet(name, value);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamFloatGet")]
		static extern double dllIFOpParamFloatGet (string name);
		public double IFOpParamFloatGet (string name) {
			return dllIFOpParamFloatGet(name);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamBoolSet")]
		static extern int dllIFOpParamBoolSet (string name, int value);
		public int IFOpParamBoolSet (string name, int value) {
			return dllIFOpParamBoolSet(name, value);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamBoolGet")]
		static extern int dllIFOpParamBoolGet (string name);
		public int IFOpParamBoolGet (string name) {
			return dllIFOpParamBoolGet(name);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpCmdOkIs")]
		static extern int dllIFOpCmdOkIs ();
		public int IFOpCmdOkIs () {
			return dllIFOpCmdOkIs();
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpErrorGet")]
		static extern int dllIFOpErrorGet ();
		public int IFOpErrorGet () {
			return dllIFOpErrorGet();
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpErrorDescGet")]
		static extern IntPtr dllIFOpErrorDescGet ();
		public string IFOpErrorDescGet () {
			return Marshal.PtrToStringAnsi(dllIFOpErrorDescGet());
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpStateGet")]
		static extern int dllIFOpStateGet (string name);
		public int IFOpStateGet (string name) {
			return dllIFOpStateGet(name);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpRetGet")]
		static extern IntPtr dllIFOpRetGet (string name);
		public string IFOpRetGet (string name) {
			return Marshal.PtrToStringAnsi(dllIFOpRetGet(name));
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpRetIntGet")]
		static extern int dllIFOpRetIntGet (string name);
		public int IFOpRetIntGet (string name) {
			return dllIFOpRetIntGet(name);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpRetFloatGet")]
		static extern double dllIFOpRetFloatGet (string name);
		public double IFOpRetFloatGet (string name) {
			return dllIFOpRetFloatGet(name);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpRetBoolGet")]
		static extern int dllIFOpRetBoolGet (string name);
		public int IFOpRetBoolGet (string name) {
			return dllIFOpRetBoolGet(name);
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpListGet")]
		static extern IntPtr dllIFOpListGet (int idx);
		public string IFOpListGet (int idx) {
			return Marshal.PtrToStringAnsi(dllIFOpListGet(idx));
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpParamListGet")]
		static extern IntPtr dllIFOpParamListGet (int idx);
		public string IFOpParamListGet (int idx) {
			return Marshal.PtrToStringAnsi(dllIFOpParamListGet(idx));
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpRetListGet")]
		static extern IntPtr dllIFOpRetListGet (int idx);
		public string IFOpRetListGet (int idx) {
			return Marshal.PtrToStringAnsi(dllIFOpRetListGet(idx));
		}
		[DllImport("Sam4sFiscalDriver.dll", EntryPoint="IFOpStateListGet")]
		static extern IntPtr dllIFOpStateListGet (int idx);
		public string IFOpStateListGet (int idx) {
			return Marshal.PtrToStringAnsi(dllIFOpStateListGet(idx));
		}

	}

    class Program
    {
		static void cmd_error(string cmdname, Sam4sFiscalDriver drv)
		{
			Console.WriteLine("Error {0} en comando {1}: {2}",
				drv.IFOpErrorGet(), cmdname, drv.IFOpErrorDescGet());
			System.Environment.Exit(1);
		}

        static int Main(string[] args)
        {
            if (args.Length < 2)
            {
				Console.WriteLine("Error: insuficientes parámetros");
                Console.WriteLine("Uso: test [numero_puerto] [baudios] [prueba]");
                Console.WriteLine("Pruebas: info tique tnc factura credito debito recibo generico interno voucher remitor remitox recibox presupuesto donacion tiqueinfo printertest reimprimir cancel totalestique config x z auditoria misc eventlog rptpend rptzdown");
                return -1000;
            }
            int comnum = int.Parse(args[0]);
            int baudrate = int.Parse(args[1]);
            String testname = args[2];
            String extra1 = (args.Length > 3) ? args[3] : "";
            String extra2 = (args.Length > 4) ? args[4] : "";
            
            Sam4sFiscalDriver drv = new Sam4sFiscalDriver();
            
            if (drv.SerialBaudSet(baudrate) == 0)
			{
				Console.WriteLine("Error: no se pudo configurar la velocidad {0}", baudrate);
				return 2;
			}
            
            if (drv.SerialPortOpen(comnum) == 0)
			{
				Console.WriteLine("Error: no se pudo abrir el puerto serial {0}", comnum);
				return 2;
			}
			
			drv.IFOpBegin("DocumentoEnCurso");
			if (drv.IFOpSend(1) == 0)
				cmd_error("DocumentoEnCurso",drv);
			if (drv.IFOpRetIntGet("CodigoTipo")!=0)
				drv.IFOpBegin("Cancelar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cancelar",drv);
			
			if (testname == "info") // Información del equipo
			{
				Console.WriteLine("Estado");
				drv.IFOpBegin("Estado");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Estado",drv);
				Console.WriteLine(" FechaAperturaJornada: {0}", drv.IFOpRetGet("FechaAperturaJornada"));
				Console.WriteLine(" HoraAperturaJornada: {0}", drv.IFOpRetGet("HoraAperturaJornada"));
				Console.WriteLine(" NumeroUltimoZ: {0}", drv.IFOpRetIntGet("NumeroUltimoZ"));
				Console.WriteLine(" NumeroRegistro: {0}", drv.IFOpRetGet("NumeroRegistro"));
				Console.WriteLine(" Version: {0}", drv.IFOpRetGet("Version"));

				Console.WriteLine("CaracteristicasEquipo");
				drv.IFOpBegin("CaracteristicasEquipo");
				if (drv.IFOpSend(1) == 0)
					cmd_error("CaracteristicasEquipo",drv);
				Console.WriteLine(" AnchoTique: {0}", drv.IFOpRetIntGet("AnchoTique"));
				Console.WriteLine(" EmiteTiqueFiscal: {0}", (drv.IFOpRetBoolGet("EmiteTiqueFiscal")!=0) ? "Si" : "No");
				Console.WriteLine(" EmiteTiqueFactura: {0}", (drv.IFOpRetBoolGet("EmiteTiqueFactura")!=0) ? "Si" : "No");
				Console.WriteLine(" EmiteFactura: {0}", (drv.IFOpRetBoolGet("EmiteFactura")!=0) ? "Si" : "No");
				Console.WriteLine(" DigitosDecimales: {0}", drv.IFOpRetIntGet("DigitosDecimales"));
				Console.WriteLine(" ModeloVersion: {0}", drv.IFOpRetGet("ModeloVersion"));

				Console.WriteLine("DatosContribuyente");
				drv.IFOpBegin("DatosContribuyente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosContribuyente",drv);
				Console.WriteLine(" CUIT: {0}", drv.IFOpRetGet("CUIT"));
				Console.WriteLine(" PV: {0}", drv.IFOpRetGet("PV"));
				Console.WriteLine(" ResponsabilidadIVA: {0}", drv.IFOpRetGet("ResponsabilidadIVA"));
				Console.WriteLine(" IVAEstandar: {0}", drv.IFOpRetFloatGet("IVAEstandar"));
				Console.WriteLine(" MaximoTiqueFactura: {0}", drv.IFOpRetFloatGet("MaximoTiqueFactura"));
				Console.WriteLine(" MaximoTique: {0}", drv.IFOpRetFloatGet("MaximoTique"));
				Console.WriteLine(" RazonSocial: {0}", drv.IFOpRetGet("RazonSocial"));
				Console.WriteLine(" TipoHabilitacion: {0}", drv.IFOpRetGet("TipoHabilitacion"));
				Console.WriteLine(" IngresosBrutos: {0}", drv.IFOpRetGet("IngresosBrutos"));
				Console.WriteLine(" InicioActividades: {0}", drv.IFOpRetGet("InicioActividades"));

				Console.WriteLine("DocumentoEnCurso");
				drv.IFOpBegin("DocumentoEnCurso");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DocumentoEnCurso",drv);
				Console.WriteLine(" Tipo: {0}", drv.IFOpRetGet("Tipo"));
				Console.WriteLine(" Letra: {0}", drv.IFOpRetGet("Letra"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetIntGet("CodigoTipo"));
				Console.WriteLine(" Numero: {0}", drv.IFOpRetIntGet("Numero"));

				Console.WriteLine("FechaHora");
				drv.IFOpBegin("FechaHora");
				if (drv.IFOpSend(1) == 0)
					cmd_error("FechaHora",drv);
				Console.WriteLine(" Fecha: {0}", drv.IFOpRetGet("Fecha"));
				Console.WriteLine(" Hora: {0}", drv.IFOpRetGet("Hora"));

				Console.WriteLine("Ethernet");
				drv.IFOpBegin("Ethernet");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Ethernet",drv);
				Console.WriteLine(" DireccionIP: {0}", drv.IFOpRetGet("DireccionIP"));
				Console.WriteLine(" MascaraRed: {0}", drv.IFOpRetGet("MascaraRed"));
				Console.WriteLine(" PuertaEnlace: {0}", drv.IFOpRetGet("PuertaEnlace"));
				Console.WriteLine(" MAC: {0}", drv.IFOpRetGet("MAC"));

				Console.WriteLine("ConfiguracionUSB");
				drv.IFOpBegin("ConfiguracionUSB");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ConfiguracionUSB",drv);
				Console.WriteLine(" Modo: {0}", drv.IFOpRetGet("Modo"));

				Console.WriteLine("DescargasPendientes");
				drv.IFOpBegin("DescargasPendientes");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DescargasPendientes",drv);
				Console.WriteLine(" PrimerZPendiente: {0}", drv.IFOpRetGet("PrimerZPendiente"));
				Console.WriteLine(" FechaPrimerZPendiente: {0}", drv.IFOpRetGet("FechaPrimerZPendiente"));
				Console.WriteLine(" HoraPrimerZPendiente: {0}", drv.IFOpRetGet("HoraPrimerZPendiente"));
				Console.WriteLine(" UltimoZPendiente: {0}", drv.IFOpRetGet("UltimoZPendiente"));
				Console.WriteLine(" FechaUltimoZPendiente: {0}", drv.IFOpRetGet("FechaUltimoZPendiente"));
				Console.WriteLine(" HoraUltimoZPendiente: {0}", drv.IFOpRetGet("HoraUltimoZPendiente"));
				Console.WriteLine(" CantidadGeneracionesNoDescargadas: {0}", drv.IFOpRetGet("CantidadGeneracionesNoDescargadas"));
				Console.WriteLine(" PrimerGeneracionNoDescargada: {0}", drv.IFOpRetGet("PrimerGeneracionNoDescargada"));
			}
			else if (testname == "tique") // Tique
			{
				Console.WriteLine("AbrirTique");
				drv.IFOpBegin("AbrirTique");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirTique",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba");
				drv.IFOpParamFloatSet("Precio", 1.2345);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoProducto", "7791234567898");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));

				Console.WriteLine("AbrirCajon");
				drv.IFOpBegin("AbrirCajon");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirCajon",drv);
			}
			else if (testname == "tnc") // Tique Nota de Credito
			{
				Console.WriteLine("ComprobanteAsociado");
				drv.IFOpBegin("ComprobanteAsociado");
				drv.IFOpParamIntSet("CodigoTipo", 83);
				drv.IFOpParamIntSet("PV", 12345);
				drv.IFOpParamIntSet("Numero", 12345678);
				if (drv.IFOpSend(1) == 0)
					cmd_error("ComprobanteAsociado",drv);

				Console.WriteLine("AbrirTiqueNotaCredito");
				drv.IFOpBegin("AbrirTiqueNotaCredito");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirTiqueNotaCredito",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción extra del ítem");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba");
				drv.IFOpParamFloatSet("Cantidad", 3.0);
				drv.IFOpParamFloatSet("Precio", 1.2345);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoProducto", "6935750533048");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción extra del ítem");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("ItemRetorno");
				drv.IFOpBegin("ItemRetorno");
				drv.IFOpParamSet("Descripcion", "Item de prueba");
				drv.IFOpParamFloatSet("Cantidad", 2.0);
				drv.IFOpParamFloatSet("Precio", 1.2345);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoProducto", "6935750533048");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemRetorno",drv);

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "factura") // Factura
			{
				Console.WriteLine("AbrirFactura");
				drv.IFOpBegin("AbrirFactura");
				drv.IFOpParamSet("ClienteResponsabilidad", "I");
				drv.IFOpParamSet("ClienteRazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("ClienteTipoDocumento", "CUIT");
				drv.IFOpParamSet("ClienteNumeroDocumento", "11111111113");
				drv.IFOpParamSet("ClienteDomicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirFactura",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 1");
				drv.IFOpParamFloatSet("Cantidad", 3.0);
				drv.IFOpParamFloatSet("Precio", 1.2345);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 2");
				drv.IFOpParamFloatSet("Cantidad", 1.0);
				drv.IFOpParamFloatSet("Precio", 1.2);
				drv.IFOpParamFloatSet("IVA", 10.5);
				drv.IFOpParamSet("CodigoInterno", "1002");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 3");
				drv.IFOpParamFloatSet("Precio", 1.3);
				drv.IFOpParamFloatSet("IVA", 0.0);
				drv.IFOpParamSet("CodigoInterno", "1003");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 4");
				drv.IFOpParamFloatSet("Precio", 1.4);
				drv.IFOpParamSet("IVA", "E");
				drv.IFOpParamSet("CodigoInterno", "1004");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 5");
				drv.IFOpParamFloatSet("Precio", 1.5);
				drv.IFOpParamSet("IVA", "N");
				drv.IFOpParamSet("CodigoInterno", "1005");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 6");
				drv.IFOpParamFloatSet("Precio", 1.6);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamFloatSet("MontoImpIntFijo", 0.6);
				drv.IFOpParamSet("CodigoInterno", "1006");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 7");
				drv.IFOpParamFloatSet("Precio", 1.7);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamFloatSet("TasaAjuste", 0.14893617);
				drv.IFOpParamSet("CodigoInterno", "1007");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("SubtotalImpreso");
				drv.IFOpBegin("SubtotalImpreso");
				if (drv.IFOpSend(1) == 0)
					cmd_error("SubtotalImpreso",drv);
				Console.WriteLine(" CantidadItems: {0}", drv.IFOpRetGet("CantidadItems"));
				Console.WriteLine(" Total: {0}", drv.IFOpRetFloatGet("Total"));
				Console.WriteLine(" IVA: {0}", drv.IFOpRetFloatGet("IVA"));
				Console.WriteLine(" Pagado: {0}", drv.IFOpRetFloatGet("Pagado"));
				Console.WriteLine(" ImpIntPorc: {0}", drv.IFOpRetFloatGet("ImpIntPorc"));
				Console.WriteLine(" ImpIntFijo: {0}", drv.IFOpRetFloatGet("ImpIntFijo"));
				Console.WriteLine(" Neto: {0}", drv.IFOpRetFloatGet("Neto"));

				Console.WriteLine("ItemBonificacion");
				drv.IFOpBegin("ItemBonificacion");
				drv.IFOpParamSet("Descripcion", "Decuento articulo");
				drv.IFOpParamFloatSet("Cantidad", 3.0);
				drv.IFOpParamFloatSet("Precio", 0.12345);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoInterno", "1001b");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemBonificacion",drv);

				Console.WriteLine("ItemRetornoBonificacion");
				drv.IFOpBegin("ItemRetornoBonificacion");
				drv.IFOpParamSet("Descripcion", "Decuento articulo");
				drv.IFOpParamFloatSet("Cantidad", 1.0);
				drv.IFOpParamFloatSet("Precio", 0.12345);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoInterno", "1001b");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemRetornoBonificacion",drv);

				Console.WriteLine("OtroTributo");
				drv.IFOpBegin("OtroTributo");
				drv.IFOpParamIntSet("CodigoTipo", 7);
				drv.IFOpParamFloatSet("Monto", 5.0);
				if (drv.IFOpSend(1) == 0)
					cmd_error("OtroTributo",drv);

				Console.WriteLine("Pago");
				drv.IFOpBegin("Pago");
				drv.IFOpParamFloatSet("Monto", 50.0);
				drv.IFOpParamIntSet("CodigoTipo", 8);
				if (drv.IFOpSend(1) == 0)
					cmd_error("Pago",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));

				Console.WriteLine("SubtotalInfo");
				drv.IFOpBegin("SubtotalInfo");
				if (drv.IFOpSend(1) == 0)
					cmd_error("SubtotalInfo",drv);
				Console.WriteLine(" CantidadItems: {0}", drv.IFOpRetGet("CantidadItems"));
				Console.WriteLine(" Total: {0}", drv.IFOpRetFloatGet("Total"));
				Console.WriteLine(" IVA: {0}", drv.IFOpRetFloatGet("IVA"));
				Console.WriteLine(" Pagado: {0}", drv.IFOpRetFloatGet("Pagado"));
				Console.WriteLine(" ImpIntPorc: {0}", drv.IFOpRetFloatGet("ImpIntPorc"));
				Console.WriteLine(" ImpIntFijo: {0}", drv.IFOpRetFloatGet("ImpIntFijo"));
				Console.WriteLine(" Neto: {0}", drv.IFOpRetFloatGet("Neto"));
			}
			else if (testname == "credito") // Nota de Crédito
			{
				Console.WriteLine("AbrirNotaCredito");
				drv.IFOpBegin("AbrirNotaCredito");
				drv.IFOpParamSet("ClienteResponsabilidad", "M");
				drv.IFOpParamSet("ClienteRazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("ClienteTipoDocumento", "CUIT");
				drv.IFOpParamSet("ClienteNumeroDocumento", "11111111113");
				drv.IFOpParamSet("ClienteDomicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirNotaCredito",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba");
				drv.IFOpParamFloatSet("Cantidad", 3.0);
				drv.IFOpParamFloatSet("Precio", 1.5);
				drv.IFOpParamFloatSet("IVA", 10.5);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemSena");
				drv.IFOpBegin("ItemSena");
				drv.IFOpParamSet("Descripcion", "Item de seña");
				drv.IFOpParamFloatSet("Cantidad", 3.0);
				drv.IFOpParamFloatSet("Precio", 3.2);
				drv.IFOpParamFloatSet("IVA", 0.0);
				drv.IFOpParamSet("CodigoInterno", "2001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemSena",drv);

				Console.WriteLine("ItemRetornoSena");
				drv.IFOpBegin("ItemRetornoSena");
				drv.IFOpParamSet("Descripcion", "Item de seña");
				drv.IFOpParamFloatSet("Cantidad", -2.0);
				drv.IFOpParamFloatSet("Precio", -3.2);
				drv.IFOpParamFloatSet("IVA", 0.0);
				drv.IFOpParamSet("CodigoInterno", "2001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemRetornoSena",drv);

				Console.WriteLine("DescuentoGeneral");
				drv.IFOpBegin("DescuentoGeneral");
				drv.IFOpParamSet("Descripcion", "Oferta del día");
				drv.IFOpParamFloatSet("Monto", 2.4);
				if (drv.IFOpSend(1) == 0)
					cmd_error("DescuentoGeneral",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Pago");
				drv.IFOpBegin("Pago");
				drv.IFOpParamFloatSet("Monto", 20.0);
				if (drv.IFOpSend(1) == 0)
					cmd_error("Pago",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "debito") // Nota de Débito
			{
				Console.WriteLine("AbrirNotaDebito");
				drv.IFOpBegin("AbrirNotaDebito");
				drv.IFOpParamSet("ClienteResponsabilidad", "F");
				drv.IFOpParamSet("ClienteRazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("ClienteTipoDocumento", "DNI");
				drv.IFOpParamSet("ClienteNumeroDocumento", "11222333");
				drv.IFOpParamSet("ClienteDomicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirNotaDebito",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 1");
				drv.IFOpParamFloatSet("Precio", 1.5);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 2");
				drv.IFOpParamFloatSet("Precio", 0.5);
				drv.IFOpParamFloatSet("IVA", 10.5);
				drv.IFOpParamSet("CodigoInterno", "1002");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("RecargoGeneral");
				drv.IFOpBegin("RecargoGeneral");
				drv.IFOpParamSet("Descripcion", "Recargo administrativo");
				drv.IFOpParamFloatSet("Monto", 2.0);
				if (drv.IFOpSend(1) == 0)
					cmd_error("RecargoGeneral",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Pago");
				drv.IFOpBegin("Pago");
				drv.IFOpParamSet("Descripcion", "CTA 123458");
				drv.IFOpParamFloatSet("Monto", 20.0);
				drv.IFOpParamIntSet("CodigoTipo", 6);
				drv.IFOpParamSet("TextoLibre", "Vencimiento XX/XX/XXXX");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Pago",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "recibo") // Recibo
			{
				Console.WriteLine("AbrirRecibo");
				drv.IFOpBegin("AbrirRecibo");
				drv.IFOpParamSet("ClienteResponsabilidad", "I");
				drv.IFOpParamSet("ClienteRazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("ClienteTipoDocumento", "CUIT");
				drv.IFOpParamSet("ClienteNumeroDocumento", "11111111113");
				drv.IFOpParamSet("ClienteDomicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirRecibo",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba");
				drv.IFOpParamFloatSet("Precio", 2.5);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("Pago");
				drv.IFOpBegin("Pago");
				drv.IFOpParamSet("Descripcion", "Tarjeta XXXX");
				drv.IFOpParamFloatSet("Monto", 5.0);
				drv.IFOpParamIntSet("CodigoTipo", 20);
				drv.IFOpParamSet("Cuotas", "12");
				drv.IFOpParamSet("Cupones", "XXX-XX-XXXX");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Pago",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "generico") // Documento Generico
			{
				Console.WriteLine("AbrirDocGenerico");
				drv.IFOpBegin("AbrirDocGenerico");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirDocGenerico",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Línea de texto no fiscal");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "abc \\R\\Resaltado\\f\\ def");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "abc \\A\\Doble alto\\f\\ def");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "abc \\N\\Doble ancho\\f\\ def");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "abc \\S\\Subrayado\\f\\ def");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "abc \\AN\\Doble A&A\\f\\ def");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "CODE 39 \\xE1\\A1+-.$/%\\xE0\\");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Interleaved \\xE3\\1122334455\\xE0\\");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "UPC A \\xE5\\123456789012\\xE0\\");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "EAN 13 \\xE7\\123456789012\\xE0\\");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "EAN 8 \\xEA\\12345678\\xE0\\");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "CODABAR \\xEC\\D164-$:/.+B-\\xE0\\");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "interno") // Documento de Uso Interno
			{
				Console.WriteLine("AbrirDocInterno");
				drv.IFOpBegin("AbrirDocInterno");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirDocInterno",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Línea de texto no fiscal");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "voucher") // Voucher de Tarjeta de Crédito
			{
				Console.WriteLine("AbrirDNFH");
				drv.IFOpBegin("AbrirDNFH");
				drv.IFOpParamIntSet("CodigoTipo", 922);
				drv.IFOpParamSet("Atributos", "difat");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirDNFH",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 1);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 2);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 3);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "09/14");
				drv.IFOpParamIntSet("Tipo", 4);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 5);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Línea libre 1 (opcional)");
				drv.IFOpParamIntSet("Tipo", 19);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Línea libre 2 (opcional)");
				drv.IFOpParamIntSet("Tipo", 20);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Línea libre 3 (opcional)");
				drv.IFOpParamIntSet("Tipo", 21);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 6);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 7);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 8);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 9);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 10);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 11);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 12);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Línea libre 4 (opcional)");
				drv.IFOpParamIntSet("Tipo", 22);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Línea libre 5 (opcional)");
				drv.IFOpParamIntSet("Tipo", 23);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Línea libre 6 (opcional)");
				drv.IFOpParamIntSet("Tipo", 24);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 13);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 14);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 15);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 16);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 17);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("TextoNoFiscal");
				drv.IFOpBegin("TextoNoFiscal");
				drv.IFOpParamSet("Texto", "Dato libre");
				drv.IFOpParamIntSet("Tipo", 18);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoNoFiscal",drv);

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "remitor") // Remito R
			{
				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "0");
				drv.IFOpParamSet("Responsabilidad", "I");
				drv.IFOpParamSet("RazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("TipoDocumento", "CUIT");
				drv.IFOpParamSet("NumeroDocumento", "11111111113");
				drv.IFOpParamSet("Domicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "2");
				drv.IFOpParamSet("Responsabilidad", "I");
				drv.IFOpParamSet("RazonSocial1", "Razon social transportista");
				drv.IFOpParamSet("TipoDocumento", "CUIT");
				drv.IFOpParamSet("NumeroDocumento", "99999999995");
				drv.IFOpParamSet("Domicilio1", "Domicilio transportista");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "3");
				drv.IFOpParamSet("Responsabilidad", "F");
				drv.IFOpParamSet("RazonSocial1", "Nombre Chofer");
				drv.IFOpParamSet("TipoDocumento", "DNI");
				drv.IFOpParamSet("NumeroDocumento", "11222333");
				drv.IFOpParamSet("Domicilio1", "Patente 1");
				drv.IFOpParamSet("Domicilio2", "Patente 2");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("AbrirRemitoR");
				drv.IFOpBegin("AbrirRemitoR");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirRemitoR",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 1");
				drv.IFOpParamFloatSet("Cantidad", 2.0);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 2");
				drv.IFOpParamFloatSet("Cantidad", 3.0);
				drv.IFOpParamSet("CodigoInterno", "1002");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "remitox") // Remito X
			{
				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "0");
				drv.IFOpParamSet("Responsabilidad", "I");
				drv.IFOpParamSet("RazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("TipoDocumento", "CUIT");
				drv.IFOpParamSet("NumeroDocumento", "11111111113");
				drv.IFOpParamSet("Domicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "2");
				drv.IFOpParamSet("Responsabilidad", "I");
				drv.IFOpParamSet("RazonSocial1", "Razon social transportista");
				drv.IFOpParamSet("TipoDocumento", "CUIT");
				drv.IFOpParamSet("NumeroDocumento", "99999999995");
				drv.IFOpParamSet("Domicilio1", "Domicilio transportista");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "3");
				drv.IFOpParamSet("Responsabilidad", "F");
				drv.IFOpParamSet("RazonSocial1", "Nombre Chofer");
				drv.IFOpParamSet("TipoDocumento", "DNI");
				drv.IFOpParamSet("NumeroDocumento", "11222333");
				drv.IFOpParamSet("Domicilio1", "Patente 1");
				drv.IFOpParamSet("Domicilio2", "Patente 2");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("AbrirRemitoX");
				drv.IFOpBegin("AbrirRemitoX");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirRemitoX",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 1");
				drv.IFOpParamFloatSet("Cantidad", 12.345678);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 2");
				drv.IFOpParamSet("CodigoInterno", "1002");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "recibox") // Recibo X
			{
				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "0");
				drv.IFOpParamSet("Responsabilidad", "I");
				drv.IFOpParamSet("RazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("TipoDocumento", "CUIT");
				drv.IFOpParamSet("NumeroDocumento", "11111111113");
				drv.IFOpParamSet("Domicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("AbrirReciboX");
				drv.IFOpBegin("AbrirReciboX");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirReciboX",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción línea 1");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción línea 2");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción línea 3");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción línea 4");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Descripción línea 5");
				drv.IFOpParamFloatSet("Precio", 12.34);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("Pago");
				drv.IFOpBegin("Pago");
				drv.IFOpParamFloatSet("Monto", 50.0);
				drv.IFOpParamIntSet("CodigoTipo", 8);
				if (drv.IFOpSend(1) == 0)
					cmd_error("Pago",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "presupuesto") // Presupuesto
			{
				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "0");
				drv.IFOpParamSet("Responsabilidad", "I");
				drv.IFOpParamSet("RazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("TipoDocumento", "CUIT");
				drv.IFOpParamSet("NumeroDocumento", "11111111113");
				drv.IFOpParamSet("Domicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("AbrirPresupuesto");
				drv.IFOpBegin("AbrirPresupuesto");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirPresupuesto",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 1");
				drv.IFOpParamFloatSet("Precio", 12.34);
				drv.IFOpParamFloatSet("IVA", 21.0);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Item de prueba 2");
				drv.IFOpParamFloatSet("Precio", 5.0);
				drv.IFOpParamFloatSet("IVA", 10.5);
				drv.IFOpParamSet("CodigoInterno", "1002");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("DescuentoGeneral");
				drv.IFOpBegin("DescuentoGeneral");
				drv.IFOpParamSet("Descripcion", "Oferta del día");
				drv.IFOpParamFloatSet("Monto", 2.34);
				if (drv.IFOpSend(1) == 0)
					cmd_error("DescuentoGeneral",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "donacion") // Documento Donación
			{
				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "0");
				drv.IFOpParamSet("Responsabilidad", "I");
				drv.IFOpParamSet("RazonSocial1", "Razon social cliente");
				drv.IFOpParamSet("TipoDocumento", "CUIT");
				drv.IFOpParamSet("NumeroDocumento", "11111111113");
				drv.IFOpParamSet("Domicilio1", "Domicilio cliente");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("DatosTercero");
				drv.IFOpBegin("DatosTercero");
				drv.IFOpParamSet("Tipo", "1");
				drv.IFOpParamSet("Responsabilidad", "I");
				drv.IFOpParamSet("RazonSocial1", "Razon social beneficiario");
				drv.IFOpParamSet("TipoDocumento", "CUIT");
				drv.IFOpParamSet("NumeroDocumento", "99999999995");
				drv.IFOpParamSet("Domicilio1", "Domicilio beneficiario");
				if (drv.IFOpSend(1) == 0)
					cmd_error("DatosTercero",drv);

				Console.WriteLine("AbrirDonacion");
				drv.IFOpBegin("AbrirDonacion");
				drv.IFOpParamSet("Texto", "Descripción línea 1");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirDonacion",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción línea 2");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción línea 3");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("TextoFiscal");
				drv.IFOpBegin("TextoFiscal");
				drv.IFOpParamSet("Texto", "Descripción línea 4");
				if (drv.IFOpSend(1) == 0)
					cmd_error("TextoFiscal",drv);

				Console.WriteLine("ItemVenta");
				drv.IFOpBegin("ItemVenta");
				drv.IFOpParamSet("Descripcion", "Descripción línea 5");
				drv.IFOpParamFloatSet("Precio", 12.34);
				drv.IFOpParamSet("CodigoInterno", "1001");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ItemVenta",drv);

				Console.WriteLine("Pago");
				drv.IFOpBegin("Pago");
				drv.IFOpParamFloatSet("Monto", 50.0);
				drv.IFOpParamIntSet("CodigoTipo", 8);
				if (drv.IFOpSend(1) == 0)
					cmd_error("Pago",drv);
				Console.WriteLine(" MontoFaltaPagar: {0}", drv.IFOpRetFloatGet("MontoFaltaPagar"));

				Console.WriteLine("Cerrar");
				drv.IFOpBegin("Cerrar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cerrar",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CodigoTipo: {0}", drv.IFOpRetGet("CodigoTipo"));
			}
			else if (testname == "tiqueinfo") // Tique de Información del Equipo
			{
				Console.WriteLine("ImprimirInformacion");
				drv.IFOpBegin("ImprimirInformacion");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ImprimirInformacion",drv);
			}
			else if (testname == "printertest") // Prueba Mecanismo Impresor
			{
				Console.WriteLine("ImprimirPruebaImpresora");
				drv.IFOpBegin("ImprimirPruebaImpresora");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ImprimirPruebaImpresora",drv);
			}
			else if (testname == "reimprimir") // Reimpresión Tique 1
			{
				Console.WriteLine("Reimprimir");
				drv.IFOpBegin("Reimprimir");
				drv.IFOpParamIntSet("CodigoTipo", 83);
				drv.IFOpParamIntSet("Numero", 1);
				if (drv.IFOpSend(1) == 0)
					cmd_error("Reimprimir",drv);
			}
			else if (testname == "cancel") // Cancelación
			{
				Console.WriteLine("AbrirTique");
				drv.IFOpBegin("AbrirTique");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirTique",drv);

				Console.WriteLine("Cancelar");
				drv.IFOpBegin("Cancelar");
				if (drv.IFOpSend(1) == 0)
					cmd_error("Cancelar",drv);
			}
			else if (testname == "totalestique") // Obtiene totales de jornada para Tique
			{
				Console.WriteLine("Contadores");
				drv.IFOpBegin("Contadores");
				drv.IFOpParamIntSet("CodigoTipo", 83);
				if (drv.IFOpSend(1) == 0)
					cmd_error("Contadores",drv);
				Console.WriteLine(" NumeroUltimoZ: {0}", drv.IFOpRetIntGet("NumeroUltimoZ"));
				Console.WriteLine(" NumeroUltimoCambioFechaHora: {0}", drv.IFOpRetIntGet("NumeroUltimoCambioFechaHora"));
				Console.WriteLine(" NumeroUltimoInformeAuditoria: {0}", drv.IFOpRetIntGet("NumeroUltimoInformeAuditoria"));
				Console.WriteLine(" NumeroUltimoDocumento: {0}", drv.IFOpRetIntGet("NumeroUltimoDocumento"));

				Console.WriteLine("TotalesJornada");
				drv.IFOpBegin("TotalesJornada");
				drv.IFOpParamIntSet("CodigoTipo", 83);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TotalesJornada",drv);
				Console.WriteLine(" FechaAperturaJornada: {0}", drv.IFOpRetGet("FechaAperturaJornada"));
				Console.WriteLine(" HoraAperturaJornada: {0}", drv.IFOpRetGet("HoraAperturaJornada"));
				Console.WriteLine(" NumeroUltimoZ: {0}", drv.IFOpRetIntGet("NumeroUltimoZ"));
				Console.WriteLine(" NecesitaZ: {0}", (drv.IFOpRetBoolGet("NecesitaZ")!=0) ? "Si" : "No");
				Console.WriteLine(" CantidadEmitidos: {0}", drv.IFOpRetIntGet("CantidadEmitidos"));
				Console.WriteLine(" CantidadCancelados: {0}", drv.IFOpRetIntGet("CantidadCancelados"));
				Console.WriteLine(" Total: {0}", drv.IFOpRetFloatGet("Total"));
				Console.WriteLine(" TotalIva: {0}", drv.IFOpRetFloatGet("TotalIva"));
				Console.WriteLine(" TotalImpIntFijo: {0}", drv.IFOpRetFloatGet("TotalImpIntFijo"));
				Console.WriteLine(" TotalImpIntPorc: {0}", drv.IFOpRetFloatGet("TotalImpIntPorc"));
				Console.WriteLine(" TotalOtroTributo: {0}", drv.IFOpRetFloatGet("TotalOtroTributo"));

				Console.WriteLine("TotalesJornadaIva");
				drv.IFOpBegin("TotalesJornadaIva");
				drv.IFOpParamIntSet("CodigoTipo", 83);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TotalesJornadaIva",drv);
				Console.WriteLine(" TotalIva: {0}", drv.IFOpRetFloatGet("TotalIva"));
				Console.WriteLine(" TasaIva1: {0}", drv.IFOpRetFloatGet("TasaIva1"));
				Console.WriteLine(" TotalIva1: {0}", drv.IFOpRetFloatGet("TotalIva1"));
				Console.WriteLine(" TotalVentaIva1: {0}", drv.IFOpRetFloatGet("TotalVentaIva1"));
				Console.WriteLine(" TotalImpIntFijoIva1: {0}", drv.IFOpRetFloatGet("TotalImpIntFijoIva1"));
				Console.WriteLine(" TotalImpIntPorcIva1: {0}", drv.IFOpRetFloatGet("TotalImpIntPorcIva1"));
				Console.WriteLine(" TasaIva2: {0}", drv.IFOpRetFloatGet("TasaIva2"));
				Console.WriteLine(" TotalIva2: {0}", drv.IFOpRetFloatGet("TotalIva2"));
				Console.WriteLine(" TotalVentaIva2: {0}", drv.IFOpRetFloatGet("TotalVentaIva2"));
				Console.WriteLine(" TotalImpIntFijoIva2: {0}", drv.IFOpRetFloatGet("TotalImpIntFijoIva2"));
				Console.WriteLine(" TotalImpIntPorcIva2: {0}", drv.IFOpRetFloatGet("TotalImpIntPorcIva2"));
				Console.WriteLine(" TasaIva3: {0}", drv.IFOpRetFloatGet("TasaIva3"));
				Console.WriteLine(" TotalIva3: {0}", drv.IFOpRetFloatGet("TotalIva3"));
				Console.WriteLine(" TotalVentaIva3: {0}", drv.IFOpRetFloatGet("TotalVentaIva3"));
				Console.WriteLine(" TotalImpIntFijoIva3: {0}", drv.IFOpRetFloatGet("TotalImpIntFijoIva3"));
				Console.WriteLine(" TotalImpIntPorcIva3: {0}", drv.IFOpRetFloatGet("TotalImpIntPorcIva3"));
				Console.WriteLine(" TasaIva4: {0}", drv.IFOpRetFloatGet("TasaIva4"));
				Console.WriteLine(" TotalIva4: {0}", drv.IFOpRetFloatGet("TotalIva4"));
				Console.WriteLine(" TotalVentaIva4: {0}", drv.IFOpRetFloatGet("TotalVentaIva4"));
				Console.WriteLine(" TotalImpIntFijoIva4: {0}", drv.IFOpRetFloatGet("TotalImpIntFijoIva4"));
				Console.WriteLine(" TotalImpIntPorcIva4: {0}", drv.IFOpRetFloatGet("TotalImpIntPorcIva4"));
				Console.WriteLine(" TasaIva5: {0}", drv.IFOpRetFloatGet("TasaIva5"));
				Console.WriteLine(" TotalIva5: {0}", drv.IFOpRetFloatGet("TotalIva5"));
				Console.WriteLine(" TotalVentaIva5: {0}", drv.IFOpRetFloatGet("TotalVentaIva5"));
				Console.WriteLine(" TotalImpIntFijoIva5: {0}", drv.IFOpRetFloatGet("TotalImpIntFijoIva5"));
				Console.WriteLine(" TotalImpIntPorcIva5: {0}", drv.IFOpRetFloatGet("TotalImpIntPorcIva5"));
				Console.WriteLine(" TasaIva6: {0}", drv.IFOpRetFloatGet("TasaIva6"));
				Console.WriteLine(" TotalIva6: {0}", drv.IFOpRetFloatGet("TotalIva6"));
				Console.WriteLine(" TotalVentaIva6: {0}", drv.IFOpRetFloatGet("TotalVentaIva6"));
				Console.WriteLine(" TotalImpIntFijoIva6: {0}", drv.IFOpRetFloatGet("TotalImpIntFijoIva6"));
				Console.WriteLine(" TotalImpIntPorcIva6: {0}", drv.IFOpRetFloatGet("TotalImpIntPorcIva6"));

				Console.WriteLine("TotalesJornadaOtroTributo");
				drv.IFOpBegin("TotalesJornadaOtroTributo");
				drv.IFOpParamIntSet("CodigoTipo", 83);
				drv.IFOpParamIntSet("IndiceOtroTributo", 1);
				if (drv.IFOpSend(1) == 0)
					cmd_error("TotalesJornadaOtroTributo",drv);
				Console.WriteLine(" TotalOtroTributoGeneral: {0}", drv.IFOpRetFloatGet("TotalOtroTributoGeneral"));
				Console.WriteLine(" TotalOtroTributo07: {0}", drv.IFOpRetFloatGet("TotalOtroTributo07"));
				Console.WriteLine(" TotalOtroTributo06: {0}", drv.IFOpRetFloatGet("TotalOtroTributo06"));
				Console.WriteLine(" TotalOtroTributo09: {0}", drv.IFOpRetFloatGet("TotalOtroTributo09"));
				Console.WriteLine(" CantidadEnJornada: {0}", drv.IFOpRetIntGet("CantidadEnJornada"));
				Console.WriteLine(" TotalOtroTributo: {0}", drv.IFOpRetFloatGet("TotalOtroTributo"));
				Console.WriteLine(" CodigoOtroTributo: {0}", drv.IFOpRetIntGet("CodigoOtroTributo"));
			}
			else if (testname == "config") // Configuración
			{
				Console.WriteLine("EstablecerOpcion");
				drv.IFOpBegin("EstablecerOpcion");
				drv.IFOpParamIntSet("Numero", 242);
				drv.IFOpParamIntSet("Valor", 1);
				if (drv.IFOpSend(1) == 0)
					cmd_error("EstablecerOpcion",drv);

				Console.WriteLine("Opcion");
				drv.IFOpBegin("Opcion");
				drv.IFOpParamIntSet("Numero", 242);
				if (drv.IFOpSend(1) == 0)
					cmd_error("Opcion",drv);
				Console.WriteLine(" Valor: {0}", drv.IFOpRetGet("Valor"));

				Console.WriteLine("EstablecerEncabezadoCola");
				drv.IFOpBegin("EstablecerEncabezadoCola");
				drv.IFOpParamIntSet("Numero", 79);
				drv.IFOpParamSet("Texto", "Encabezado libre 9");
				if (drv.IFOpSend(1) == 0)
					cmd_error("EstablecerEncabezadoCola",drv);

				Console.WriteLine("EncabezadoCola");
				drv.IFOpBegin("EncabezadoCola");
				drv.IFOpParamIntSet("Numero", 79);
				if (drv.IFOpSend(1) == 0)
					cmd_error("EncabezadoCola",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetIntGet("Numero"));
				Console.WriteLine(" Texto: {0}", drv.IFOpRetGet("Texto"));

				Console.WriteLine("EstablecerEncabezadoCola");
				drv.IFOpBegin("EstablecerEncabezadoCola");
				drv.IFOpParamIntSet("Numero", 19);
				drv.IFOpParamSet("Texto", "Cola libre 9");
				if (drv.IFOpSend(1) == 0)
					cmd_error("EstablecerEncabezadoCola",drv);

				Console.WriteLine("EncabezadoCola");
				drv.IFOpBegin("EncabezadoCola");
				drv.IFOpParamIntSet("Numero", 19);
				if (drv.IFOpSend(1) == 0)
					cmd_error("EncabezadoCola",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetIntGet("Numero"));
				Console.WriteLine(" Texto: {0}", drv.IFOpRetGet("Texto"));
			}
			else if (testname == "x") // Informe X
			{
				Console.WriteLine("InformeXNoImpreso");
				drv.IFOpBegin("InformeXNoImpreso");
				if (drv.IFOpSend(1) == 0)
					cmd_error("InformeXNoImpreso",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CantidadDocFiscalCancel: {0}", drv.IFOpRetGet("CantidadDocFiscalCancel"));
				Console.WriteLine(" CantidadDocNoFiscal: {0}", drv.IFOpRetGet("CantidadDocNoFiscal"));
				Console.WriteLine(" CantidadDocGenerico: {0}", drv.IFOpRetGet("CantidadDocGenerico"));
				Console.WriteLine(" CantidadTique: {0}", drv.IFOpRetGet("CantidadTique"));
				Console.WriteLine(" CantidadFacturaA: {0}", drv.IFOpRetGet("CantidadFacturaA"));
				Console.WriteLine(" NumeroUltimoTique: {0}", drv.IFOpRetGet("NumeroUltimoTique"));
				Console.WriteLine(" MontoVenta: {0}", drv.IFOpRetFloatGet("MontoVenta"));
				Console.WriteLine(" MontoIVAVenta: {0}", drv.IFOpRetFloatGet("MontoIVAVenta"));
				Console.WriteLine(" MontoOtrosTributosVenta: {0}", drv.IFOpRetFloatGet("MontoOtrosTributosVenta"));
				Console.WriteLine(" NumeroFacturaA: {0}", drv.IFOpRetGet("NumeroFacturaA"));
				Console.WriteLine(" NumeroCreditoA: {0}", drv.IFOpRetGet("NumeroCreditoA"));
				Console.WriteLine(" NumeroCreditoB: {0}", drv.IFOpRetGet("NumeroCreditoB"));
				Console.WriteLine(" MontoCredito: {0}", drv.IFOpRetFloatGet("MontoCredito"));
				Console.WriteLine(" MontoIVACredito: {0}", drv.IFOpRetFloatGet("MontoIVACredito"));
				Console.WriteLine(" MontoOtrosTributosCredito: {0}", drv.IFOpRetFloatGet("MontoOtrosTributosCredito"));

				Console.WriteLine("InformeXResumido");
				drv.IFOpBegin("InformeXResumido");
				if (drv.IFOpSend(1) == 0)
					cmd_error("InformeXResumido",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CantidadDocFiscalCancel: {0}", drv.IFOpRetGet("CantidadDocFiscalCancel"));
				Console.WriteLine(" CantidadDocNoFiscal: {0}", drv.IFOpRetGet("CantidadDocNoFiscal"));
				Console.WriteLine(" CantidadDocGenerico: {0}", drv.IFOpRetGet("CantidadDocGenerico"));
				Console.WriteLine(" CantidadTique: {0}", drv.IFOpRetGet("CantidadTique"));
				Console.WriteLine(" CantidadFacturaA: {0}", drv.IFOpRetGet("CantidadFacturaA"));
				Console.WriteLine(" NumeroUltimoTique: {0}", drv.IFOpRetGet("NumeroUltimoTique"));
				Console.WriteLine(" MontoVenta: {0}", drv.IFOpRetFloatGet("MontoVenta"));
				Console.WriteLine(" MontoIVAVenta: {0}", drv.IFOpRetFloatGet("MontoIVAVenta"));
				Console.WriteLine(" MontoOtrosTributosVenta: {0}", drv.IFOpRetFloatGet("MontoOtrosTributosVenta"));
				Console.WriteLine(" NumeroFacturaA: {0}", drv.IFOpRetGet("NumeroFacturaA"));
				Console.WriteLine(" NumeroCreditoA: {0}", drv.IFOpRetGet("NumeroCreditoA"));
				Console.WriteLine(" NumeroCreditoB: {0}", drv.IFOpRetGet("NumeroCreditoB"));
				Console.WriteLine(" MontoCredito: {0}", drv.IFOpRetFloatGet("MontoCredito"));
				Console.WriteLine(" MontoIVACredito: {0}", drv.IFOpRetFloatGet("MontoIVACredito"));
				Console.WriteLine(" MontoOtrosTributosCredito: {0}", drv.IFOpRetFloatGet("MontoOtrosTributosCredito"));

				Console.WriteLine("InformeXDetallado");
				drv.IFOpBegin("InformeXDetallado");
				if (drv.IFOpSend(1) == 0)
					cmd_error("InformeXDetallado",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CantidadDocFiscalCancel: {0}", drv.IFOpRetGet("CantidadDocFiscalCancel"));
				Console.WriteLine(" CantidadDocNoFiscal: {0}", drv.IFOpRetGet("CantidadDocNoFiscal"));
				Console.WriteLine(" CantidadDocGenerico: {0}", drv.IFOpRetGet("CantidadDocGenerico"));
				Console.WriteLine(" CantidadTique: {0}", drv.IFOpRetGet("CantidadTique"));
				Console.WriteLine(" CantidadFacturaA: {0}", drv.IFOpRetGet("CantidadFacturaA"));
				Console.WriteLine(" NumeroUltimoTique: {0}", drv.IFOpRetGet("NumeroUltimoTique"));
				Console.WriteLine(" MontoVenta: {0}", drv.IFOpRetFloatGet("MontoVenta"));
				Console.WriteLine(" MontoIVAVenta: {0}", drv.IFOpRetFloatGet("MontoIVAVenta"));
				Console.WriteLine(" MontoOtrosTributosVenta: {0}", drv.IFOpRetFloatGet("MontoOtrosTributosVenta"));
				Console.WriteLine(" NumeroFacturaA: {0}", drv.IFOpRetGet("NumeroFacturaA"));
				Console.WriteLine(" NumeroCreditoA: {0}", drv.IFOpRetGet("NumeroCreditoA"));
				Console.WriteLine(" NumeroCreditoB: {0}", drv.IFOpRetGet("NumeroCreditoB"));
				Console.WriteLine(" MontoCredito: {0}", drv.IFOpRetFloatGet("MontoCredito"));
				Console.WriteLine(" MontoIVACredito: {0}", drv.IFOpRetFloatGet("MontoIVACredito"));
				Console.WriteLine(" MontoOtrosTributosCredito: {0}", drv.IFOpRetFloatGet("MontoOtrosTributosCredito"));
			}
			else if (testname == "z") // Cierre Z
			{
				Console.WriteLine("CierreZ");
				drv.IFOpBegin("CierreZ");
				if (drv.IFOpSend(1) == 0)
					cmd_error("CierreZ",drv);
				Console.WriteLine(" Numero: {0}", drv.IFOpRetGet("Numero"));
				Console.WriteLine(" CantidadDocFiscalCancel: {0}", drv.IFOpRetGet("CantidadDocFiscalCancel"));
				Console.WriteLine(" CantidadDocNoFiscal: {0}", drv.IFOpRetGet("CantidadDocNoFiscal"));
				Console.WriteLine(" CantidadDocGenerico: {0}", drv.IFOpRetGet("CantidadDocGenerico"));
				Console.WriteLine(" CantidadTique: {0}", drv.IFOpRetGet("CantidadTique"));
				Console.WriteLine(" CantidadFacturaA: {0}", drv.IFOpRetGet("CantidadFacturaA"));
				Console.WriteLine(" NumeroUltimoTique: {0}", drv.IFOpRetGet("NumeroUltimoTique"));
				Console.WriteLine(" MontoVenta: {0}", drv.IFOpRetFloatGet("MontoVenta"));
				Console.WriteLine(" MontoIVAVenta: {0}", drv.IFOpRetFloatGet("MontoIVAVenta"));
				Console.WriteLine(" MontoOtrosTributosVenta: {0}", drv.IFOpRetFloatGet("MontoOtrosTributosVenta"));
				Console.WriteLine(" NumeroFacturaA: {0}", drv.IFOpRetGet("NumeroFacturaA"));
				Console.WriteLine(" NumeroCreditoA: {0}", drv.IFOpRetGet("NumeroCreditoA"));
				Console.WriteLine(" NumeroCreditoB: {0}", drv.IFOpRetGet("NumeroCreditoB"));
				Console.WriteLine(" MontoCredito: {0}", drv.IFOpRetFloatGet("MontoCredito"));
				Console.WriteLine(" MontoIVACredito: {0}", drv.IFOpRetFloatGet("MontoIVACredito"));
				Console.WriteLine(" MontoOtrosTributosCredito: {0}", drv.IFOpRetFloatGet("MontoOtrosTributosCredito"));
			}
			else if (testname == "auditoria") // Informe de Auditoría resumido
			{
				Console.WriteLine("ImprimirAuditoriaResumidaPorZ");
				drv.IFOpBegin("ImprimirAuditoriaResumidaPorZ");
				drv.IFOpParamSet("ZInicial", "1");
				drv.IFOpParamSet("ZFinal", "9999");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ImprimirAuditoriaResumidaPorZ",drv);
			}
			else if (testname == "misc") // Miscelaneos
			{
				Console.WriteLine("AbrirCajon");
				drv.IFOpBegin("AbrirCajon");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirCajon",drv);

				Console.WriteLine("AvanzarPapel");
				drv.IFOpBegin("AvanzarPapel");
				drv.IFOpParamSet("Lineas", "5");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AvanzarPapel",drv);

				Console.WriteLine("CortarPapel");
				drv.IFOpBegin("CortarPapel");
				if (drv.IFOpSend(1) == 0)
					cmd_error("CortarPapel",drv);

				Console.WriteLine("AbrirCajon2");
				drv.IFOpBegin("AbrirCajon2");
				if (drv.IFOpSend(1) == 0)
					cmd_error("AbrirCajon2",drv);
			}
			else if (testname == "eventlog") // Descarga log de eventos
			{
				Console.WriteLine("ComenzarDescargaEventLog");
				drv.IFOpBegin("ComenzarDescargaEventLog");
				if (drv.IFOpSend(1) == 0)
					cmd_error("ComenzarDescargaEventLog",drv);

				StreamWriter fout = new StreamWriter("eventlog.txt");
				int bloop = 1;
				String data;
				while (bloop!=0)
				{
					Console.WriteLine("DescargarBloque");
					drv.IFOpBegin("DescargarBloque");
					if (drv.IFOpSend(1) == 0)
						cmd_error("DescargarBloque",drv);
					data = drv.IFOpRetGet("Datos");
					fout.Write(data);
					//Console.WriteLine(" Datos: {0}", data);
					bloop = drv.IFOpRetBoolGet("Continuar");
					Console.WriteLine(" Continuar: {0}", (bloop!=0) ? "Si" : "No");
				}
				fout.Close();
			}
			else if (testname == "rptpend") // Descarga reportes ya generados y no descargados
			{
				while (true)
				{
					Console.WriteLine("DescargasPendientes");
					drv.IFOpBegin("DescargasPendientes");
					if (drv.IFOpSend(1) == 0)
						cmd_error("DescargasPendientes",drv);
					int npend = drv.IFOpRetIntGet("CantidadGeneracionesNoDescargadas");
					Console.WriteLine(" CantidadGeneracionesNoDescargadas: {0}", npend);
					int ipend = drv.IFOpRetIntGet("PrimerGeneracionNoDescargada");
					Console.WriteLine(" PrimerGeneracionNoDescargada: {0}", ipend);

					if (ipend == 0)
						break;

					for (int rpttype=1; rpttype<=3; rpttype++)
					{
						Console.WriteLine("ComenzarDescargaReporte");
						drv.IFOpBegin("ComenzarDescargaReporte");
						drv.IFOpParamIntSet("TipoReporte", rpttype);
						drv.IFOpParamIntSet("NumeroGeneracion", ipend);
						if (drv.IFOpSend(1) == 0)
							cmd_error("ComenzarDescargaReporte",drv);
						String filename = drv.IFOpRetGet("NombreArchivo");
						Console.WriteLine(" NombreArchivo: {0}", filename);

						StreamWriter fout = new StreamWriter(filename);
						int bloop = 1;
						String data;
						while (bloop!=0)
						{
							Console.WriteLine("DescargarBloque");
							drv.IFOpBegin("DescargarBloque");
							if (drv.IFOpSend(1) == 0)
								cmd_error("DescargarBloque",drv);
							data = drv.IFOpRetGet("Datos");
							fout.Write(data);
							//Console.WriteLine(" Datos: {0}", data);
							bloop = drv.IFOpRetBoolGet("Continuar");
							//Console.WriteLine(" Continuar: {0}", (bloop!=0) ? "Si" : "No");
						}
						fout.Close();
					}
				}
			}
			else if (testname == "rptzdown") // Genera y descarga reportes por rango de Z
			{
				Console.WriteLine("GenerarReportesPorZ desde {0} hasta {1}", extra1, extra2);
				drv.IFOpBegin("GenerarReportesPorZ");
				drv.IFOpParamSet("ZInicial", extra1);
				drv.IFOpParamSet("ZFinal", extra2);
				if (drv.IFOpSend(1) == 0)
					cmd_error("GenerarReportesPorZ",drv);
				Console.WriteLine(" NumeroGeneracion: {0}", drv.IFOpRetGet("NumeroGeneracion"));

				for (int rpttype=1; rpttype<=3; rpttype++)
				{
					Console.WriteLine("ComenzarDescargaReporte");
					drv.IFOpBegin("ComenzarDescargaReporte");
					drv.IFOpParamIntSet("TipoReporte", rpttype);
					if (drv.IFOpSend(1) == 0)
						cmd_error("ComenzarDescargaReporte",drv);
					String filename = drv.IFOpRetGet("NombreArchivo");
					Console.WriteLine(" NombreArchivo: {0}", filename);

					StreamWriter fout = new StreamWriter(filename);
					int bloop = 1;
					String data;
					while (bloop!=0)
					{
						Console.WriteLine("DescargarBloque");
						drv.IFOpBegin("DescargarBloque");
						if (drv.IFOpSend(1) == 0)
							cmd_error("DescargarBloque",drv);
						data = drv.IFOpRetGet("Datos");
						fout.Write(data);
						//Console.WriteLine(" Datos: {0}", data);
						bloop = drv.IFOpRetBoolGet("Continuar");
						//Console.WriteLine(" Continuar: {0}", (bloop!=0) ? "Si" : "No");
					}
					fout.Close();
				}
			}
			else if (testname == "docdown") // Descarga xml de un documento emitido
			{
				Console.WriteLine("ComenzarDescargaDocumento {0} {1}", extra1, extra2);
				drv.IFOpBegin("ComenzarDescargaDocumento");
				drv.IFOpParamSet("CodigoTipo", extra1);
				drv.IFOpParamSet("Numero", extra2);
				if (drv.IFOpSend(1) == 0)
					cmd_error("ComenzarDescargaDocumento",drv);

				StreamWriter fout = new StreamWriter("doc.xml");
				int bloop = 1;
				String data;
				while (bloop!=0)
				{
					Console.WriteLine("DescargarBloque");
					drv.IFOpBegin("DescargarBloque");
					if (drv.IFOpSend(1) == 0)
						cmd_error("DescargarBloque",drv);
					data = drv.IFOpRetGet("Datos");
					fout.Write(data);
					//Console.WriteLine(" Datos: {0}", data);
					bloop = drv.IFOpRetBoolGet("Continuar");
					Console.WriteLine(" Continuar: {0}", (bloop!=0) ? "Si" : "No");
				}
				fout.Close();
			}

			else
			{
				Console.WriteLine("Error: prueba desconocida: {0}", testname);
				return 3;
			}

			return 0;
        }
    }
}
