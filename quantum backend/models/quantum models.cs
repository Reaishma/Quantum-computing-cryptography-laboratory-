
namespace QuantumLab.API.Models
{
    public class QuantumCircuit
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public List<string> Gates { get; set; } = new();
        public string State { get; set; } = "|0⟩";
        public int Qubits { get; set; }
        public double Fidelity { get; set; }
        public double Entanglement { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    }

    public class QuantumKey
    {
        public string KeyId { get; set; } = string.Empty;
        public string SharedKey { get; set; } = string.Empty;
        public int KeyLength { get; set; }
        public double ErrorRate { get; set; }
        public string Protocol { get; set; } = "BB84";
        public DateTime GeneratedAt { get; set; } = DateTime.UtcNow;
    }

    public class Molecule
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public List<Atom> Atoms { get; set; } = new();
        public List<Bond> Bonds { get; set; } = new();
        public double Temperature { get; set; }
        public double Pressure { get; set; }
    }

    public class Atom
    {
        public int Id { get; set; }
        public string Symbol { get; set; } = string.Empty;
        public double X { get; set; }
        public double Y { get; set; }
        public string Color { get; set; } = string.Empty;
    }

    public class Bond
    {
        public int Id { get; set; }
        public double X1 { get; set; }
        public double Y1 { get; set; }
        public double Length { get; set; }
        public double Angle { get; set; }
    }

    public class QuantumRandomResult
    {
        public string Binary { get; set; } = string.Empty;
        public long Decimal { get; set; }
        public string Hex { get; set; } = string.Empty;
        public int Bits { get; set; }
    }

    public class AttackSimulation
    {
        public string Protocol { get; set; } = string.Empty;
        public double SuccessRate { get; set; }
        public double DetectionRate { get; set; }
        public string Description { get; set; } = string.Empty;
    }
}
