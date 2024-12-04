document.getElementById('upload-btn').addEventListener('click', function() {
    // Dispara el evento de click en el input file oculto
    document.getElementById('file-input').click();
});

document.getElementById('file-input').addEventListener('change', function(event) {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
        console.log("Archivo seleccionado: " + selectedFile.name);
        // Puedes hacer otras cosas con el archivo seleccionado aquí
    }
});




