let key ="96618441b12bde6ad128ec3d325cfba5"

function putdados(dados){
    document.querySelector(".city").innerHTML= "Tempo em " + dados.name
    document.querySelector(".temp").innerHTML = dados.main.temp
    document.querySelector(".statu-temp").innerHTML  = dados.weather[0].description
    document.querySelector(".umid").innerHTML  = dados.main.humidity
    document.querySelector(".s-img").src = `https://openweathermap.org/img/wn/${dados.weather[0].icon}.png`
}
async function buscarcity(city){
    let dados  = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${key}`).then(resposta => resposta.json())
    putdados(dados)
}

function clickbottom(){
    let city = document.querySelector(".bus-city").value
    
    buscarcity(city)
}



