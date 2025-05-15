

    // SCRIP DE LA BARRA DE NAVEGACIÓN
    const hamburguesa = document.querySelector('.hamburguesa');
  const navLinks = document.querySelector('.nav-links');
  let timeoutId;

  // Menú hamburguesa
  hamburguesa.addEventListener('click', (e) => {
      e.stopPropagation();
      navLinks.classList.toggle('active');
      hamburguesa.classList.toggle('active');
  });

  // Control dropdowns
  document.querySelectorAll('.dropdown-toggle').forEach(item => {
      item.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          
          const dropdown = e.target.closest('.dropdown-parent');
          const wasActive = dropdown.classList.contains('active');
          
          // Cerrar todos los dropdowns
          document.querySelectorAll('.dropdown-parent').forEach(d => d.classList.remove('active'));
          
          // Toggle solo si no estaba activo
          if (!wasActive) {
              dropdown.classList.add('active');
              if (window.innerWidth <= 768) {
                  dropdown.querySelector('.dropdown-menu').style.display = 'block';
              }
          }
      });
  });

  // Cerrar menús al hacer clic fuera
  document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav-links')) {
          navLinks.classList.remove('active');
          hamburguesa.classList.remove('active');
          document.querySelectorAll('.dropdown-parent').forEach(d => d.classList.remove('active'));
      }
  });

  // Cerrar al seleccionar opción (mobile)
  document.querySelectorAll('.dropdown-menu a').forEach(link => {
      link.addEventListener('click', (e) => {
          if (window.innerWidth <= 768) {
              navLinks.classList.remove('active');
              hamburguesa.classList.remove('active');
              link.closest('.dropdown-parent').classList.remove('active');
          }
      });
  });