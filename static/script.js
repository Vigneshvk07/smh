document.getElementById('startButton').addEventListener('click', function() {
    const resultDiv = document.getElementById('result');
    resultDiv.innerText = 'Loading...';
    
    fetch('/get_information', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'moisture': '40',
            'pH': '6.5',
            'temperature': '25',
            'ec': '1.2',
            'npk': '10-20-15'
        })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerText = 'Recommendation: ' + data.recommendation;
    })
    .catch(error => {
        resultDiv.innerText = 'Error fetching data';
        console.error('Error:', error);
    });
});
