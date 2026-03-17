using System;
using System.Runtime.Versioning;
namespace API.Processador
{
    class Processador
    {
        private string sem_a(String s)
        {
            s = s.Replace("a", "b");
            s = s.Replace("A", "B");

            return s;
        }   

        private string inverter(String s)
        {
            char[] chars = s.ToCharArray();
            Array.Reverse(chars);
            string inv = new string(chars);
            return inv;
        }

        public string transform(string s)
        {
            s = sem_a(s);
            s = inverter(s);
            return s;
        }
    }
}

