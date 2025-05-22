const input = document.getElementById('imagem');
const previewImage = document.getElementById('preview-image');

input.addEventListener('change', () => {
    const file = input.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = e => {
            previewImage.src = e.target.result;
            previewImage.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});