
using Microsoft.AspNetCore.Mvc;
using QuantumLab.API.Models;
using System.Security.Cryptography;
using System.Text;

namespace QuantumLab.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class CryptographyController : ControllerBase
    {
        private static List<QuantumKey> _keys = new();

        [HttpPost("qkd/start")]
        public ActionResult<QuantumKey> StartQKD([FromBody] QKDRequest request)
        {
            var key = new QuantumKey
            {
                KeyId = Guid.NewGuid().ToString(),
                KeyLength = request.KeyLength,
                SharedKey = GenerateRandomBits(request.KeyLength),
                ErrorRate = new Random().NextDouble() * 5,
                Protocol = "BB84"
            };

            _keys.Add(key);
            return Ok(key);
        }

        [HttpPost("qrng/generate")]
        public ActionResult<QuantumRandomResult> GenerateQuantumRandom([FromBody] QRNGRequest request)
        {
            var binary = GenerateRandomBits(request.Bits);
            var decimal_val = Convert.ToInt64(binary.Substring(0, Math.Min(32, binary.Length)), 2);
            var hex = decimal_val.ToString("X");

            return Ok(new QuantumRandomResult
            {
                Binary = binary,
                Decimal = decimal_val,
                Hex = hex,
                Bits = request.Bits
            });
        }

        [HttpPost("pqc/encrypt")]
        public ActionResult<PQCResult> EncryptPQC([FromBody] PQCRequest request)
        {
            var encrypted = Convert.ToBase64String(
                Encoding.UTF8.GetBytes($"{request.Message}_{request.Algorithm}")
            );

            return Ok(new PQCResult
            {
                Encrypted = encrypted,
                Algorithm = request.Algorithm
            });
        }

        [HttpPost("pqc/decrypt")]
        public ActionResult<PQCResult> DecryptPQC([FromBody] PQCDecryptRequest request)
        {
            try
            {
                var decoded = Encoding.UTF8.GetString(Convert.FromBase64String(request.Encrypted));
                var message = decoded.Split('_')[0];

                return Ok(new PQCResult
                {
                    Decrypted = message,
                    Algorithm = request.Algorithm
                });
            }
            catch
            {
                return BadRequest("Decryption failed");
            }
        }

        [HttpGet("keys")]
        public ActionResult<IEnumerable<QuantumKey>> GetKeys()
        {
            return Ok(_keys);
        }

        private string GenerateRandomBits(int length)
        {
            var random = new Random();
            var result = new StringBuilder();

            for (int i = 0; i < length; i++)
            {
                result.Append(random.Next(2));
            }

            return result.ToString();
        }
    }

    public class QKDRequest
    {
        public int KeyLength { get; set; } = 256;
    }

    public class QRNGRequest
    {
        public int Bits { get; set; } = 128;
    }

    public class PQCRequest
    {
        public string Message { get; set; } = string.Empty;
        public string Algorithm { get; set; } = "CRYSTALS-Kyber";
    }

    public class PQCDecryptRequest
    {
        public string Encrypted { get; set; } = string.Empty;
        public string Algorithm { get; set; } = "CRYSTALS-Kyber";
    }

    public class PQCResult
    {
        public string Encrypted { get; set; } = string.Empty;
        public string Decrypted { get; set; } = string.Empty;
        public string Algorithm { get; set; } = string.Empty;
    }
}
