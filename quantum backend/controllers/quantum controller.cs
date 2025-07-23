
using Microsoft.AspNetCore.Mvc;
using QuantumLab.API.Models;

namespace QuantumLab.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class QuantumController : ControllerBase
    {
        private static List<QuantumCircuit> _circuits = new();
        private static int _circuitIdCounter = 1;

        [HttpGet("circuits")]
        public ActionResult<IEnumerable<QuantumCircuit>> GetCircuits()
        {
            return Ok(_circuits);
        }

        [HttpGet("circuits/{id}")]
        public ActionResult<QuantumCircuit> GetCircuit(int id)
        {
            var circuit = _circuits.FirstOrDefault(c => c.Id == id);
            if (circuit == null)
                return NotFound();
            
            return Ok(circuit);
        }

        [HttpPost("circuits")]
        public ActionResult<QuantumCircuit> CreateCircuit([FromBody] QuantumCircuit circuit)
        {
            circuit.Id = _circuitIdCounter++;
            circuit.CreatedAt = DateTime.UtcNow;
            circuit.Fidelity = 0.9 + new Random().NextDouble() * 0.1;
            circuit.Entanglement = new Random().NextDouble();
            
            _circuits.Add(circuit);
            return CreatedAtAction(nameof(GetCircuit), new { id = circuit.Id }, circuit);
        }

        [HttpPut("circuits/{id}")]
        public ActionResult<QuantumCircuit> UpdateCircuit(int id, [FromBody] QuantumCircuit circuit)
        {
            var existingCircuit = _circuits.FirstOrDefault(c => c.Id == id);
            if (existingCircuit == null)
                return NotFound();

            existingCircuit.Name = circuit.Name;
            existingCircuit.Gates = circuit.Gates;
            existingCircuit.State = circuit.State;
            existingCircuit.Qubits = circuit.Qubits;
            
            return Ok(existingCircuit);
        }

        [HttpDelete("circuits/{id}")]
        public ActionResult DeleteCircuit(int id)
        {
            var circuit = _circuits.FirstOrDefault(c => c.Id == id);
            if (circuit == null)
                return NotFound();

            _circuits.Remove(circuit);
            return NoContent();
        }

        [HttpPost("circuits/{id}/execute")]
        public ActionResult<QuantumCircuit> ExecuteCircuit(int id)
        {
            var circuit = _circuits.FirstOrDefault(c => c.Id == id);
            if (circuit == null)
                return NotFound();

            // Simulate quantum state evolution
            var states = new[] { "|0⟩", "|1⟩", "|+⟩", "|-⟩", "|00⟩", "|01⟩", "|10⟩", "|11⟩" };
            circuit.State = states[new Random().Next(states.Length)];
            circuit.Fidelity = 0.9 + new Random().NextDouble() * 0.1;
            circuit.Entanglement = new Random().NextDouble();

            return Ok(circuit);
        }
    }
}
