document.getElementById('btnAbrirModal').addEventListener('click', function() {
    document.getElementById('addLivroModal').classList.add('modal-open');
  });
  

  function enviarFormulario() {
    const form = document.getElementById('addLivroForm');
    const formDataAddLivro = new FormData(form);

    fetch('/api/adicionar_livro', {
        method: 'POST',
        body: formDataAddLivro
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Livro cadastrado com sucesso.');
            closeModal(); // Fechar o modal após cadastrar o livro
        } else {
            alert('Erro ao cadastrar o livro.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro de conexão com o servidor.');
    });
}

document.getElementById('btnSalvarLivro').addEventListener('click', function() {
    enviarFormulario();
});


function closeModal() {
    document.getElementById('addLivroModal').classList.remove('modal-open');
    // Limpar os campos do formulário após fechar o modal, se necessário
    document.getElementById('autorInput').value = '';
    document.getElementById('tituloInput').value = '';
    document.getElementById('generoInput').value = '';
}
