using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Text.RegularExpressions;
using System.Diagnostics.Eventing.Reader;

namespace _3M_CalderonDaniel05
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            tbNombre.TextAlignChanged += validarNombre;
            tbApellidos.TextChanged += validarApellidos;
            tbEdad.TextChanged += validarEdad;
            tbEstatura.TextChanged += validarEstatura;
            tbTelefono.TextChanged+= validarTelefono;

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void btnGuardar_Click(object sender, EventArgs e)
        {
            string nombres = tbNombre.Text;
            string apellidos = tbApellidos.Text;
            string edad = tbEdad.Text;
            string estatura = tbEstatura.Text;
            string telefono = tbTelefono.Text;
            string genero = "";

            if (rbHombre.Checked)
            {
                genero = "Hombre";
            }

            else if (rbMujer.Checked)
            {
                genero = "Mujer";
            }

            string datos = $"Nombre(s): {nombres}\r\nApellidos: {apellidos}\r\nEdad: {edad}\r\nEstatura: {estatura}\r\nTelefono: {telefono}\r\nGenero: {genero}";

            string rutaArchivo = "C:\\Users\\lenin\\Music\\datos.txt";
            bool archivoExiste = File.Exists(rutaArchivo);

            using (StreamWriter writer = new StreamWriter(rutaArchivo, true))
            {
                if (archivoExiste)
                {
                    writer.WriteLine();
                }
                writer.WriteLine(datos);

            }
            MessageBox.Show("Datos guardados con exito:\n\n" + datos, "Informacion",
            MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
        private bool EsEnteroValido(string valor)
        {
            int resultado;
            return int.TryParse(valor, out resultado);
        }

        private bool EsDecimalValido(string valor)
        {
            decimal resultado;
            return decimal.TryParse(valor, out resultado);
        }

        private bool EsEnteroValido10Digitos(string valor)
        {
            long resultado;
            return long.TryParse(valor, out resultado) && valor.Length == 10;
           
        }

        private bool EsTextoValido (string valor)
        {
            return Regex.IsMatch(valor, @"^[a-zA-Z\s]+$");
        }

        private void validarEdad(object sender, EventArgs e)
        {
            TextBox textBox = (TextBox)sender;

            if (string.IsNullOrWhiteSpace(textBox.Text))
            {
                return; 
            }
            if (!EsEnteroValido(textBox.Text))
            {
                MessageBox.Show("Por favor, ingrese una edad valida.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox.Clear();
            }
        }

        private void validarEstatura(object sender, EventArgs e)
        {
            TextBox textBox = (TextBox)sender;

            if (string.IsNullOrWhiteSpace(textBox.Text))
            {
                return; // No validar si está vacío
            }
            if (!EsDecimalValido(textBox.Text))
            {
                MessageBox.Show("Por favor, ingrese una Estatura valida.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox.Clear();
            }
        }

        private void validarTelefono(object sender, EventArgs e)
        {
            TextBox textBox = (TextBox)sender;
            if (string.IsNullOrWhiteSpace(textBox.Text))
            {
                return; // No validar si está vacío
            }

            // valida si el texto tiene 10 caracteres
            if (textBox.Text.Length == 10)
            {
                if (EsEnteroValido10Digitos(textBox.Text))
                {
                    textBox.BackColor = Color.Green; // Color válido
                }
                else
                {
                    textBox.BackColor = Color.Pink; // Color inválido
                    MessageBox.Show("Por favor, ingrese un número de teléfono válido.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    // No borres 
                }
            }
            else if (textBox.Text.Length > 10)
            {
                textBox.BackColor = Color.Pink;
                MessageBox.Show("El número de teléfono debe tener exactamente 10 dígitos.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                
            }
            else
            {
                textBox.BackColor = Color.White; 
            }
        }

        private void validarNombre(object sender, EventArgs e)
        {
            TextBox textBox = (TextBox)sender;
            if (string.IsNullOrWhiteSpace(textBox.Text))
            {
                return; // No validar si está vacío
            }
            if (!EsTextoValido(textBox.Text))
            {
                MessageBox.Show("Por favor, ingrese una nombre valido.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox.Clear();
            }

        }
        private void validarApellidos(object sender, EventArgs e)
        {
            TextBox textBox = (TextBox)sender;
            if (string.IsNullOrWhiteSpace(textBox.Text))
            {
                return; // No validar si está vacío
            }
            if (!EsTextoValido(textBox.Text))
            {
                MessageBox.Show("Por favor, ingrese una apellido valido.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox.Clear();
            }
        }

        private void btnLimpiar_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Datos borrados exitosamente");


            tbNombre.Clear();
            tbApellidos.Clear();
            tbTelefono.Clear();
            tbEdad.Clear();
            tbEstatura.Clear();
            rbHombre.Checked = false;
            rbMujer.Checked = false;

            tbNombre.BackColor = Color.White;
            tbApellidos.BackColor = Color.White;
            tbTelefono.BackColor = Color.White;
            tbEdad.BackColor = Color.White;
            tbEstatura.BackColor = Color.White;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
            
        }

        private void btnMinim_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }
    }
}
