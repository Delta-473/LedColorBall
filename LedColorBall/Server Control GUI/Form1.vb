Public Class MainGUI

    Private Sub AanUit_Click(sender As Object, e As EventArgs) Handles AanUit.Click
        ' AanUit.()

    End Sub

    Private Sub MainGUI_Paint(sender As Object, e As PaintEventArgs) Handles MyBase.Paint
        e.Graphics.DrawEllipse(Pens.Black, 250, 200, 20, 20)
        e.Graphics.FillEllipse(Brushes.Red, 250, 200, 19, 19)
    End Sub

    Private Sub MainGUI_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class
