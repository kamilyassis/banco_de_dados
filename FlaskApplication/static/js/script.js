$(document).ready(function() {
    $('#formulario-livro').submit(function(event) {
        event.preventDefault(); // Evitar o envio padrão do formulário

        var formData = new FormData(this);

        fetch('/adicionar_livro', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            var mensagemBox = document.getElementById('mensagem-box');
            var mensagemTexto = document.getElementById('mensagem-texto');
            if (data.mensagem) {
                mensagemTexto.textContent = data.mensagem;
                mensagemBox.classList.remove('alert-danger');
                mensagemBox.classList.add('alert-success');
            } else {
                mensagemTexto.textContent = 'Erro ao adicionar livro.';
                mensagemBox.classList.remove('alert-success');
                mensagemBox.classList.add('alert-danger');
            }
            mensagemBox.style.display = 'block';
            $('#modalAdicionarLivro').modal('hide'); // Fechar o modal após processar o formulário
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    });
});
