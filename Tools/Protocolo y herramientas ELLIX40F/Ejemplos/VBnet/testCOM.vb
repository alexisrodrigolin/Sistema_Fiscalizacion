' Ejemplo de uso de Sam4sFiscalDriver
' 2019-04-03
' Para probar crear un formulario (Form1) con un boton (Button1)
Public Class Form1
    ' Agregar referencia al objeto COM "Sam4sFiscalDriver COM Server"
    Dim Drv As New Sam4sFiscalDriver.Sam4sFiscalDriver

    Private Sub CmdError(cmdname As String)
        MsgBox("Error " & Drv.IFOpErrorGet() & " en comando " & cmdname & ": " & Drv.IFOpErrorDescGet())
        Drv.SerialPortClose()
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        'MsgBox("Sam4sFiscalDriver Version: " + Drv.version)

        'Configura velocidad de comunicacion del puerto serial
        Dim baudrate = 9600
        If (Drv.SerialBaudSet(baudrate) = 0) Then
            MsgBox("No se pudo configurar la velocidad " & baudrate)
            Return
        End If

        'Abre el puerto serial
        Dim comnum = 8
        If (Drv.SerialPortOpen(comnum) = 0) Then
            MsgBox("No se pudo abrir el puerto serial " & comnum)
            Return
        End If

        ' Si hay un documento abierto, lo cancela primero
        Drv.IFOpBegin("DocumentoEnCurso")
        If (Drv.IFOpSend(1) = 0) Then
            CmdError("DocumentoEnCurso")
            Return
        End If
        If (Drv.IFOpRetIntGet("CodigoTipo") <> 0) Then
            Drv.IFOpBegin("Cancelar")
            If (Drv.IFOpSend(1) = 0) Then
                CmdError("Cancelar")
                Return
            End If
        End If
        
		'Ejemplo: Tique
		Drv.IFOpBegin("AbrirTique")
		If (Drv.IFOpSend(1) = 0) Then
			CmdError("AbrirTique")
			Return
		End If

		Drv.IFOpBegin("ItemVenta")
		Drv.IFOpParamSet("Descripcion", "Item de prueba")
		Drv.IFOpParamFloatSet("Precio", 1.2345)
		Drv.IFOpParamFloatSet("IVA", 21.0)
		Drv.IFOpParamSet("CodigoProducto", "7791234567898")
		If (Drv.IFOpSend(1) = 0) Then
			CmdError("ItemVenta")
			Return
		End If

		Drv.IFOpBegin("Cerrar")
		If (Drv.IFOpSend(1) = 0) Then
			CmdError("Cerrar")
			Return
		End If
		Dim resNumero = Drv.IFOpRetGet("Numero")
		Dim resCodigoTipo = Drv.IFOpRetGet("CodigoTipo")

		Drv.IFOpBegin("AbrirCajon")
		If (Drv.IFOpSend(1) = 0) Then
			CmdError("AbrirCajon")
			Return
		End If

        Drv.SerialPortClose()
        
        MsgBox("Se emitio el documento tipo " & resCodigoTipo & " numero " & resNumero)
    End Sub
End Class
