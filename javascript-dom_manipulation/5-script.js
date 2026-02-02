document.addEventListener('DOMContentLoaded', () => {
  const updateHeaderElement = document.querySelector('#update_header');
  
  updateHeaderElement.addEventListener('click', () => {
    const header = document.querySelector('header');
    header.textContent = 'New Header!!!';
  });
});
