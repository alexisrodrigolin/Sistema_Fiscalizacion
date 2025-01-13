/*
	Ejemplo de uso de Sam4sFiscalDriver.dll
	Para Windows
	2019-04-03
*/

#include <Windows.h>
#include <stdio.h>
#include <tchar.h>

/*
	Punteros a las funciones de la DLL cargada dinámicamente
*/
typedef int (WINAPI *LPSERIALPORTOPEN) (int);
typedef int (WINAPI *LPSERIALBAUDSET) (int);
typedef int (WINAPI *LPSERIALPORTCLOSE) ();
typedef int (WINAPI *LPIFOPBEGIN) (const char *);
typedef int (WINAPI *LPIFOPSEND) (int);
typedef int (WINAPI *LPIFOPWAITINGIS) ();
typedef int (WINAPI *LPIFOPABORT) ();
typedef int (WINAPI *LPIFOPPARAMSET) (const char *, const char *);
typedef const char * (WINAPI *LPIFOPPARAMGET) (const char *);
typedef int (WINAPI *LPIFOPPARAMINTSET) (const char *, int);
typedef int (WINAPI *LPIFOPPARAMINTGET) (const char *);
typedef int (WINAPI *LPIFOPPARAMFLOATSET) (const char *, double);
typedef double (WINAPI *LPIFOPPARAMFLOATGET) (const char *);
typedef int (WINAPI *LPIFOPPARAMBOOLSET) (const char *, int);
typedef int (WINAPI *LPIFOPPARAMBOOLGET) (const char *);
typedef int (WINAPI *LPIFOPCMDOKIS) ();
typedef int (WINAPI *LPIFOPERRORGET) ();
typedef const char * (WINAPI *LPIFOPERRORDESCGET) ();
typedef int (WINAPI *LPIFOPSTATEGET) (const char *);
typedef const char * (WINAPI *LPIFOPRETGET) (const char *);
typedef int (WINAPI *LPIFOPRETINTGET) (const char *);
typedef double (WINAPI *LPIFOPRETFLOATGET) (const char *);
typedef int (WINAPI *LPIFOPRETBOOLGET) (const char *);
typedef const char * (WINAPI *LPIFOPLISTGET) (int);
typedef const char * (WINAPI *LPIFOPPARAMLISTGET) (int);
typedef const char * (WINAPI *LPIFOPRETLISTGET) (int);
typedef const char * (WINAPI *LPIFOPSTATELISTGET) (int);

LPSERIALPORTOPEN SerialPortOpen;
LPSERIALBAUDSET SerialBaudSet;
LPSERIALPORTCLOSE SerialPortClose;
LPIFOPBEGIN IFOpBegin;
LPIFOPSEND IFOpSend;
LPIFOPWAITINGIS IFOpWaitingIs;
LPIFOPABORT IFOpAbort;
LPIFOPPARAMSET IFOpParamSet;
LPIFOPPARAMGET IFOpParamGet;
LPIFOPPARAMINTSET IFOpParamIntSet;
LPIFOPPARAMINTGET IFOpParamIntGet;
LPIFOPPARAMFLOATSET IFOpParamFloatSet;
LPIFOPPARAMFLOATGET IFOpParamFloatGet;
LPIFOPPARAMBOOLSET IFOpParamBoolSet;
LPIFOPPARAMBOOLGET IFOpParamBoolGet;
LPIFOPCMDOKIS IFOpCmdOkIs;
LPIFOPERRORGET IFOpErrorGet;
LPIFOPERRORDESCGET IFOpErrorDescGet;
LPIFOPSTATEGET IFOpStateGet;
LPIFOPRETGET IFOpRetGet;
LPIFOPRETINTGET IFOpRetIntGet;
LPIFOPRETFLOATGET IFOpRetFloatGet;
LPIFOPRETBOOLGET IFOpRetBoolGet;
LPIFOPLISTGET IFOpListGet;
LPIFOPPARAMLISTGET IFOpParamListGet;
LPIFOPRETLISTGET IFOpRetListGet;
LPIFOPSTATELISTGET IFOpStateListGet;

/*
	Carga la DLL en forma dinámica
*/
int driver_load ()
{
	HINSTANCE hlib;

	hlib = (HINSTANCE)LoadLibrary(_T("Sam4sFiscalDriver.dll"));
	if (!hlib)
	{
		printf("Error cargando Sam4sFiscalDriver.dll\n");
		return 0;
	}

	SerialPortOpen = (LPSERIALPORTOPEN) GetProcAddress(hlib, "SerialPortOpen");
	SerialBaudSet = (LPSERIALBAUDSET) GetProcAddress(hlib, "SerialBaudSet");
	SerialPortClose = (LPSERIALPORTCLOSE) GetProcAddress(hlib, "SerialPortClose");
	IFOpBegin = (LPIFOPBEGIN) GetProcAddress(hlib, "IFOpBegin");
	IFOpSend = (LPIFOPSEND) GetProcAddress(hlib, "IFOpSend");
	IFOpWaitingIs = (LPIFOPWAITINGIS) GetProcAddress(hlib, "IFOpWaitingIs");
	IFOpAbort = (LPIFOPABORT) GetProcAddress(hlib, "IFOpAbort");
	IFOpParamSet = (LPIFOPPARAMSET) GetProcAddress(hlib, "IFOpParamSet");
	IFOpParamGet = (LPIFOPPARAMGET) GetProcAddress(hlib, "IFOpParamGet");
	IFOpParamIntSet = (LPIFOPPARAMINTSET) GetProcAddress(hlib, "IFOpParamIntSet");
	IFOpParamIntGet = (LPIFOPPARAMINTGET) GetProcAddress(hlib, "IFOpParamIntGet");
	IFOpParamFloatSet = (LPIFOPPARAMFLOATSET) GetProcAddress(hlib, "IFOpParamFloatSet");
	IFOpParamFloatGet = (LPIFOPPARAMFLOATGET) GetProcAddress(hlib, "IFOpParamFloatGet");
	IFOpParamBoolSet = (LPIFOPPARAMBOOLSET) GetProcAddress(hlib, "IFOpParamBoolSet");
	IFOpParamBoolGet = (LPIFOPPARAMBOOLGET) GetProcAddress(hlib, "IFOpParamBoolGet");
	IFOpCmdOkIs = (LPIFOPCMDOKIS) GetProcAddress(hlib, "IFOpCmdOkIs");
	IFOpErrorGet = (LPIFOPERRORGET) GetProcAddress(hlib, "IFOpErrorGet");
	IFOpErrorDescGet = (LPIFOPERRORDESCGET) GetProcAddress(hlib, "IFOpErrorDescGet");
	IFOpStateGet = (LPIFOPSTATEGET) GetProcAddress(hlib, "IFOpStateGet");
	IFOpRetGet = (LPIFOPRETGET) GetProcAddress(hlib, "IFOpRetGet");
	IFOpRetIntGet = (LPIFOPRETINTGET) GetProcAddress(hlib, "IFOpRetIntGet");
	IFOpRetFloatGet = (LPIFOPRETFLOATGET) GetProcAddress(hlib, "IFOpRetFloatGet");
	IFOpRetBoolGet = (LPIFOPRETBOOLGET) GetProcAddress(hlib, "IFOpRetBoolGet");
	IFOpListGet = (LPIFOPLISTGET) GetProcAddress(hlib, "IFOpListGet");
	IFOpParamListGet = (LPIFOPPARAMLISTGET) GetProcAddress(hlib, "IFOpParamListGet");
	IFOpRetListGet = (LPIFOPRETLISTGET) GetProcAddress(hlib, "IFOpRetListGet");
	IFOpStateListGet = (LPIFOPSTATELISTGET) GetProcAddress(hlib, "IFOpStateListGet");

	if (!SerialPortOpen
		|| !SerialBaudSet
		|| !SerialPortClose
		|| !IFOpBegin
		|| !IFOpSend
		|| !IFOpWaitingIs
		|| !IFOpAbort
		|| !IFOpParamSet
		|| !IFOpParamGet
		|| !IFOpParamIntSet
		|| !IFOpParamIntGet
		|| !IFOpParamFloatSet
		|| !IFOpParamFloatGet
		|| !IFOpParamBoolSet
		|| !IFOpParamBoolGet
		|| !IFOpCmdOkIs
		|| !IFOpErrorGet
		|| !IFOpErrorDescGet
		|| !IFOpStateGet
		|| !IFOpRetGet
		|| !IFOpRetIntGet
		|| !IFOpRetFloatGet
		|| !IFOpRetBoolGet
		|| !IFOpListGet
		|| !IFOpParamListGet
		|| !IFOpRetListGet
		|| !IFOpStateListGet)
	{
		printf("Error cargando funciones de Sam4sFiscalDriver.dll\n");
		return 0;
	}
	
	return 1;
}

/*
	Manejo error en comando
*/
void cmd_error (const char * cmdname)
{
	printf("Error %d en comando %s: %s\n",
		IFOpErrorGet(), cmdname, IFOpErrorDescGet());
	exit(1);
}

/*
	Programa de prueba
*/
int main (int argc, char* argv[])
{
	int comnum, baudrate;
	const char *testname, *extra1, *extra2;
	
	if (argc < 3)
	{
		printf("Error: insuficientes parámetros\n");
		printf("Uso: %s [numero_puerto] [baudios] [prueba]\n", argv[0]);
		printf("Pruebas: info tique tnc factura credito debito recibo generico interno voucher remitor remitox recibox presupuesto donacion tiqueinfo printertest reimprimir cancel totalestique config x z auditoria misc eventlog rptpend rptzdown\n");
		exit(1);
	}
	comnum = atoi(argv[1]);
	baudrate = atoi(argv[2]);
	testname = argv[3];
	extra1 = (argc > 4) ? argv[4] : "";
	extra2 = (argc > 5) ? argv[5] : "";
	
	if (!driver_load())
	{
		printf("Error: no se puede cargar la DLL\n");
		return 3;
	}
	
	if (!SerialBaudSet(baudrate))
	{
		printf("Error: no se pudo configurar la velocidad %d\n", baudrate);
		return 2;
	}
	
	if (!SerialPortOpen(comnum))
	{
		printf("Error: no se puede abrir el puerto serial %d\n", comnum);
		return 2;
	}
	
	IFOpBegin("DocumentoEnCurso");
	if (!IFOpSend(1))
		cmd_error("DocumentoEnCurso");
	if (IFOpRetIntGet("CodigoTipo"))
		IFOpBegin("Cancelar");
		if (!IFOpSend(1))
			cmd_error("Cancelar");
	
	if (_stricmp(testname,"info") == 0) /* Información del equipo */
	{
		printf("Estado\n");
		IFOpBegin("Estado");
		if (!IFOpSend(1))
			cmd_error("Estado");
		printf(" FechaAperturaJornada: %s\n", IFOpRetGet("FechaAperturaJornada"));
		printf(" HoraAperturaJornada: %s\n", IFOpRetGet("HoraAperturaJornada"));
		printf(" NumeroUltimoZ: %d\n", IFOpRetIntGet("NumeroUltimoZ"));
		printf(" NumeroRegistro: %s\n", IFOpRetGet("NumeroRegistro"));
		printf(" Version: %s\n", IFOpRetGet("Version"));

		printf("CaracteristicasEquipo\n");
		IFOpBegin("CaracteristicasEquipo");
		if (!IFOpSend(1))
			cmd_error("CaracteristicasEquipo");
		printf(" AnchoTique: %d\n", IFOpRetIntGet("AnchoTique"));
		printf(" EmiteTiqueFiscal: %s\n", IFOpRetBoolGet("EmiteTiqueFiscal") ? "Si" : "No");
		printf(" EmiteTiqueFactura: %s\n", IFOpRetBoolGet("EmiteTiqueFactura") ? "Si" : "No");
		printf(" EmiteFactura: %s\n", IFOpRetBoolGet("EmiteFactura") ? "Si" : "No");
		printf(" DigitosDecimales: %d\n", IFOpRetIntGet("DigitosDecimales"));
		printf(" ModeloVersion: %s\n", IFOpRetGet("ModeloVersion"));

		printf("DatosContribuyente\n");
		IFOpBegin("DatosContribuyente");
		if (!IFOpSend(1))
			cmd_error("DatosContribuyente");
		printf(" CUIT: %s\n", IFOpRetGet("CUIT"));
		printf(" PV: %s\n", IFOpRetGet("PV"));
		printf(" ResponsabilidadIVA: %s\n", IFOpRetGet("ResponsabilidadIVA"));
		printf(" IVAEstandar: %f\n", IFOpRetFloatGet("IVAEstandar"));
		printf(" MaximoTiqueFactura: %f\n", IFOpRetFloatGet("MaximoTiqueFactura"));
		printf(" MaximoTique: %f\n", IFOpRetFloatGet("MaximoTique"));
		printf(" RazonSocial: %s\n", IFOpRetGet("RazonSocial"));
		printf(" TipoHabilitacion: %s\n", IFOpRetGet("TipoHabilitacion"));
		printf(" IngresosBrutos: %s\n", IFOpRetGet("IngresosBrutos"));
		printf(" InicioActividades: %s\n", IFOpRetGet("InicioActividades"));

		printf("DocumentoEnCurso\n");
		IFOpBegin("DocumentoEnCurso");
		if (!IFOpSend(1))
			cmd_error("DocumentoEnCurso");
		printf(" Tipo: %s\n", IFOpRetGet("Tipo"));
		printf(" Letra: %s\n", IFOpRetGet("Letra"));
		printf(" CodigoTipo: %d\n", IFOpRetIntGet("CodigoTipo"));
		printf(" Numero: %d\n", IFOpRetIntGet("Numero"));

		printf("FechaHora\n");
		IFOpBegin("FechaHora");
		if (!IFOpSend(1))
			cmd_error("FechaHora");
		printf(" Fecha: %s\n", IFOpRetGet("Fecha"));
		printf(" Hora: %s\n", IFOpRetGet("Hora"));

		printf("Ethernet\n");
		IFOpBegin("Ethernet");
		if (!IFOpSend(1))
			cmd_error("Ethernet");
		printf(" DireccionIP: %s\n", IFOpRetGet("DireccionIP"));
		printf(" MascaraRed: %s\n", IFOpRetGet("MascaraRed"));
		printf(" PuertaEnlace: %s\n", IFOpRetGet("PuertaEnlace"));
		printf(" MAC: %s\n", IFOpRetGet("MAC"));

		printf("ConfiguracionUSB\n");
		IFOpBegin("ConfiguracionUSB");
		if (!IFOpSend(1))
			cmd_error("ConfiguracionUSB");
		printf(" Modo: %s\n", IFOpRetGet("Modo"));

		printf("DescargasPendientes\n");
		IFOpBegin("DescargasPendientes");
		if (!IFOpSend(1))
			cmd_error("DescargasPendientes");
		printf(" PrimerZPendiente: %s\n", IFOpRetGet("PrimerZPendiente"));
		printf(" FechaPrimerZPendiente: %s\n", IFOpRetGet("FechaPrimerZPendiente"));
		printf(" HoraPrimerZPendiente: %s\n", IFOpRetGet("HoraPrimerZPendiente"));
		printf(" UltimoZPendiente: %s\n", IFOpRetGet("UltimoZPendiente"));
		printf(" FechaUltimoZPendiente: %s\n", IFOpRetGet("FechaUltimoZPendiente"));
		printf(" HoraUltimoZPendiente: %s\n", IFOpRetGet("HoraUltimoZPendiente"));
		printf(" CantidadGeneracionesNoDescargadas: %s\n", IFOpRetGet("CantidadGeneracionesNoDescargadas"));
		printf(" PrimerGeneracionNoDescargada: %s\n", IFOpRetGet("PrimerGeneracionNoDescargada"));
	}
	else if (_stricmp(testname,"tique") == 0) /* Tique */
	{
		printf("AbrirTique\n");
		IFOpBegin("AbrirTique");
		if (!IFOpSend(1))
			cmd_error("AbrirTique");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba");
		IFOpParamFloatSet("Precio", 1.2345);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoProducto", "7791234567898");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));

		printf("AbrirCajon\n");
		IFOpBegin("AbrirCajon");
		if (!IFOpSend(1))
			cmd_error("AbrirCajon");
	}
	else if (_stricmp(testname,"tnc") == 0) /* Tique Nota de Credito */
	{
		printf("ComprobanteAsociado\n");
		IFOpBegin("ComprobanteAsociado");
		IFOpParamIntSet("CodigoTipo", 83);
		IFOpParamIntSet("PV", 12345);
		IFOpParamIntSet("Numero", 12345678);
		if (!IFOpSend(1))
			cmd_error("ComprobanteAsociado");

		printf("AbrirTiqueNotaCredito\n");
		IFOpBegin("AbrirTiqueNotaCredito");
		if (!IFOpSend(1))
			cmd_error("AbrirTiqueNotaCredito");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción extra del ítem");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba");
		IFOpParamFloatSet("Cantidad", 3.0);
		IFOpParamFloatSet("Precio", 1.2345);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoProducto", "6935750533048");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción extra del ítem");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("ItemRetorno\n");
		IFOpBegin("ItemRetorno");
		IFOpParamSet("Descripcion", "Item de prueba");
		IFOpParamFloatSet("Cantidad", 2.0);
		IFOpParamFloatSet("Precio", 1.2345);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoProducto", "6935750533048");
		if (!IFOpSend(1))
			cmd_error("ItemRetorno");

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"factura") == 0) /* Factura */
	{
		printf("AbrirFactura\n");
		IFOpBegin("AbrirFactura");
		IFOpParamSet("ClienteResponsabilidad", "I");
		IFOpParamSet("ClienteRazonSocial1", "Razon social cliente");
		IFOpParamSet("ClienteTipoDocumento", "CUIT");
		IFOpParamSet("ClienteNumeroDocumento", "11111111113");
		IFOpParamSet("ClienteDomicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("AbrirFactura");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 1");
		IFOpParamFloatSet("Cantidad", 3.0);
		IFOpParamFloatSet("Precio", 1.2345);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 2");
		IFOpParamFloatSet("Cantidad", 1.0);
		IFOpParamFloatSet("Precio", 1.2);
		IFOpParamFloatSet("IVA", 10.5);
		IFOpParamSet("CodigoInterno", "1002");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 3");
		IFOpParamFloatSet("Precio", 1.3);
		IFOpParamFloatSet("IVA", 0.0);
		IFOpParamSet("CodigoInterno", "1003");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 4");
		IFOpParamFloatSet("Precio", 1.4);
		IFOpParamSet("IVA", "E");
		IFOpParamSet("CodigoInterno", "1004");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 5");
		IFOpParamFloatSet("Precio", 1.5);
		IFOpParamSet("IVA", "N");
		IFOpParamSet("CodigoInterno", "1005");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 6");
		IFOpParamFloatSet("Precio", 1.6);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamFloatSet("MontoImpIntFijo", 0.6);
		IFOpParamSet("CodigoInterno", "1006");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 7");
		IFOpParamFloatSet("Precio", 1.7);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamFloatSet("TasaAjuste", 0.14893617);
		IFOpParamSet("CodigoInterno", "1007");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("SubtotalImpreso\n");
		IFOpBegin("SubtotalImpreso");
		if (!IFOpSend(1))
			cmd_error("SubtotalImpreso");
		printf(" CantidadItems: %s\n", IFOpRetGet("CantidadItems"));
		printf(" Total: %f\n", IFOpRetFloatGet("Total"));
		printf(" IVA: %f\n", IFOpRetFloatGet("IVA"));
		printf(" Pagado: %f\n", IFOpRetFloatGet("Pagado"));
		printf(" ImpIntPorc: %f\n", IFOpRetFloatGet("ImpIntPorc"));
		printf(" ImpIntFijo: %f\n", IFOpRetFloatGet("ImpIntFijo"));
		printf(" Neto: %f\n", IFOpRetFloatGet("Neto"));

		printf("ItemBonificacion\n");
		IFOpBegin("ItemBonificacion");
		IFOpParamSet("Descripcion", "Decuento articulo");
		IFOpParamFloatSet("Cantidad", 3.0);
		IFOpParamFloatSet("Precio", 0.12345);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoInterno", "1001b");
		if (!IFOpSend(1))
			cmd_error("ItemBonificacion");

		printf("ItemRetornoBonificacion\n");
		IFOpBegin("ItemRetornoBonificacion");
		IFOpParamSet("Descripcion", "Decuento articulo");
		IFOpParamFloatSet("Cantidad", 1.0);
		IFOpParamFloatSet("Precio", 0.12345);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoInterno", "1001b");
		if (!IFOpSend(1))
			cmd_error("ItemRetornoBonificacion");

		printf("OtroTributo\n");
		IFOpBegin("OtroTributo");
		IFOpParamIntSet("CodigoTipo", 7);
		IFOpParamFloatSet("Monto", 5.0);
		if (!IFOpSend(1))
			cmd_error("OtroTributo");

		printf("Pago\n");
		IFOpBegin("Pago");
		IFOpParamFloatSet("Monto", 50.0);
		IFOpParamIntSet("CodigoTipo", 8);
		if (!IFOpSend(1))
			cmd_error("Pago");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));

		printf("SubtotalInfo\n");
		IFOpBegin("SubtotalInfo");
		if (!IFOpSend(1))
			cmd_error("SubtotalInfo");
		printf(" CantidadItems: %s\n", IFOpRetGet("CantidadItems"));
		printf(" Total: %f\n", IFOpRetFloatGet("Total"));
		printf(" IVA: %f\n", IFOpRetFloatGet("IVA"));
		printf(" Pagado: %f\n", IFOpRetFloatGet("Pagado"));
		printf(" ImpIntPorc: %f\n", IFOpRetFloatGet("ImpIntPorc"));
		printf(" ImpIntFijo: %f\n", IFOpRetFloatGet("ImpIntFijo"));
		printf(" Neto: %f\n", IFOpRetFloatGet("Neto"));
	}
	else if (_stricmp(testname,"credito") == 0) /* Nota de Crédito */
	{
		printf("AbrirNotaCredito\n");
		IFOpBegin("AbrirNotaCredito");
		IFOpParamSet("ClienteResponsabilidad", "M");
		IFOpParamSet("ClienteRazonSocial1", "Razon social cliente");
		IFOpParamSet("ClienteTipoDocumento", "CUIT");
		IFOpParamSet("ClienteNumeroDocumento", "11111111113");
		IFOpParamSet("ClienteDomicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("AbrirNotaCredito");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba");
		IFOpParamFloatSet("Cantidad", 3.0);
		IFOpParamFloatSet("Precio", 1.5);
		IFOpParamFloatSet("IVA", 10.5);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemSena\n");
		IFOpBegin("ItemSena");
		IFOpParamSet("Descripcion", "Item de seña");
		IFOpParamFloatSet("Cantidad", 3.0);
		IFOpParamFloatSet("Precio", 3.2);
		IFOpParamFloatSet("IVA", 0.0);
		IFOpParamSet("CodigoInterno", "2001");
		if (!IFOpSend(1))
			cmd_error("ItemSena");

		printf("ItemRetornoSena\n");
		IFOpBegin("ItemRetornoSena");
		IFOpParamSet("Descripcion", "Item de seña");
		IFOpParamFloatSet("Cantidad", -2.0);
		IFOpParamFloatSet("Precio", -3.2);
		IFOpParamFloatSet("IVA", 0.0);
		IFOpParamSet("CodigoInterno", "2001");
		if (!IFOpSend(1))
			cmd_error("ItemRetornoSena");

		printf("DescuentoGeneral\n");
		IFOpBegin("DescuentoGeneral");
		IFOpParamSet("Descripcion", "Oferta del día");
		IFOpParamFloatSet("Monto", 2.4);
		if (!IFOpSend(1))
			cmd_error("DescuentoGeneral");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Pago\n");
		IFOpBegin("Pago");
		IFOpParamFloatSet("Monto", 20.0);
		if (!IFOpSend(1))
			cmd_error("Pago");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"debito") == 0) /* Nota de Débito */
	{
		printf("AbrirNotaDebito\n");
		IFOpBegin("AbrirNotaDebito");
		IFOpParamSet("ClienteResponsabilidad", "F");
		IFOpParamSet("ClienteRazonSocial1", "Razon social cliente");
		IFOpParamSet("ClienteTipoDocumento", "DNI");
		IFOpParamSet("ClienteNumeroDocumento", "11222333");
		IFOpParamSet("ClienteDomicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("AbrirNotaDebito");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 1");
		IFOpParamFloatSet("Precio", 1.5);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 2");
		IFOpParamFloatSet("Precio", 0.5);
		IFOpParamFloatSet("IVA", 10.5);
		IFOpParamSet("CodigoInterno", "1002");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("RecargoGeneral\n");
		IFOpBegin("RecargoGeneral");
		IFOpParamSet("Descripcion", "Recargo administrativo");
		IFOpParamFloatSet("Monto", 2.0);
		if (!IFOpSend(1))
			cmd_error("RecargoGeneral");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Pago\n");
		IFOpBegin("Pago");
		IFOpParamSet("Descripcion", "CTA 123458");
		IFOpParamFloatSet("Monto", 20.0);
		IFOpParamIntSet("CodigoTipo", 6);
		IFOpParamSet("TextoLibre", "Vencimiento XX/XX/XXXX");
		if (!IFOpSend(1))
			cmd_error("Pago");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"recibo") == 0) /* Recibo */
	{
		printf("AbrirRecibo\n");
		IFOpBegin("AbrirRecibo");
		IFOpParamSet("ClienteResponsabilidad", "I");
		IFOpParamSet("ClienteRazonSocial1", "Razon social cliente");
		IFOpParamSet("ClienteTipoDocumento", "CUIT");
		IFOpParamSet("ClienteNumeroDocumento", "11111111113");
		IFOpParamSet("ClienteDomicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("AbrirRecibo");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba");
		IFOpParamFloatSet("Precio", 2.5);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("Pago\n");
		IFOpBegin("Pago");
		IFOpParamSet("Descripcion", "Tarjeta XXXX");
		IFOpParamFloatSet("Monto", 5.0);
		IFOpParamIntSet("CodigoTipo", 20);
		IFOpParamSet("Cuotas", "12");
		IFOpParamSet("Cupones", "XXX-XX-XXXX");
		if (!IFOpSend(1))
			cmd_error("Pago");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"generico") == 0) /* Documento Generico */
	{
		printf("AbrirDocGenerico\n");
		IFOpBegin("AbrirDocGenerico");
		if (!IFOpSend(1))
			cmd_error("AbrirDocGenerico");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Línea de texto no fiscal");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "abc \\R\\Resaltado\\f\\ def");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "abc \\A\\Doble alto\\f\\ def");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "abc \\N\\Doble ancho\\f\\ def");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "abc \\S\\Subrayado\\f\\ def");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "abc \\AN\\Doble A&A\\f\\ def");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "CODE 39 \\xE1\\A1+-.$/%\\xE0\\");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Interleaved \\xE3\\1122334455\\xE0\\");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "UPC A \\xE5\\123456789012\\xE0\\");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "EAN 13 \\xE7\\123456789012\\xE0\\");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "EAN 8 \\xEA\\12345678\\xE0\\");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "CODABAR \\xEC\\D164-$:/.+B-\\xE0\\");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"interno") == 0) /* Documento de Uso Interno */
	{
		printf("AbrirDocInterno\n");
		IFOpBegin("AbrirDocInterno");
		if (!IFOpSend(1))
			cmd_error("AbrirDocInterno");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Línea de texto no fiscal");
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"voucher") == 0) /* Voucher de Tarjeta de Crédito */
	{
		printf("AbrirDNFH\n");
		IFOpBegin("AbrirDNFH");
		IFOpParamIntSet("CodigoTipo", 922);
		IFOpParamSet("Atributos", "difat");
		if (!IFOpSend(1))
			cmd_error("AbrirDNFH");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 1);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 2);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 3);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "09/14");
		IFOpParamIntSet("Tipo", 4);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 5);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Línea libre 1 (opcional)");
		IFOpParamIntSet("Tipo", 19);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Línea libre 2 (opcional)");
		IFOpParamIntSet("Tipo", 20);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Línea libre 3 (opcional)");
		IFOpParamIntSet("Tipo", 21);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 6);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 7);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 8);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 9);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 10);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 11);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 12);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Línea libre 4 (opcional)");
		IFOpParamIntSet("Tipo", 22);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Línea libre 5 (opcional)");
		IFOpParamIntSet("Tipo", 23);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Línea libre 6 (opcional)");
		IFOpParamIntSet("Tipo", 24);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 13);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 14);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 15);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 16);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 17);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("TextoNoFiscal\n");
		IFOpBegin("TextoNoFiscal");
		IFOpParamSet("Texto", "Dato libre");
		IFOpParamIntSet("Tipo", 18);
		if (!IFOpSend(1))
			cmd_error("TextoNoFiscal");

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"remitor") == 0) /* Remito R */
	{
		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "0");
		IFOpParamSet("Responsabilidad", "I");
		IFOpParamSet("RazonSocial1", "Razon social cliente");
		IFOpParamSet("TipoDocumento", "CUIT");
		IFOpParamSet("NumeroDocumento", "11111111113");
		IFOpParamSet("Domicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "2");
		IFOpParamSet("Responsabilidad", "I");
		IFOpParamSet("RazonSocial1", "Razon social transportista");
		IFOpParamSet("TipoDocumento", "CUIT");
		IFOpParamSet("NumeroDocumento", "99999999995");
		IFOpParamSet("Domicilio1", "Domicilio transportista");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "3");
		IFOpParamSet("Responsabilidad", "F");
		IFOpParamSet("RazonSocial1", "Nombre Chofer");
		IFOpParamSet("TipoDocumento", "DNI");
		IFOpParamSet("NumeroDocumento", "11222333");
		IFOpParamSet("Domicilio1", "Patente 1");
		IFOpParamSet("Domicilio2", "Patente 2");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("AbrirRemitoR\n");
		IFOpBegin("AbrirRemitoR");
		if (!IFOpSend(1))
			cmd_error("AbrirRemitoR");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 1");
		IFOpParamFloatSet("Cantidad", 2.0);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 2");
		IFOpParamFloatSet("Cantidad", 3.0);
		IFOpParamSet("CodigoInterno", "1002");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"remitox") == 0) /* Remito X */
	{
		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "0");
		IFOpParamSet("Responsabilidad", "I");
		IFOpParamSet("RazonSocial1", "Razon social cliente");
		IFOpParamSet("TipoDocumento", "CUIT");
		IFOpParamSet("NumeroDocumento", "11111111113");
		IFOpParamSet("Domicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "2");
		IFOpParamSet("Responsabilidad", "I");
		IFOpParamSet("RazonSocial1", "Razon social transportista");
		IFOpParamSet("TipoDocumento", "CUIT");
		IFOpParamSet("NumeroDocumento", "99999999995");
		IFOpParamSet("Domicilio1", "Domicilio transportista");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "3");
		IFOpParamSet("Responsabilidad", "F");
		IFOpParamSet("RazonSocial1", "Nombre Chofer");
		IFOpParamSet("TipoDocumento", "DNI");
		IFOpParamSet("NumeroDocumento", "11222333");
		IFOpParamSet("Domicilio1", "Patente 1");
		IFOpParamSet("Domicilio2", "Patente 2");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("AbrirRemitoX\n");
		IFOpBegin("AbrirRemitoX");
		if (!IFOpSend(1))
			cmd_error("AbrirRemitoX");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 1");
		IFOpParamFloatSet("Cantidad", 12.345678);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 2");
		IFOpParamSet("CodigoInterno", "1002");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"recibox") == 0) /* Recibo X */
	{
		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "0");
		IFOpParamSet("Responsabilidad", "I");
		IFOpParamSet("RazonSocial1", "Razon social cliente");
		IFOpParamSet("TipoDocumento", "CUIT");
		IFOpParamSet("NumeroDocumento", "11111111113");
		IFOpParamSet("Domicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("AbrirReciboX\n");
		IFOpBegin("AbrirReciboX");
		if (!IFOpSend(1))
			cmd_error("AbrirReciboX");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción línea 1");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción línea 2");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción línea 3");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción línea 4");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Descripción línea 5");
		IFOpParamFloatSet("Precio", 12.34);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("Pago\n");
		IFOpBegin("Pago");
		IFOpParamFloatSet("Monto", 50.0);
		IFOpParamIntSet("CodigoTipo", 8);
		if (!IFOpSend(1))
			cmd_error("Pago");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"presupuesto") == 0) /* Presupuesto */
	{
		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "0");
		IFOpParamSet("Responsabilidad", "I");
		IFOpParamSet("RazonSocial1", "Razon social cliente");
		IFOpParamSet("TipoDocumento", "CUIT");
		IFOpParamSet("NumeroDocumento", "11111111113");
		IFOpParamSet("Domicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("AbrirPresupuesto\n");
		IFOpBegin("AbrirPresupuesto");
		if (!IFOpSend(1))
			cmd_error("AbrirPresupuesto");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 1");
		IFOpParamFloatSet("Precio", 12.34);
		IFOpParamFloatSet("IVA", 21.0);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Item de prueba 2");
		IFOpParamFloatSet("Precio", 5.0);
		IFOpParamFloatSet("IVA", 10.5);
		IFOpParamSet("CodigoInterno", "1002");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("DescuentoGeneral\n");
		IFOpBegin("DescuentoGeneral");
		IFOpParamSet("Descripcion", "Oferta del día");
		IFOpParamFloatSet("Monto", 2.34);
		if (!IFOpSend(1))
			cmd_error("DescuentoGeneral");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"donacion") == 0) /* Documento Donación */
	{
		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "0");
		IFOpParamSet("Responsabilidad", "I");
		IFOpParamSet("RazonSocial1", "Razon social cliente");
		IFOpParamSet("TipoDocumento", "CUIT");
		IFOpParamSet("NumeroDocumento", "11111111113");
		IFOpParamSet("Domicilio1", "Domicilio cliente");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("DatosTercero\n");
		IFOpBegin("DatosTercero");
		IFOpParamSet("Tipo", "1");
		IFOpParamSet("Responsabilidad", "I");
		IFOpParamSet("RazonSocial1", "Razon social beneficiario");
		IFOpParamSet("TipoDocumento", "CUIT");
		IFOpParamSet("NumeroDocumento", "99999999995");
		IFOpParamSet("Domicilio1", "Domicilio beneficiario");
		if (!IFOpSend(1))
			cmd_error("DatosTercero");

		printf("AbrirDonacion\n");
		IFOpBegin("AbrirDonacion");
		IFOpParamSet("Texto", "Descripción línea 1");
		if (!IFOpSend(1))
			cmd_error("AbrirDonacion");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción línea 2");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción línea 3");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("TextoFiscal\n");
		IFOpBegin("TextoFiscal");
		IFOpParamSet("Texto", "Descripción línea 4");
		if (!IFOpSend(1))
			cmd_error("TextoFiscal");

		printf("ItemVenta\n");
		IFOpBegin("ItemVenta");
		IFOpParamSet("Descripcion", "Descripción línea 5");
		IFOpParamFloatSet("Precio", 12.34);
		IFOpParamSet("CodigoInterno", "1001");
		if (!IFOpSend(1))
			cmd_error("ItemVenta");

		printf("Pago\n");
		IFOpBegin("Pago");
		IFOpParamFloatSet("Monto", 50.0);
		IFOpParamIntSet("CodigoTipo", 8);
		if (!IFOpSend(1))
			cmd_error("Pago");
		printf(" MontoFaltaPagar: %f\n", IFOpRetFloatGet("MontoFaltaPagar"));

		printf("Cerrar\n");
		IFOpBegin("Cerrar");
		if (!IFOpSend(1))
			cmd_error("Cerrar");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CodigoTipo: %s\n", IFOpRetGet("CodigoTipo"));
	}
	else if (_stricmp(testname,"tiqueinfo") == 0) /* Tique de Información del Equipo */
	{
		printf("ImprimirInformacion\n");
		IFOpBegin("ImprimirInformacion");
		if (!IFOpSend(1))
			cmd_error("ImprimirInformacion");
	}
	else if (_stricmp(testname,"printertest") == 0) /* Prueba Mecanismo Impresor */
	{
		printf("ImprimirPruebaImpresora\n");
		IFOpBegin("ImprimirPruebaImpresora");
		if (!IFOpSend(1))
			cmd_error("ImprimirPruebaImpresora");
	}
	else if (_stricmp(testname,"reimprimir") == 0) /* Reimpresión Tique 1 */
	{
		printf("Reimprimir\n");
		IFOpBegin("Reimprimir");
		IFOpParamIntSet("CodigoTipo", 83);
		IFOpParamIntSet("Numero", 1);
		if (!IFOpSend(1))
			cmd_error("Reimprimir");
	}
	else if (_stricmp(testname,"cancel") == 0) /* Cancelación */
	{
		printf("AbrirTique\n");
		IFOpBegin("AbrirTique");
		if (!IFOpSend(1))
			cmd_error("AbrirTique");

		printf("Cancelar\n");
		IFOpBegin("Cancelar");
		if (!IFOpSend(1))
			cmd_error("Cancelar");
	}
	else if (_stricmp(testname,"totalestique") == 0) /* Obtiene totales de jornada para Tique */
	{
		printf("Contadores\n");
		IFOpBegin("Contadores");
		IFOpParamIntSet("CodigoTipo", 83);
		if (!IFOpSend(1))
			cmd_error("Contadores");
		printf(" NumeroUltimoZ: %d\n", IFOpRetIntGet("NumeroUltimoZ"));
		printf(" NumeroUltimoCambioFechaHora: %d\n", IFOpRetIntGet("NumeroUltimoCambioFechaHora"));
		printf(" NumeroUltimoInformeAuditoria: %d\n", IFOpRetIntGet("NumeroUltimoInformeAuditoria"));
		printf(" NumeroUltimoDocumento: %d\n", IFOpRetIntGet("NumeroUltimoDocumento"));

		printf("TotalesJornada\n");
		IFOpBegin("TotalesJornada");
		IFOpParamIntSet("CodigoTipo", 83);
		if (!IFOpSend(1))
			cmd_error("TotalesJornada");
		printf(" FechaAperturaJornada: %s\n", IFOpRetGet("FechaAperturaJornada"));
		printf(" HoraAperturaJornada: %s\n", IFOpRetGet("HoraAperturaJornada"));
		printf(" NumeroUltimoZ: %d\n", IFOpRetIntGet("NumeroUltimoZ"));
		printf(" NecesitaZ: %s\n", IFOpRetBoolGet("NecesitaZ") ? "Si" : "No");
		printf(" CantidadEmitidos: %d\n", IFOpRetIntGet("CantidadEmitidos"));
		printf(" CantidadCancelados: %d\n", IFOpRetIntGet("CantidadCancelados"));
		printf(" Total: %f\n", IFOpRetFloatGet("Total"));
		printf(" TotalIva: %f\n", IFOpRetFloatGet("TotalIva"));
		printf(" TotalImpIntFijo: %f\n", IFOpRetFloatGet("TotalImpIntFijo"));
		printf(" TotalImpIntPorc: %f\n", IFOpRetFloatGet("TotalImpIntPorc"));
		printf(" TotalOtroTributo: %f\n", IFOpRetFloatGet("TotalOtroTributo"));

		printf("TotalesJornadaIva\n");
		IFOpBegin("TotalesJornadaIva");
		IFOpParamIntSet("CodigoTipo", 83);
		if (!IFOpSend(1))
			cmd_error("TotalesJornadaIva");
		printf(" TotalIva: %f\n", IFOpRetFloatGet("TotalIva"));
		printf(" TasaIva1: %f\n", IFOpRetFloatGet("TasaIva1"));
		printf(" TotalIva1: %f\n", IFOpRetFloatGet("TotalIva1"));
		printf(" TotalVentaIva1: %f\n", IFOpRetFloatGet("TotalVentaIva1"));
		printf(" TotalImpIntFijoIva1: %f\n", IFOpRetFloatGet("TotalImpIntFijoIva1"));
		printf(" TotalImpIntPorcIva1: %f\n", IFOpRetFloatGet("TotalImpIntPorcIva1"));
		printf(" TasaIva2: %f\n", IFOpRetFloatGet("TasaIva2"));
		printf(" TotalIva2: %f\n", IFOpRetFloatGet("TotalIva2"));
		printf(" TotalVentaIva2: %f\n", IFOpRetFloatGet("TotalVentaIva2"));
		printf(" TotalImpIntFijoIva2: %f\n", IFOpRetFloatGet("TotalImpIntFijoIva2"));
		printf(" TotalImpIntPorcIva2: %f\n", IFOpRetFloatGet("TotalImpIntPorcIva2"));
		printf(" TasaIva3: %f\n", IFOpRetFloatGet("TasaIva3"));
		printf(" TotalIva3: %f\n", IFOpRetFloatGet("TotalIva3"));
		printf(" TotalVentaIva3: %f\n", IFOpRetFloatGet("TotalVentaIva3"));
		printf(" TotalImpIntFijoIva3: %f\n", IFOpRetFloatGet("TotalImpIntFijoIva3"));
		printf(" TotalImpIntPorcIva3: %f\n", IFOpRetFloatGet("TotalImpIntPorcIva3"));
		printf(" TasaIva4: %f\n", IFOpRetFloatGet("TasaIva4"));
		printf(" TotalIva4: %f\n", IFOpRetFloatGet("TotalIva4"));
		printf(" TotalVentaIva4: %f\n", IFOpRetFloatGet("TotalVentaIva4"));
		printf(" TotalImpIntFijoIva4: %f\n", IFOpRetFloatGet("TotalImpIntFijoIva4"));
		printf(" TotalImpIntPorcIva4: %f\n", IFOpRetFloatGet("TotalImpIntPorcIva4"));
		printf(" TasaIva5: %f\n", IFOpRetFloatGet("TasaIva5"));
		printf(" TotalIva5: %f\n", IFOpRetFloatGet("TotalIva5"));
		printf(" TotalVentaIva5: %f\n", IFOpRetFloatGet("TotalVentaIva5"));
		printf(" TotalImpIntFijoIva5: %f\n", IFOpRetFloatGet("TotalImpIntFijoIva5"));
		printf(" TotalImpIntPorcIva5: %f\n", IFOpRetFloatGet("TotalImpIntPorcIva5"));
		printf(" TasaIva6: %f\n", IFOpRetFloatGet("TasaIva6"));
		printf(" TotalIva6: %f\n", IFOpRetFloatGet("TotalIva6"));
		printf(" TotalVentaIva6: %f\n", IFOpRetFloatGet("TotalVentaIva6"));
		printf(" TotalImpIntFijoIva6: %f\n", IFOpRetFloatGet("TotalImpIntFijoIva6"));
		printf(" TotalImpIntPorcIva6: %f\n", IFOpRetFloatGet("TotalImpIntPorcIva6"));

		printf("TotalesJornadaOtroTributo\n");
		IFOpBegin("TotalesJornadaOtroTributo");
		IFOpParamIntSet("CodigoTipo", 83);
		IFOpParamIntSet("IndiceOtroTributo", 1);
		if (!IFOpSend(1))
			cmd_error("TotalesJornadaOtroTributo");
		printf(" TotalOtroTributoGeneral: %f\n", IFOpRetFloatGet("TotalOtroTributoGeneral"));
		printf(" TotalOtroTributo07: %f\n", IFOpRetFloatGet("TotalOtroTributo07"));
		printf(" TotalOtroTributo06: %f\n", IFOpRetFloatGet("TotalOtroTributo06"));
		printf(" TotalOtroTributo09: %f\n", IFOpRetFloatGet("TotalOtroTributo09"));
		printf(" CantidadEnJornada: %d\n", IFOpRetIntGet("CantidadEnJornada"));
		printf(" TotalOtroTributo: %f\n", IFOpRetFloatGet("TotalOtroTributo"));
		printf(" CodigoOtroTributo: %d\n", IFOpRetIntGet("CodigoOtroTributo"));
	}
	else if (_stricmp(testname,"config") == 0) /* Configuración */
	{
		printf("EstablecerOpcion\n");
		IFOpBegin("EstablecerOpcion");
		IFOpParamIntSet("Numero", 242);
		IFOpParamIntSet("Valor", 1);
		if (!IFOpSend(1))
			cmd_error("EstablecerOpcion");

		printf("Opcion\n");
		IFOpBegin("Opcion");
		IFOpParamIntSet("Numero", 242);
		if (!IFOpSend(1))
			cmd_error("Opcion");
		printf(" Valor: %s\n", IFOpRetGet("Valor"));

		printf("EstablecerEncabezadoCola\n");
		IFOpBegin("EstablecerEncabezadoCola");
		IFOpParamIntSet("Numero", 79);
		IFOpParamSet("Texto", "Encabezado libre 9");
		if (!IFOpSend(1))
			cmd_error("EstablecerEncabezadoCola");

		printf("EncabezadoCola\n");
		IFOpBegin("EncabezadoCola");
		IFOpParamIntSet("Numero", 79);
		if (!IFOpSend(1))
			cmd_error("EncabezadoCola");
		printf(" Numero: %d\n", IFOpRetIntGet("Numero"));
		printf(" Texto: %s\n", IFOpRetGet("Texto"));

		printf("EstablecerEncabezadoCola\n");
		IFOpBegin("EstablecerEncabezadoCola");
		IFOpParamIntSet("Numero", 19);
		IFOpParamSet("Texto", "Cola libre 9");
		if (!IFOpSend(1))
			cmd_error("EstablecerEncabezadoCola");

		printf("EncabezadoCola\n");
		IFOpBegin("EncabezadoCola");
		IFOpParamIntSet("Numero", 19);
		if (!IFOpSend(1))
			cmd_error("EncabezadoCola");
		printf(" Numero: %d\n", IFOpRetIntGet("Numero"));
		printf(" Texto: %s\n", IFOpRetGet("Texto"));
	}
	else if (_stricmp(testname,"x") == 0) /* Informe X */
	{
		printf("InformeXNoImpreso\n");
		IFOpBegin("InformeXNoImpreso");
		if (!IFOpSend(1))
			cmd_error("InformeXNoImpreso");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CantidadDocFiscalCancel: %s\n", IFOpRetGet("CantidadDocFiscalCancel"));
		printf(" CantidadDocNoFiscal: %s\n", IFOpRetGet("CantidadDocNoFiscal"));
		printf(" CantidadDocGenerico: %s\n", IFOpRetGet("CantidadDocGenerico"));
		printf(" CantidadTique: %s\n", IFOpRetGet("CantidadTique"));
		printf(" CantidadFacturaA: %s\n", IFOpRetGet("CantidadFacturaA"));
		printf(" NumeroUltimoTique: %s\n", IFOpRetGet("NumeroUltimoTique"));
		printf(" MontoVenta: %f\n", IFOpRetFloatGet("MontoVenta"));
		printf(" MontoIVAVenta: %f\n", IFOpRetFloatGet("MontoIVAVenta"));
		printf(" MontoOtrosTributosVenta: %f\n", IFOpRetFloatGet("MontoOtrosTributosVenta"));
		printf(" NumeroFacturaA: %s\n", IFOpRetGet("NumeroFacturaA"));
		printf(" NumeroCreditoA: %s\n", IFOpRetGet("NumeroCreditoA"));
		printf(" NumeroCreditoB: %s\n", IFOpRetGet("NumeroCreditoB"));
		printf(" MontoCredito: %f\n", IFOpRetFloatGet("MontoCredito"));
		printf(" MontoIVACredito: %f\n", IFOpRetFloatGet("MontoIVACredito"));
		printf(" MontoOtrosTributosCredito: %f\n", IFOpRetFloatGet("MontoOtrosTributosCredito"));

		printf("InformeXResumido\n");
		IFOpBegin("InformeXResumido");
		if (!IFOpSend(1))
			cmd_error("InformeXResumido");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CantidadDocFiscalCancel: %s\n", IFOpRetGet("CantidadDocFiscalCancel"));
		printf(" CantidadDocNoFiscal: %s\n", IFOpRetGet("CantidadDocNoFiscal"));
		printf(" CantidadDocGenerico: %s\n", IFOpRetGet("CantidadDocGenerico"));
		printf(" CantidadTique: %s\n", IFOpRetGet("CantidadTique"));
		printf(" CantidadFacturaA: %s\n", IFOpRetGet("CantidadFacturaA"));
		printf(" NumeroUltimoTique: %s\n", IFOpRetGet("NumeroUltimoTique"));
		printf(" MontoVenta: %f\n", IFOpRetFloatGet("MontoVenta"));
		printf(" MontoIVAVenta: %f\n", IFOpRetFloatGet("MontoIVAVenta"));
		printf(" MontoOtrosTributosVenta: %f\n", IFOpRetFloatGet("MontoOtrosTributosVenta"));
		printf(" NumeroFacturaA: %s\n", IFOpRetGet("NumeroFacturaA"));
		printf(" NumeroCreditoA: %s\n", IFOpRetGet("NumeroCreditoA"));
		printf(" NumeroCreditoB: %s\n", IFOpRetGet("NumeroCreditoB"));
		printf(" MontoCredito: %f\n", IFOpRetFloatGet("MontoCredito"));
		printf(" MontoIVACredito: %f\n", IFOpRetFloatGet("MontoIVACredito"));
		printf(" MontoOtrosTributosCredito: %f\n", IFOpRetFloatGet("MontoOtrosTributosCredito"));

		printf("InformeXDetallado\n");
		IFOpBegin("InformeXDetallado");
		if (!IFOpSend(1))
			cmd_error("InformeXDetallado");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CantidadDocFiscalCancel: %s\n", IFOpRetGet("CantidadDocFiscalCancel"));
		printf(" CantidadDocNoFiscal: %s\n", IFOpRetGet("CantidadDocNoFiscal"));
		printf(" CantidadDocGenerico: %s\n", IFOpRetGet("CantidadDocGenerico"));
		printf(" CantidadTique: %s\n", IFOpRetGet("CantidadTique"));
		printf(" CantidadFacturaA: %s\n", IFOpRetGet("CantidadFacturaA"));
		printf(" NumeroUltimoTique: %s\n", IFOpRetGet("NumeroUltimoTique"));
		printf(" MontoVenta: %f\n", IFOpRetFloatGet("MontoVenta"));
		printf(" MontoIVAVenta: %f\n", IFOpRetFloatGet("MontoIVAVenta"));
		printf(" MontoOtrosTributosVenta: %f\n", IFOpRetFloatGet("MontoOtrosTributosVenta"));
		printf(" NumeroFacturaA: %s\n", IFOpRetGet("NumeroFacturaA"));
		printf(" NumeroCreditoA: %s\n", IFOpRetGet("NumeroCreditoA"));
		printf(" NumeroCreditoB: %s\n", IFOpRetGet("NumeroCreditoB"));
		printf(" MontoCredito: %f\n", IFOpRetFloatGet("MontoCredito"));
		printf(" MontoIVACredito: %f\n", IFOpRetFloatGet("MontoIVACredito"));
		printf(" MontoOtrosTributosCredito: %f\n", IFOpRetFloatGet("MontoOtrosTributosCredito"));
	}
	else if (_stricmp(testname,"z") == 0) /* Cierre Z */
	{
		printf("CierreZ\n");
		IFOpBegin("CierreZ");
		if (!IFOpSend(1))
			cmd_error("CierreZ");
		printf(" Numero: %s\n", IFOpRetGet("Numero"));
		printf(" CantidadDocFiscalCancel: %s\n", IFOpRetGet("CantidadDocFiscalCancel"));
		printf(" CantidadDocNoFiscal: %s\n", IFOpRetGet("CantidadDocNoFiscal"));
		printf(" CantidadDocGenerico: %s\n", IFOpRetGet("CantidadDocGenerico"));
		printf(" CantidadTique: %s\n", IFOpRetGet("CantidadTique"));
		printf(" CantidadFacturaA: %s\n", IFOpRetGet("CantidadFacturaA"));
		printf(" NumeroUltimoTique: %s\n", IFOpRetGet("NumeroUltimoTique"));
		printf(" MontoVenta: %f\n", IFOpRetFloatGet("MontoVenta"));
		printf(" MontoIVAVenta: %f\n", IFOpRetFloatGet("MontoIVAVenta"));
		printf(" MontoOtrosTributosVenta: %f\n", IFOpRetFloatGet("MontoOtrosTributosVenta"));
		printf(" NumeroFacturaA: %s\n", IFOpRetGet("NumeroFacturaA"));
		printf(" NumeroCreditoA: %s\n", IFOpRetGet("NumeroCreditoA"));
		printf(" NumeroCreditoB: %s\n", IFOpRetGet("NumeroCreditoB"));
		printf(" MontoCredito: %f\n", IFOpRetFloatGet("MontoCredito"));
		printf(" MontoIVACredito: %f\n", IFOpRetFloatGet("MontoIVACredito"));
		printf(" MontoOtrosTributosCredito: %f\n", IFOpRetFloatGet("MontoOtrosTributosCredito"));
	}
	else if (_stricmp(testname,"auditoria") == 0) /* Informe de Auditoría resumido */
	{
		printf("ImprimirAuditoriaResumidaPorZ\n");
		IFOpBegin("ImprimirAuditoriaResumidaPorZ");
		IFOpParamSet("ZInicial", "1");
		IFOpParamSet("ZFinal", "9999");
		if (!IFOpSend(1))
			cmd_error("ImprimirAuditoriaResumidaPorZ");
	}
	else if (_stricmp(testname,"misc") == 0) /* Miscelaneos */
	{
		printf("AbrirCajon\n");
		IFOpBegin("AbrirCajon");
		if (!IFOpSend(1))
			cmd_error("AbrirCajon");

		printf("AvanzarPapel\n");
		IFOpBegin("AvanzarPapel");
		IFOpParamSet("Lineas", "5");
		if (!IFOpSend(1))
			cmd_error("AvanzarPapel");

		printf("CortarPapel\n");
		IFOpBegin("CortarPapel");
		if (!IFOpSend(1))
			cmd_error("CortarPapel");

		printf("AbrirCajon2\n");
		IFOpBegin("AbrirCajon2");
		if (!IFOpSend(1))
			cmd_error("AbrirCajon2");
	}
	else if (_stricmp(testname,"eventlog") == 0) /* Descarga log de eventos */
	{
		const char *data;
		FILE *fout;
		int bloop;

		printf("ComenzarDescargaEventLog\n");
		IFOpBegin("ComenzarDescargaEventLog");
		if (!IFOpSend(1))
			cmd_error("ComenzarDescargaEventLog");

		fout = fopen("eventlog.txt", "wb");
		bloop = 1;
		while (bloop)
		{
			printf("DescargarBloque\n");
			IFOpBegin("DescargarBloque");
			if (!IFOpSend(1))
				cmd_error("DescargarBloque");
			data = IFOpRetGet("Datos");
			fwrite(data, 1, strlen(data), fout);
//			printf(" Datos: %s\n", data);
			bloop = IFOpRetBoolGet("Continuar");
//			printf(" Continuar: %s\n", bloop ? "Si" : "No");
		}
		fclose(fout);
	}
	else if (_stricmp(testname,"rptpend") == 0) /* Descarga reportes ya generados y no descargados */
	{
		while (1)
		{
			int npend, ipend, rpttype;

			printf("DescargasPendientes\n");
			IFOpBegin("DescargasPendientes");
			if (!IFOpSend(1))
				cmd_error("DescargasPendientes");
			npend = IFOpRetIntGet("CantidadGeneracionesNoDescargadas");
			printf(" CantidadGeneracionesNoDescargadas: %d\n", npend);
			ipend = IFOpRetIntGet("PrimerGeneracionNoDescargada");
			printf(" PrimerGeneracionNoDescargada: %d\n", ipend);

			if (!ipend)
				break;

			for (rpttype=1; rpttype<=3; rpttype++)
			{
				const char *filename, *data;
				FILE* fout;
				int bloop;

				printf("ComenzarDescargaReporte\n");
				IFOpBegin("ComenzarDescargaReporte");
				IFOpParamIntSet("TipoReporte", rpttype);
				IFOpParamIntSet("NumeroGeneracion", ipend);
				if (!IFOpSend(1))
					cmd_error("ComenzarDescargaReporte");
				filename = IFOpRetGet("NombreArchivo");
				printf(" NombreArchivo: %s\n", filename);

				fout = fopen(filename, "wb");
				bloop = 1;
				while (bloop)
				{
					printf("DescargarBloque\n");
					IFOpBegin("DescargarBloque");
					if (!IFOpSend(1))
						cmd_error("DescargarBloque");
					data = IFOpRetGet("Datos");
					fwrite(data, 1, strlen(data), fout);
		//			printf(" Datos: %s\n", data);
					bloop = IFOpRetBoolGet("Continuar");
		//			printf(" Continuar: %s\n", bloop ? "Si" : "No");
				}
				fclose(fout);
			}
		}
	}
	else if (_stricmp(testname,"rptzdown") == 0) /* Genera y descarga reportes por rango de Z */
	{
		int rpttype;

		printf("GenerarReportesPorZ desde %s hasta %s\n", extra1, extra2);
		IFOpBegin("GenerarReportesPorZ");
		IFOpParamSet("ZInicial", extra1);
		IFOpParamSet("ZFinal", extra2);
		if (!IFOpSend(1))
			cmd_error("GenerarReportesPorZ");
		printf(" NumeroGeneracion: %s\n", IFOpRetGet("NumeroGeneracion"));

		for (rpttype=1; rpttype<=3; rpttype++)
		{
			const char *filename, *data;
			FILE* fout;
			int bloop;

			printf("ComenzarDescargaReporte\n");
			IFOpBegin("ComenzarDescargaReporte");
			IFOpParamIntSet("TipoReporte", rpttype);
			if (!IFOpSend(1))
				cmd_error("ComenzarDescargaReporte");
			filename = IFOpRetGet("NombreArchivo");
			printf(" NombreArchivo: %s\n", filename);

			fout = fopen(filename, "wb");
			bloop = 1;
			while (bloop)
			{
				printf("DescargarBloque\n");
				IFOpBegin("DescargarBloque");
				if (!IFOpSend(1))
					cmd_error("DescargarBloque");
				data = IFOpRetGet("Datos");
				fwrite(data, 1, strlen(data), fout);
	//			printf(" Datos: %s\n", data);
				bloop = IFOpRetBoolGet("Continuar");
	//			printf(" Continuar: %s\n", bloop ? "Si" : "No");
			}
			fclose(fout);
		}
	}
	else if (_stricmp(testname,"docdown") == 0) /* Descarga xml de un documento emitido */
	{
		const char *data;
		FILE *fout;
		int bloop;

		printf("ComenzarDescargaDocumento %s %s\n", extra1, extra2);
		IFOpBegin("ComenzarDescargaDocumento");
		IFOpParamSet("CodigoTipo", extra1);
		IFOpParamSet("Numero", extra2);
		if (!IFOpSend(1))
			cmd_error("ComenzarDescargaDocumento");

		fout = fopen("doc.xml", "wb");
		bloop = 1;
		while (bloop)
		{
			printf("DescargarBloque\n");
			IFOpBegin("DescargarBloque");
			if (!IFOpSend(1))
				cmd_error("DescargarBloque");
			data = IFOpRetGet("Datos");
			fwrite(data, 1, strlen(data), fout);
//			printf(" Datos: %s\n", data);
			bloop = IFOpRetBoolGet("Continuar");
//			printf(" Continuar: %s\n", bloop ? "Si" : "No");
		}
		fclose(fout);
	}

	else
	{
		printf("Error: prueba desconocida: %s\n", testname);
		return 3;
	}
	
	return 0;
}
