document.getElementById('searchBtn').addEventListener('click', function() {
            const ticker = document.getElementById('tickerfield').value;
            const token = "{{token}}";

            if (ticker) {
                fetch(`https://brapi.dev/api/quote/list?search=${ticker}&token=${token}`)
                .then(response => response.json())
                .then(data => {
                    let resultDiv = document.getElementById('results');
                    resultDiv.innerHTML = '';

                    if (data && data.stocks && data.stocks.length > 0) {
                        data.stocks.forEach(stock => {
                            let stockInfo =
                                `<div style="display: flex; align-items: center; justify-content: space-around;">
                                    <p>${stock.type} / ${stock.sector}</p>
                                    <p>${stock.stock} - ${stock.name}: ${stock.close} (Último fechamento)</p>
                                     <button>Adicionar</button>
                                 </div>`;
                            resultDiv.innerHTML += stockInfo;
                        });
                    } else {
                        resultDiv.innerHTML = '<p>Nenhum resultado encontrado</p>';
                    }
                })
                .catch(error => {
                    console.error('Erro ao buscar ações:', error);
                });
            } else {
                alert('Por favor, insira um ticker!');
            }
        });