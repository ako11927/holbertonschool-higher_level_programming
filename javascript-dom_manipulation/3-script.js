document.addEventListener('DOMContentLoaded', () => {
  const toggleHeaderElement = document.querySelector('#toggle_header');
  
  toggleHeaderElement.addEventListener('click', () => {
    const header = document.querySelector('header');
    
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      header.classList.remove('green');
      header.classList.add('red');
    }
  });
});
