// Validação do formulário e envio
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('cadastro-form');

    form.addEventListener('submit', (event) => {
        const senha = document.getElementById('senha').value;
        const confirmarSenha = document.getElementById('confirmar_senha').value;

        if (senha !== confirmarSenha) {
            event.preventDefault(); // Impede o envio do formulário
            alert('As senhas não coincidem. Por favor, verifique.');
        }
    });
});
