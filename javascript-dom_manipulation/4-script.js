document.addEventListener('DOMContentLoaded', () => {
  const addItemElement = document.querySelector('#add_item');
  
  addItemElement.addEventListener('click', () => {
    const list = document.querySelector('.my_list');
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });
});
