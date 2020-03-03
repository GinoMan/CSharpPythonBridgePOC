using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using net.r_eg.DllExport;
using net.r_eg.Conari.Types;
using System.Runtime.InteropServices;

namespace CSharp_To_Python_Proof_of_Concept
{
	public class Functions
    {
		[DllExport]
		public static int safeMessageBox ([MarshalAs(UnmanagedType.LPWStr)] string title, [MarshalAs(UnmanagedType.LPWStr)] string text)
		{
			return (int)MessageBox.Show(text, title, MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
		}
    }
}
