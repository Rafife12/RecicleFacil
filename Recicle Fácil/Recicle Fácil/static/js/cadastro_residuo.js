// JavaScript para o formulário de Cadastro de Resíduos

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('cadastro-residuo-form');

    form.addEventListener('submit', (event) => {
        const nome = document.getElementById('nome').value;
        const tipoResiduo = document.getElementById('tipo_residuo').value;
        const quantidade = document.getElementById('quantidade').value;

        if (!nome || !tipoResiduo || !quantidade) {
            event.preventDefault(); // Impede o envio se os campos estiverem vazios
            alert('Por favor, preencha todos os campos obrigatórios.');
        }

        if (quantidade <= 0) {
            event.preventDefault();
            alert('A quantidade deve ser maior que zero.');
        }
    });
});
