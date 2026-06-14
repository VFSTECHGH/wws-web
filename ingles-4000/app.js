const textToRead = "El arte de la guerra es el mejor libro de estrategia de todos los tiempos. Inspiró a Napoleón, Maquiavelo, Mao Tse Tung y muchas más figuras históricas. Este libro de dos mil quinientos años de antigüedad, es uno de los más importantes textos clásicos chinos, en el que, a pesar del tiempo transcurrido, ninguna de sus máximas ha quedado anticuada, ni hay un solo consejo que hoy no sea útil. Pero la obra del general Sun Tzu no es únicamente un libro de práctica militar, sino un tratado que enseña la estrategia suprema de aplicar con sabiduría el conocimiento de la naturaleza humana en los momentos de confrontación.".split(" ");

const display = document.getElementById('rsvp-demo');
const btnPlay = document.getElementById('btn-play');
const btnFaster = document.getElementById('btn-faster');
const btnSlower = document.getElementById('btn-slower');
const wpmBadge = document.querySelector('.wpm-badge');
const progressFill = document.querySelector('.progress-fill');

let isPlaying = false;
let wpm = 400;
let currentIndex = 0;
let intervalId = null;

function updateDisplay() {
    if (currentIndex >= textToRead.length) {
        currentIndex = 0;
        pauseReading();
        return;
    }
    
    // Highlight the middle letter roughly
    const word = textToRead[currentIndex];
    const midIndex = Math.floor(word.length / 2);
    const before = word.slice(0, midIndex);
    const mid = word.charAt(midIndex);
    const after = word.slice(midIndex + 1);
    
    display.innerHTML = `${before}<span style="color: var(--accent);">${mid}</span>${after}`;
    
    progressFill.style.width = `${(currentIndex / textToRead.length) * 100}%`;
    currentIndex++;
}

function startReading() {
    if (intervalId) clearInterval(intervalId);
    const msPerWord = 60000 / wpm;
    intervalId = setInterval(updateDisplay, msPerWord);
    isPlaying = true;
    btnPlay.textContent = '⏸';
}

function pauseReading() {
    clearInterval(intervalId);
    isPlaying = false;
    btnPlay.textContent = '▶';
}

btnPlay.addEventListener('click', () => {
    if (isPlaying) {
        pauseReading();
    } else {
        startReading();
    }
});

btnFaster.addEventListener('click', () => {
    if (wpm < 1500) wpm += 50;
    wpmBadge.textContent = `${wpm} WPM`;
    if (isPlaying) startReading();
});

btnSlower.addEventListener('click', () => {
    if (wpm > 100) wpm -= 50;
    wpmBadge.textContent = `${wpm} WPM`;
    if (isPlaying) startReading();
});

// Init
updateDisplay();
