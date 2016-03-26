Public Class ServerControler
    Private Delegate Sub ConsoleOutputAddBuffer(ByVal text As String)
    Private WithEvents ProcessServer As Process

    Private Sub AanUit_Click(sender As Object, e As EventArgs) Handles AanUit.Click
        ' AanUit.()

    End Sub

    '  Private Sub MainGUI_Paint(sender As Object, e As PaintEventArgs) Handles MyBase.Paint
    '    e.Graphics.DrawEllipse(Pens.Black, 250, 200, 20, 20)
    '    e.Graphics.FillEllipse(Brushes.Red, 250, 200, 19, 19)
    'End Sub

    Private Sub ServerControler_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ProcessServer = New Process
        With ProcessServer.StartInfo
            .FileName = "CMD.EXE"
            .UseShellExecute = False
            .CreateNoWindow = False
            .RedirectStandardError = False
            .RedirectStandardInput = True
            .RedirectStandardOutput = False
        End With
        ProcessServer.Start()


    End Sub

    Private Sub ServerControler_FormClosing(sender As Object, e As FormClosingEventArgs) Handles MyBase.FormClosing
        ProcessServer.StandardInput.WriteLine("EXIT")
        ProcessServer.StandardInput.Flush()
        ProcessServer.Close()
    End Sub

    Private Sub AfsluitenToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles AfsluitenToolStripMenuItem.Click
        Me.Close()
    End Sub

    Private Sub OverToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles OverToolStripMenuItem.Click
        About.Show()
    End Sub

    Private Sub InstellingenToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles InstellingenToolStripMenuItem.Click
        Settings.Show()
    End Sub

    Private Sub VerbindingenToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles VerbindingenToolStripMenuItem.Click
        Connections.Show()
    End Sub

    Private Sub ProcessServer_ErrorDataReceived(ByVal sender As Object, ByVal e As System.Diagnostics.DataReceivedEventArgs)
        ConsoleOutputAdd(vbCrLf & "Error: " & e.Data)
    End Sub

    Private Sub ProcessServer_OutputDataReceived(ByVal sender As Object, ByVal e As System.Diagnostics.DataReceivedEventArgs)
        ConsoleOutputAdd(vbCrLf & e.Data)
    End Sub

    Private Sub ExecuteButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        ProcessServer.StandardInput.WriteLine(ConsoleInput.Text)
        ProcessServer.StandardInput.Flush()
        ConsoleInput.Text = ""
    End Sub
    Private Sub ConsoleOutputAdd(ByVal text As String)
        If ConsoleOutput.InvokeRequired Then
            Dim ConsoleOutputBuffer As New ConsoleOutputAddBuffer(AddressOf ConsoleOutputAdd)
            Me.Invoke(ConsoleOutputBuffer, text)
        Else
            ConsoleOutput.AppendText(text)
        End If

    End Sub

End Class
