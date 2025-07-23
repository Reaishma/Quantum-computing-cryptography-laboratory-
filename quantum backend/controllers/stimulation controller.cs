
using Microsoft.AspNetCore.Mvc;
using QuantumLab.API.Models;

namespace QuantumLab.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class SimulationController : ControllerBase
    {
        private static List<Molecule> _molecules = new();

        [HttpGet("molecules")]
        public ActionResult<IEnumerable<Molecule>> GetMolecules()
        {
            return Ok(_molecules);
        }

        [HttpPost("molecules/generate")]
        public ActionResult<Molecule> GenerateMolecule([FromBody] MoleculeRequest request)
        {
            var molecule = request.Type?.ToLower() switch
            {
                "h2o" => GenerateH2O(),
                "co2" => GenerateCO2(),
                "nh3" => GenerateNH3(),
                _ => GenerateRandomMolecule()
            };

            molecule.Temperature = request.Temperature;
            molecule.Pressure = request.Pressure;
            _molecules.Add(molecule);

            return Ok(molecule);
        }

        [HttpPost("attacks/simulate")]
        public ActionResult<AttackSimulation> SimulateAttack([FromBody] AttackRequest request)
        {
            var random = new Random();
            var successRate = random.NextDouble() * 100;
            var detectionRate = 100 - successRate + random.NextDouble() * 20;

            return Ok(new AttackSimulation
            {
                Protocol = request.Protocol,
                SuccessRate = Math.Round(successRate, 2),
                DetectionRate = Math.Round(detectionRate, 2),
                Description = GetAttackDescription(request.Protocol)
            });
        }

        private Molecule GenerateH2O()
        {
            return new Molecule
            {
                Id = _molecules.Count + 1,
                Name = "H2O",
                Atoms = new List<Atom>
                {
                    new Atom { Id = 1, Symbol = "O", X = 200, Y = 180, Color = "#ff4757" },
                    new Atom { Id = 2, Symbol = "H", X = 150, Y = 150, Color = "#00d4ff" },
                    new Atom { Id = 3, Symbol = "H", X = 250, Y = 150, Color = "#00d4ff" }
                }
            };
        }

        private Molecule GenerateCO2()
        {
            return new Molecule
            {
                Id = _molecules.Count + 1,
                Name = "CO2",
                Atoms = new List<Atom>
                {
                    new Atom { Id = 1, Symbol = "C", X = 200, Y = 180, Color = "#2f3542" },
                    new Atom { Id = 2, Symbol = "O", X = 150, Y = 180, Color = "#ff4757" },
                    new Atom { Id = 3, Symbol = "O", X = 250, Y = 180, Color = "#ff4757" }
                }
            };
        }

        private Molecule GenerateNH3()
        {
            return new Molecule
            {
                Id = _molecules.Count + 1,
                Name = "NH3",
                Atoms = new List<Atom>
                {
                    new Atom { Id = 1, Symbol = "N", X = 200, Y = 180, Color = "#3742fa" },
                    new Atom { Id = 2, Symbol = "H", X = 170, Y = 150, Color = "#00d4ff" },
                    new Atom { Id = 3, Symbol = "H", X = 230, Y = 150, Color = "#00d4ff" },
                    new Atom { Id = 4, Symbol = "H", X = 200, Y = 220, Color = "#00d4ff" }
                }
            };
        }

        private Molecule GenerateRandomMolecule()
        {
            var molecules = new[] { GenerateH2O(), GenerateCO2(), GenerateNH3() };
            return molecules[new Random().Next(molecules.Length)];
        }

        private string GetAttackDescription(string protocol)
        {
            return protocol switch
            {
                "BB84 Intercept-Resend" => "Eavesdropper intercepts and retransmits quantum bits",
                "Man-in-the-Middle" => "Attacker positions between communicating parties",
                "Photon Number Splitting" => "Exploits multi-photon pulses in quantum transmission",
                "Trojan Horse" => "Injects additional light pulses to extract information",
                _ => "Unknown attack protocol"
            };
        }
    }

    public class MoleculeRequest
    {
        public string Type { get; set; } = "random";
        public double Temperature { get; set; } = 300;
        public double Pressure { get; set; } = 1;
    }

    public class AttackRequest
    {
        public string Protocol { get; set; } = "BB84 Intercept-Resend";
    }
}
