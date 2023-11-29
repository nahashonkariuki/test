// Add JavaScript for enhanced functionality
function uploadImage() {
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];
  
    if (!file) {
      alert("Please select an image file.");
      return;
    }
  
    const formData = new FormData();
    formData.append("file", file);
  
    fetch("/upload", {
      method: "POST",
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      const resultText = document.getElementById("resultText");
      resultText.innerText = `Classification result: ${data.result}`;
    })
    .catch(error => {
      console.error("Error:", error);
    });
}

// Add additional JavaScript functions based on the suggested functionality
