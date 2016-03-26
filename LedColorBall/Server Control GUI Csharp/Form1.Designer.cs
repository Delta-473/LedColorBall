namespace Server_Control_GUI_Csharp
{
    partial class ServerControlGUI
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.ConsoleOutput = new System.Windows.Forms.TextBox();
            this.ConsoleInput = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // ConsoleOutput
            // 
            this.ConsoleOutput.Location = new System.Drawing.Point(12, 12);
            this.ConsoleOutput.Multiline = true;
            this.ConsoleOutput.Name = "ConsoleOutput";
            this.ConsoleOutput.ReadOnly = true;
            this.ConsoleOutput.Size = new System.Drawing.Size(427, 256);
            this.ConsoleOutput.TabIndex = 0;
            // 
            // ConsoleInput
            // 
            this.ConsoleInput.Location = new System.Drawing.Point(12, 292);
            this.ConsoleInput.Name = "ConsoleInput";
            this.ConsoleInput.Size = new System.Drawing.Size(427, 20);
            this.ConsoleInput.TabIndex = 1;
            // 
            // ServerControlGUI
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(451, 324);
            this.Controls.Add(this.ConsoleInput);
            this.Controls.Add(this.ConsoleOutput);
            this.Name = "ServerControlGUI";
            this.Text = "Server Control GUI";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox ConsoleOutput;
        private System.Windows.Forms.TextBox ConsoleInput;
    }
}

