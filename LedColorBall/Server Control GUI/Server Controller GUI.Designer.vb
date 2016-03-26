<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class ServerControler
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.AanUit = New System.Windows.Forms.Button()
        Me.Button2 = New System.Windows.Forms.Button()
        Me.RadioButton1 = New System.Windows.Forms.RadioButton()
        Me.MenuStrip2 = New System.Windows.Forms.MenuStrip()
        Me.FileToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.VerbindingenToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.InstellingenToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.AfsluitenToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.HelpToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.OverToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.Color = New System.Windows.Forms.GroupBox()
        Me.LabelGreen = New System.Windows.Forms.Label()
        Me.LabelBlue = New System.Windows.Forms.Label()
        Me.LabelRed = New System.Windows.Forms.Label()
        Me.Blue = New System.Windows.Forms.NumericUpDown()
        Me.Green = New System.Windows.Forms.NumericUpDown()
        Me.Red = New System.Windows.Forms.NumericUpDown()
        Me.GroupBoxStatus = New System.Windows.Forms.GroupBox()
        Me.CheckBox4 = New System.Windows.Forms.CheckBox()
        Me.CheckBox3 = New System.Windows.Forms.CheckBox()
        Me.CheckBox2 = New System.Windows.Forms.CheckBox()
        Me.CheckBox1 = New System.Windows.Forms.CheckBox()
        Me.GroupBox1 = New System.Windows.Forms.GroupBox()
        Me.ConsoleInput = New System.Windows.Forms.TextBox()
        Me.ConsoleOutput = New System.Windows.Forms.TextBox()
        Me.MenuStrip2.SuspendLayout()
        Me.Color.SuspendLayout()
        CType(Me.Blue, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.Green, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.Red, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.GroupBoxStatus.SuspendLayout()
        Me.GroupBox1.SuspendLayout()
        Me.SuspendLayout()
        '
        'AanUit
        '
        Me.AanUit.Location = New System.Drawing.Point(12, 46)
        Me.AanUit.Name = "AanUit"
        Me.AanUit.Size = New System.Drawing.Size(75, 23)
        Me.AanUit.TabIndex = 0
        Me.AanUit.Text = "Aan"
        Me.AanUit.UseVisualStyleBackColor = True
        '
        'Button2
        '
        Me.Button2.Location = New System.Drawing.Point(742, 319)
        Me.Button2.Name = "Button2"
        Me.Button2.Size = New System.Drawing.Size(75, 23)
        Me.Button2.TabIndex = 1
        Me.Button2.Text = "Button2"
        Me.Button2.UseVisualStyleBackColor = True
        '
        'RadioButton1
        '
        Me.RadioButton1.AutoSize = True
        Me.RadioButton1.Location = New System.Drawing.Point(280, 100)
        Me.RadioButton1.Name = "RadioButton1"
        Me.RadioButton1.Size = New System.Drawing.Size(90, 17)
        Me.RadioButton1.TabIndex = 2
        Me.RadioButton1.TabStop = True
        Me.RadioButton1.Text = "RadioButton1"
        Me.RadioButton1.UseVisualStyleBackColor = True
        '
        'MenuStrip2
        '
        Me.MenuStrip2.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.FileToolStripMenuItem, Me.HelpToolStripMenuItem})
        Me.MenuStrip2.Location = New System.Drawing.Point(0, 0)
        Me.MenuStrip2.Name = "MenuStrip2"
        Me.MenuStrip2.Size = New System.Drawing.Size(836, 24)
        Me.MenuStrip2.TabIndex = 4
        Me.MenuStrip2.Text = "MenuStrip"
        '
        'FileToolStripMenuItem
        '
        Me.FileToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.VerbindingenToolStripMenuItem, Me.InstellingenToolStripMenuItem, Me.AfsluitenToolStripMenuItem})
        Me.FileToolStripMenuItem.Name = "FileToolStripMenuItem"
        Me.FileToolStripMenuItem.Size = New System.Drawing.Size(61, 20)
        Me.FileToolStripMenuItem.Text = "Bestand"
        '
        'VerbindingenToolStripMenuItem
        '
        Me.VerbindingenToolStripMenuItem.Name = "VerbindingenToolStripMenuItem"
        Me.VerbindingenToolStripMenuItem.Size = New System.Drawing.Size(145, 22)
        Me.VerbindingenToolStripMenuItem.Text = "Verbindingen"
        '
        'InstellingenToolStripMenuItem
        '
        Me.InstellingenToolStripMenuItem.Name = "InstellingenToolStripMenuItem"
        Me.InstellingenToolStripMenuItem.Size = New System.Drawing.Size(145, 22)
        Me.InstellingenToolStripMenuItem.Text = "Instellingen"
        '
        'AfsluitenToolStripMenuItem
        '
        Me.AfsluitenToolStripMenuItem.Name = "AfsluitenToolStripMenuItem"
        Me.AfsluitenToolStripMenuItem.Size = New System.Drawing.Size(145, 22)
        Me.AfsluitenToolStripMenuItem.Text = "Afsluiten"
        '
        'HelpToolStripMenuItem
        '
        Me.HelpToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.OverToolStripMenuItem})
        Me.HelpToolStripMenuItem.Name = "HelpToolStripMenuItem"
        Me.HelpToolStripMenuItem.Size = New System.Drawing.Size(44, 20)
        Me.HelpToolStripMenuItem.Text = "Help"
        '
        'OverToolStripMenuItem
        '
        Me.OverToolStripMenuItem.Name = "OverToolStripMenuItem"
        Me.OverToolStripMenuItem.Size = New System.Drawing.Size(99, 22)
        Me.OverToolStripMenuItem.Text = "Over"
        '
        'Color
        '
        Me.Color.Controls.Add(Me.LabelGreen)
        Me.Color.Controls.Add(Me.LabelBlue)
        Me.Color.Controls.Add(Me.LabelRed)
        Me.Color.Controls.Add(Me.Blue)
        Me.Color.Controls.Add(Me.Green)
        Me.Color.Controls.Add(Me.Red)
        Me.Color.Location = New System.Drawing.Point(12, 376)
        Me.Color.Name = "Color"
        Me.Color.Size = New System.Drawing.Size(100, 100)
        Me.Color.TabIndex = 5
        Me.Color.TabStop = False
        Me.Color.Text = "Kleur"
        '
        'LabelGreen
        '
        Me.LabelGreen.AutoSize = True
        Me.LabelGreen.Location = New System.Drawing.Point(15, 47)
        Me.LabelGreen.Name = "LabelGreen"
        Me.LabelGreen.Size = New System.Drawing.Size(15, 13)
        Me.LabelGreen.TabIndex = 7
        Me.LabelGreen.Text = "G"
        Me.LabelGreen.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'LabelBlue
        '
        Me.LabelBlue.AutoSize = True
        Me.LabelBlue.Location = New System.Drawing.Point(15, 74)
        Me.LabelBlue.Name = "LabelBlue"
        Me.LabelBlue.Size = New System.Drawing.Size(14, 13)
        Me.LabelBlue.TabIndex = 8
        Me.LabelBlue.Text = "B"
        Me.LabelBlue.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'LabelRed
        '
        Me.LabelRed.AutoSize = True
        Me.LabelRed.Location = New System.Drawing.Point(15, 21)
        Me.LabelRed.Name = "LabelRed"
        Me.LabelRed.Size = New System.Drawing.Size(15, 13)
        Me.LabelRed.TabIndex = 6
        Me.LabelRed.Text = "R"
        Me.LabelRed.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'Blue
        '
        Me.Blue.Location = New System.Drawing.Point(36, 74)
        Me.Blue.Maximum = New Decimal(New Integer() {255, 0, 0, 0})
        Me.Blue.Name = "Blue"
        Me.Blue.Size = New System.Drawing.Size(57, 20)
        Me.Blue.TabIndex = 7
        '
        'Green
        '
        Me.Green.Location = New System.Drawing.Point(36, 45)
        Me.Green.Maximum = New Decimal(New Integer() {255, 0, 0, 0})
        Me.Green.Name = "Green"
        Me.Green.Size = New System.Drawing.Size(57, 20)
        Me.Green.TabIndex = 8
        '
        'Red
        '
        Me.Red.Location = New System.Drawing.Point(36, 19)
        Me.Red.Maximum = New Decimal(New Integer() {255, 0, 0, 0})
        Me.Red.Name = "Red"
        Me.Red.Size = New System.Drawing.Size(57, 20)
        Me.Red.TabIndex = 6
        Me.Red.Tag = ""
        '
        'GroupBoxStatus
        '
        Me.GroupBoxStatus.Controls.Add(Me.CheckBox4)
        Me.GroupBoxStatus.Controls.Add(Me.CheckBox3)
        Me.GroupBoxStatus.Controls.Add(Me.CheckBox2)
        Me.GroupBoxStatus.Controls.Add(Me.CheckBox1)
        Me.GroupBoxStatus.Location = New System.Drawing.Point(118, 376)
        Me.GroupBoxStatus.Name = "GroupBoxStatus"
        Me.GroupBoxStatus.Size = New System.Drawing.Size(200, 100)
        Me.GroupBoxStatus.TabIndex = 6
        Me.GroupBoxStatus.TabStop = False
        Me.GroupBoxStatus.Text = "Status"
        '
        'CheckBox4
        '
        Me.CheckBox4.AutoSize = True
        Me.CheckBox4.Location = New System.Drawing.Point(6, 75)
        Me.CheckBox4.Name = "CheckBox4"
        Me.CheckBox4.Size = New System.Drawing.Size(104, 17)
        Me.CheckBox4.TabIndex = 10
        Me.CheckBox4.Text = "Systeem Gereed"
        Me.CheckBox4.UseVisualStyleBackColor = True
        '
        'CheckBox3
        '
        Me.CheckBox3.AutoSize = True
        Me.CheckBox3.Location = New System.Drawing.Point(6, 56)
        Me.CheckBox3.Name = "CheckBox3"
        Me.CheckBox3.Size = New System.Drawing.Size(113, 17)
        Me.CheckBox3.TabIndex = 9
        Me.CheckBox3.Text = "Verbinding Zender"
        Me.CheckBox3.UseVisualStyleBackColor = True
        '
        'CheckBox2
        '
        Me.CheckBox2.AutoSize = True
        Me.CheckBox2.Location = New System.Drawing.Point(6, 37)
        Me.CheckBox2.Name = "CheckBox2"
        Me.CheckBox2.Size = New System.Drawing.Size(117, 17)
        Me.CheckBox2.TabIndex = 8
        Me.CheckBox2.Text = "Netwerk Connectie"
        Me.CheckBox2.UseVisualStyleBackColor = True
        '
        'CheckBox1
        '
        Me.CheckBox1.AutoSize = True
        Me.CheckBox1.Location = New System.Drawing.Point(6, 19)
        Me.CheckBox1.Name = "CheckBox1"
        Me.CheckBox1.Size = New System.Drawing.Size(94, 17)
        Me.CheckBox1.TabIndex = 7
        Me.CheckBox1.Text = "Server Starten"
        Me.CheckBox1.UseVisualStyleBackColor = True
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.ConsoleInput)
        Me.GroupBox1.Controls.Add(Me.ConsoleOutput)
        Me.GroupBox1.Location = New System.Drawing.Point(324, 348)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(500, 128)
        Me.GroupBox1.TabIndex = 7
        Me.GroupBox1.TabStop = False
        Me.GroupBox1.Text = "Console"
        '
        'ConsoleInput
        '
        Me.ConsoleInput.Location = New System.Drawing.Point(6, 103)
        Me.ConsoleInput.Name = "ConsoleInput"
        Me.ConsoleInput.Size = New System.Drawing.Size(487, 20)
        Me.ConsoleInput.TabIndex = 1
        '
        'ConsoleOutput
        '
        Me.ConsoleOutput.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.ConsoleOutput.Location = New System.Drawing.Point(7, 13)
        Me.ConsoleOutput.Multiline = True
        Me.ConsoleOutput.Name = "ConsoleOutput"
        Me.ConsoleOutput.ReadOnly = True
        Me.ConsoleOutput.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        Me.ConsoleOutput.Size = New System.Drawing.Size(487, 88)
        Me.ConsoleOutput.TabIndex = 0
        '
        'ServerControler
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(836, 488)
        Me.Controls.Add(Me.GroupBox1)
        Me.Controls.Add(Me.GroupBoxStatus)
        Me.Controls.Add(Me.Color)
        Me.Controls.Add(Me.RadioButton1)
        Me.Controls.Add(Me.Button2)
        Me.Controls.Add(Me.AanUit)
        Me.Controls.Add(Me.MenuStrip2)
        Me.Name = "ServerControler"
        Me.Text = "Server Controller GUI"
        Me.MenuStrip2.ResumeLayout(False)
        Me.MenuStrip2.PerformLayout()
        Me.Color.ResumeLayout(False)
        Me.Color.PerformLayout()
        CType(Me.Blue, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.Green, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.Red, System.ComponentModel.ISupportInitialize).EndInit()
        Me.GroupBoxStatus.ResumeLayout(False)
        Me.GroupBoxStatus.PerformLayout()
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents AanUit As System.Windows.Forms.Button
    Friend WithEvents Button2 As System.Windows.Forms.Button
    Friend WithEvents RadioButton1 As System.Windows.Forms.RadioButton
    Friend WithEvents MenuStrip2 As System.Windows.Forms.MenuStrip
    Friend WithEvents FileToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents VerbindingenToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents InstellingenToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents AfsluitenToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents HelpToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents OverToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents Color As System.Windows.Forms.GroupBox
    Friend WithEvents LabelRed As System.Windows.Forms.Label
    Friend WithEvents Blue As System.Windows.Forms.NumericUpDown
    Friend WithEvents Green As System.Windows.Forms.NumericUpDown
    Friend WithEvents Red As System.Windows.Forms.NumericUpDown
    Friend WithEvents LabelGreen As System.Windows.Forms.Label
    Friend WithEvents LabelBlue As System.Windows.Forms.Label
    Friend WithEvents GroupBoxStatus As System.Windows.Forms.GroupBox
    Friend WithEvents CheckBox1 As System.Windows.Forms.CheckBox
    Friend WithEvents CheckBox4 As System.Windows.Forms.CheckBox
    Friend WithEvents CheckBox3 As System.Windows.Forms.CheckBox
    Friend WithEvents CheckBox2 As System.Windows.Forms.CheckBox
    Friend WithEvents GroupBox1 As System.Windows.Forms.GroupBox
    Friend WithEvents ConsoleInput As System.Windows.Forms.TextBox
    Friend WithEvents ConsoleOutput As System.Windows.Forms.TextBox

End Class
