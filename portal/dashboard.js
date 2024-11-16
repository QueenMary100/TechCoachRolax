document.getElementById("generateLinkBtn").addEventListener("click", function() {
    const generatedLink = `https://meet.google.com/${Math.random().toString(36).substring(7)}`;
    document.getElementById("meetLink").innerHTML = `
      <strong>Your Google Meet Link:</strong> 
      <a href="${generatedLink}" target="_blank">${generatedLink}</a>
    `;
  });
  document.getElementById('nextContentBtn').addEventListener('click', function () {
    // Show the hidden content
    document.getElementById('moreContent').style.display = 'block';
    // Hide the button
    this.style.display = 'none';
});