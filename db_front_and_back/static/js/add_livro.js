function adicionar_livro() {
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const genero = document.getElementById('genero').value;

    const formData = new FormData();
    formData.append('titulo', titulo);
    formData.append('autor', autor);
    formData.append('genero', genero);

    fetch('/api/adicionar_livro', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Livro cadastrado com sucesso.');
            document.getElementById('titulo').value = '';
            document.getElementById('autor').value = '';
            document.getElementById('genero').value = '';
        } else {
            alert('Erro ao cadastrar o livro.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro de conexão com o servidor.');
    });
}
