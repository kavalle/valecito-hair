
console.log('aqui')

fetch('http://127.0.0.1:8000/api/reservas')
  .then(response => response.json())
  .then(response => {
    // TODO pintar en front
    console.log(response);
  })
  .catch(console.error)


fetch('https://mindicador.cl/api')
  .then(response => response.json())
  .then(response => {
    // TODO pintar en front
    const $book = document.createElement('div')
    $book.className = 'dolar'
    $book.textContent = `El valor del dolar hoy es: $${response.dolar_intercambio.valor}`
    document.body.appendChild($book)
  })
  .catch(console.error)
