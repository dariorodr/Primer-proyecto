(function () {
  
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
      btn.addEventListener('click', (e) => {
        const confirmacion = confirm('¿seguro que quieres borrar esto?');
        if (!confirmacion) {
          e.preventDefault();
        }
      });
    }); 

     
    
})();

