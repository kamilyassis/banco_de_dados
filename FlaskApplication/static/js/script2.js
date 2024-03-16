     // Adiciona um evento quando o modal é fechado
     $('#modalAdicionarLivro').on('hidden.bs.modal', function () {
        // Exibe a mensagem na página principal
        $('#mensagem-principal').text('Mensagem de exemplo').show();

        setTimeout(function(){
            window.location.href = response.redirect;
        }, 2000);
    });

    // Fecha o modal após 2 segundos (tempo em milissegundos)
    setTimeout(function(){
        $('#modalAdicionarLivro').modal('hide');
        $('#mensagem-principal').hide();
    }, 2000);