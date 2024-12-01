button_list = document.getElementsByClassName('cart-button');


for(button of button_list){
    button.addEventListener('click' ,(e) => {
        id = e.target.id;
        const formData = new FormData();
        formData.append('some_field', id);

        fetch('/update_model', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
        .then(response => {
            if (!response.ok) {
                // Handle HTTP errors
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            else{
                console.log("Model modified successfully !")
            }
        })
        
    })
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = cookies.length-1; i > 0; i--) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
