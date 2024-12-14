// JavaScript para a validação do login

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('login-form');

    form.addEventListener('submit', (event) => {
        const email = document.getElementById('email').value;
        const senha = document.getElementById('senha').value;

        if (!email || !senha) {
            event.preventDefault(); // Impede o envio se os campos estiverem vazios
            alert('Por favor, preencha todos os campos.');
        }
    });
});
