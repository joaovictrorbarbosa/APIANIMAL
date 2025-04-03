function carregarAnimais(){
    axios.get('http://127.0.0.1:8086/animais').then(response => console.log(response.data))


}


function app(){
    console.log('App Iniciada')
    carregarAnimais()
}

app()