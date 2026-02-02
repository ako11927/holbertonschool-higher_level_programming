document.addEventListener('DOMContentLoaded', () => {
  const redHeaderElement = document.querySelector('#red_header');
  
  redHeaderElement.addEventListener('click', () => {
    const header = document.querySelector('header');
    header.classList.add('red');
  });
});
