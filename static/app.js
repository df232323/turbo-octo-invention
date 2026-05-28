document.getElementById('applicationForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);
    
    const response = await fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    
    if (response.ok) {
        const result = await response.json();
        document.getElementById('trackCode').textContent = result.track_code;
        document.getElementById('successScreen').style.display = 'flex';
    }
});

document.querySelectorAll('.device-card').forEach(card => {
    card.addEventListener('click', function() {
        document.querySelectorAll('.device-card').forEach(c => c.classList.remove('active'));
        this.classList.add('active');
    });
});
