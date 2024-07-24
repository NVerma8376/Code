let innerCursor = document.querySelector('.inner-cursor');
let outerCursor = document.querySelector('.outer-cursor');

document.addEventListener('mousemove', moveCursor);

function moveCursor(e) {
    let x = e.clientX;
    let y = e.clientY;

    innerCursor.style.left = `${x}px`;
    innerCursor.style.top = `${y}px`;
    outerCursor.style.left = `${x}px`;
    outerCursor.style.top = `${y}px`;

    checkBackgroundColor(e.target);
}

function checkBackgroundColor(element) {
    const whiteBackground = 'rgb(255, 255, 255)';
    const computedStyle = getComputedStyle(element);
    const backgroundColor = computedStyle.backgroundColor;

    if (backgroundColor === whiteBackground) {
        innerCursor.style.backgroundColor = 'white';
        outerCursor.style.borderColor = 'white';
    } else {
        innerCursor.style.backgroundColor = 'var(--cursor-color)';
        outerCursor.style.borderColor = 'var(--cursor-color)';
    }
}

const clickableElements = document.querySelectorAll('a, button, input[type="button"], input[type="submit"], [role="button"], [tabindex]:not([tabindex="-1"])');

clickableElements.forEach(element => {
    element.addEventListener('mouseover', () => {
        innerCursor.classList.add('grow');
        outerCursor.classList.add('grow');
    });
    element.addEventListener('mouseout', () => {
        innerCursor.classList.remove('grow');
        outerCursor.classList.remove('grow');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const menuButton = document.getElementById('menu-button');
    const sidebar = document.getElementById('sidebar');

    menuButton.addEventListener('click', function () {
        sidebar.classList.toggle('active');
    });
});

const rand = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

const enhance = id => {
  const element = document.getElementById(id),
        text = element.innerText.split("");
  
  element.innerText = "";
  
  text.forEach((value, index) => {
    const outer = document.createElement("span");
    
    outer.className = "outer";
    
    const inner = document.createElement("span");
    
    inner.className = "inner";
    
    inner.style.animationDelay = `${rand(-5000, 0)}ms`;
    
    const letter = document.createElement("span");
    
    letter.className = "letter";
    
    letter.innerText = value;
    
    letter.style.animationDelay = `${index * 1000 }ms`;
    
    inner.appendChild(letter);    
    
    outer.appendChild(inner);    
    
    element.appendChild(outer);
  });
}

enhance("channel-link");
enhance("different-text");
enhance("unique-text");

document.addEventListener('DOMContentLoaded', (event) => {
    console.log("Document loaded");
    // Logic for changing test questions added here
});