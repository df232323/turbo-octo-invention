const form = document.getElementById("applicationForm");
const successScreen = document.getElementById("successScreen");
const trackCode = document.getElementById("trackCode");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = {
        fio: form.fio.value,
        birth: form.birth.value,
        phone: form.phone.value,
        telegram: form.telegram.value,
        experience: form.experience.value,
        time: form.time.value,
device: document.querySelector('input[name="device"]:checked').value
    };

    try {

        const response = await fetch("/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        trackCode.textContent = data.track_code;

        successScreen.style.display = "flex";

    } catch (error) {

        alert("Ошибка отправки заявки");

    }
});
