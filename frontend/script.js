document.addEventListener('DOMContentLoaded', function () {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('pdfFileInput');
    const userIdInput = document.getElementById('userId');
    const userEmailInput = document.getElementById('userEmail');
    const messageDiv = document.getElementById('message');
    const pdfPreview = document.getElementById('pdfPreview');
    const clearPdfBtn = document.getElementById('clearPdfBtn');

    clearPdfBtn.addEventListener('click', function () {
        pdfPreview.src = ''; // Clear the PDF preview
        fileInput.value = ''; // Clear the file input
        uploadForm.reset();
        messageDiv.innerHTML = ''; // Clear any error message
    });

    fileInput.addEventListener('change', function () {
        const file = fileInput.files[0];
        if (file && file.type === 'application/pdf') {
            const reader = new FileReader();
            reader.onload = function (e) {
                pdfPreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        } else {
            // Not a PDF file
            pdfPreview.src = '';
            messageDiv.innerHTML = '<p style="color: red;">Please select a valid PDF file.</p>';
        }
    });

    uploadForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const userId = userIdInput.value.trim();
        const userEmail = userEmailInput.value.trim();
        const file = fileInput.files[0];

        if (!userId || !userEmail) {
            messageDiv.innerHTML = '<p class="text-danger">Please fill out both User ID and Email.</p>';
            return;
        }

        // Additional validation for email format (can be more thorough)
        if (!isValidEmail(userEmail)) {
            messageDiv.innerHTML = '<p class="text-danger">Please enter a valid email address.</p>';
            return;
        }

        if (file && file.type === 'application/pdf') {
            // Valid PDF file
            messageDiv.innerHTML = '';
            const formData = new FormData();
            formData.append('user_id', userId)
            formData.append('user_email', userEmail)
            formData.append('file', fileInput.files[0])

                // Display formData for debugging (optional)
                for (var pair of formData.entries()) {
                    console.log(pair[0]+ ', ' + pair[1]);
                }

                fetch('/api/v1/upload', {
                    method: 'POST',
                    body: formData
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Success:', data);
                    messageDiv.innerHTML = '<p class="text-success">' + data.message + '</p>';
                })
                .catch((error) => {
                    console.error('Error:', error);
                    messageDiv.innerHTML = '<p class="text-danger">Error uploading file. Please try again.</p>';
                });
        } else {
            // Not a PDF file
            messageDiv.innerHTML = '<p style="color: red;">Please upload a valid PDF file.</p>';
        }
    });

    function uploadFile(file) {
        // File upload logic...
        // This part remains the same as in the previous example
    }

    function isValidEmail(email) {
        // Simple email validation, can be more thorough based on requirements
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }
});
