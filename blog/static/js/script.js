(function() {
    // Disable right-click
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        alert('Right-click is disabled on this site.');
    });

    // Disable F12, Ctrl+U, Ctrl+Shift+I, and Ctrl+Shift+J (Developer Tools and View Source)
    document.addEventListener('keydown', function(e) {
        if (e.key === 'F12' || 
            (e.ctrlKey && (e.key === 'U' || e.key === 'I' || e.key === 'J')) || 
            (e.shiftKey && e.ctrlKey && (e.key === 'I' || e.key === 'J'))) {
            e.preventDefault();
            alert('Viewing source code is disabled.');
        }
    });

    // Hide the view source and inspect element context menu options
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        if (e.target.tagName === 'IMG') {
            e.stopPropagation();
        }
    });

    // Obfuscate code example: minimal obfuscation for demonstration purposes
    function obfuscatedFunction() {
        console.log('This is an obfuscated function.');
    }
    obfuscatedFunction();

    // Use strict mode
    'use strict';

    // Add a function to handle page load events
    window.addEventListener('load', function() {
        console.log('Page loaded');
    });

    // Example of a function to dynamically modify page content
    function modifyPageContent() {
        var header = document.querySelector('h1');
        if (header) {
            header.innerText = 'Welcome to CACO!';
        }
    }
    modifyPageContent();
})();
