function controllaTipoDispositivo(){
    // Rileva se il dispositivo è un telefono
    var isTelefono = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

    // Modifica dinamicamente il contenuto in base al tipo di dispositivo
    if (isTelefono) {
        window.location.href = 'NotAvailable/';
    }
    if(window.innerWidth <= 1280){
        alert("error! per accedere a questo sito devi avere più di 1280px di larghezza!")
        window.location.href = 'NotAvailable/';
    }
}



















