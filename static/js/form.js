document.querySelector('form').onsubmit = function () {
    if (!document.querySelector('input').value){
        alert("you must provide name and email");
        return false;
    }
    else if (!document.querySelector('select').value){
        alert("you must provide dorm");
        return false;
    }
    return true;
    
};