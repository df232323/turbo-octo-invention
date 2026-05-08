async function sendForm() {

    const data = {
        name: document.getElementById('name').value,
        age: document.getElementById('age').value,
        phone: document.getElementById('phone').value,
        telegram: document.getElementById('telegram').value,
        experience: document.getElementById('experience').value,
        hours: document.getElementById('hours').value,
    }

    const response = await fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    const result = await response.json()

    document.getElementById('success').innerHTML = `
        <div style="margin-top:20px;">
            ✅ Заявка отправлена<br><br>
            Ваш HR-код:<br>
            <span style="font-size:42px;font-weight:700;">
                ${result.track_code}
            </span>
        </div>
    `
}
