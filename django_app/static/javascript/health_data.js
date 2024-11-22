function toggleOptions(id) {
            var optionsDiv = document.getElementById(id);
            if (optionsDiv.style.display === "none") {
                optionsDiv.style.display = "block";
            } else {
                optionsDiv.style.display = "none";
            }
        }