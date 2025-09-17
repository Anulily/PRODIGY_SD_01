async function convertTemp() {
  const tempValue = document.getElementById("tempValue").value;
  const unit = document.getElementById("unit").value;
  const resultDiv = document.getElementById("result");

  if (!tempValue) {
    resultDiv.innerHTML = "⚠️ Please enter a valid temperature!";
    resultDiv.classList.add("show");
    return;
  }

  const response = await fetch("/convert", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ temperature: tempValue, unit: unit })
  });

  const data = await response.json();

  resultDiv.innerHTML = `
    🌡 <b>Converted Values:</b><br>
    Celsius: ${data.celsius} °C<br>
    Fahrenheit: ${data.fahrenheit} °F<br>
    Kelvin: ${data.kelvin} K
  `;
  resultDiv.classList.add("show");
}
