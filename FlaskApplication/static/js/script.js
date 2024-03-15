function exibirPopup(mensagem){
    var popupElement = document.getElementById('mensagem-popup');
    popupElement.innerHTML = mensagem; // Define o conteúdo da mensagem no pop-up
    popupElement.style.display = 'block'; // Exibe o pop-up

    // Define um timer para esconder o pop-up após alguns segundos
    setTimeout(function() {
        popupElement.style.display = 'none'; // Esconde o pop-up após 3 segundos
    }, 3000);
}

document.getElementById('formulario-livro').addEventListener('submit',function(event){
    event.preventDefault(); // Evitar o envio padrão do formulário

    var formulario = this;
    var formData = new  FormData(formulario);

    fetch('/adicionar_livro',{
        method:'POST',
        body: formData
    })

    .then(response => response.json())
    .then(data => {
        if (data.mensagem){
            exibirPopup(data.mensagem)
        } else if (data.redirect){
            window.location.href = data.redirect;
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});
