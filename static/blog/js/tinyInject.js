fetch('/get-tinymce-api-key/', {
    credentials: 'same-origin'  // Include credentials with the request
})
.then(response => response.json())
.then(data => {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = `https://cdn.tiny.cloud/1/${data.api_key}/tinymce/7/tinymce.min.js`;
    document.head.appendChild(script);

    script.onload = function() {
        tinymce.init({
            selector: "#id_content",
            height: 656,
            plugins: [
                'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak',
                'searchreplace', 'wordcount', 'visualblocks', 'code', 'fullscreen', 'insertdatetime', 'media',
                'table', 'emoticons', 'help'
            ],
            toolbar: 'undo redo | styleselect | fontselect | styles | bold italic | alignleft aligncenter alignright alignjustify | ' +
                'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
                'forecolor backcolor emoticons | help',
            menu: {
                favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
            },
            menubar: 'favs file edit view insert format tools table help',
        });
    };
})
.catch(error => console.error('Error fetching the API key:', error));