// Function to convert FormData into a JSON object
function formToJson(form) {
    const formData = new FormData(form);
    const dataObject = {};

    formData.forEach((value, key) => {
        if (form.elements[key].type === 'checkbox') {
            dataObject[key] = form.elements[key].checked;
        } else {
            dataObject[key] = value;
        }
    });
    return dataObject;
    }

function handleSaveClick() {
    const form = document.getElementById('profileForm');
    const formDataJson = formToJson(form); // Pass the form element to the function
    const userId = formDataJson.id;

    if (!userId) {
        console.error("User ID is missing. Cannot perform PUT request.");
        alert("Error: User ID is missing.");
        return;
    }

    const endpointUrl = `/user/${userId}`;
    console.log("Data to be submitted:", formDataJson);

    fetch(endpointUrl, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formDataJson)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        alert('Profile updated successfully!');
    })
    .catch((error) => {
        console.error('Error during PUT request:', error);
        alert('Failed to update profile. Check the console for details.');
    });
}

// This ensures the DOM is fully loaded before trying to find the button
document.addEventListener('DOMContentLoaded', (event) => {
    const saveButton = document.getElementById('saveButton');
    if (saveButton) {
        saveButton.addEventListener('click', handleSaveClick);
        console.log('Event listener attached to saveButton.');
    } else {
        console.error('saveButton element not found!');
    }
});