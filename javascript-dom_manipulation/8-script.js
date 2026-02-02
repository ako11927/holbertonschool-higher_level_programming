// Using async/await syntax for cleaner code
document.addEventListener('DOMContentLoaded', async () => {
  const helloElement = document.querySelector('#hello');
  
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    const data = await response.json();
    helloElement.textContent = data.hello;
  } catch (error) {
    console.error('Error fetching translation:', error);
    helloElement.textContent = 'Error loading translation';
  }
});
