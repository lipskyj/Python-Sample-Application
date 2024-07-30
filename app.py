<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generador de Cuentos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #333;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        #story {
            margin-top: 20px;
            border: 1px solid #ddd;
            padding: 10px;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Generador de Cuentos</h1>
    <p>Ingrese 5 palabras separadas por comas:</p>
    <input type="text" id="words" placeholder="luna, gato, bosque, magia, sueño">
    <button onclick="generateStory()">Generar Cuento</button>
    <div id="story"></div>

    <script>
        async function generateStory() {
            const wordsInput = document.getElementById('words');
            const storyDiv = document.getElementById('story');
            const words = wordsInput.value.split(',').map(word => word.trim());

            if (words.length !== 5) {
                storyDiv.innerHTML = '<p style="color: red;">Por favor, ingrese exactamente 5 palabras.</p>';
                return;
            }

            storyDiv.innerHTML = '<p>Generando cuento...</p>';

            try {
                const response = await fetch('/generar-cuento', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ palabras: words }),
                });

                if (!response.ok) {
                    throw new Error('Error en la respuesta del servidor');
                }

                const data = await response.json();
                storyDiv.innerHTML = `<p>${data.cuento}</p>`;
            } catch (error) {
                storyDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
            }
        }
    </script>
</body>
</html>
