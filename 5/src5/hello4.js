document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {
        alert('hello, ' + document.querySelector('#name').value);
        return false;
    };
});
