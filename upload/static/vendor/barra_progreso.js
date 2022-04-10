const uploadForm =  document.getElementById('upload-form')
const inputFile = document.getElementById('id_archivo')
console.log(inputFile)

const alertBox = document.getElementById('alert-box')
const progressBox = document.getElementById('progress-box')
const cancelBtn = document.getElementById('cancel-btn')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

$('#upload-form').submit(function(e){
    e.preventDefault();
    $form = $(this)
    var formData = new FormData(this);
    const media_data = inputFile.files[0];
    console.log(media_data)
    function getFileExtension3(filename) {
        return filename.slice((filename.lastIndexOf(".") - 1 >>> 0) + 2);
    }
    extension_data = getFileExtension3(media_data.name)

    $.ajax({
        type: 'POST',
        url: uploadForm.action,
        enctype: 'multipart/form-data',
        data: formData,
        dataType: 'json',
        beforeSend: function(){
            
        },
        xhr:function(){
            const xhr = new window.XMLHttpRequest();
            if(media_data != null && media_data.type == "application/octet-stream"){
                progressBox.classList.remove("visually-hidden")
                cancelBtn.classList.remove("visually-hidden")
                xhr.upload.addEventListener('progress', e=>{
                    if(e.lengthComputable){
                        const percentProgress = parseInt((e.loaded/e.total)*100)
                        console.log(percentProgress)
                        progressBox.innerHTML = `<div class="progress-bar progress-bar-striped progress-bar-animated bg-success" 
                        role="progressbar" style="width: ${percentProgress}%" aria-valuenow="${percentProgress}" aria-valuemin="0" 
                        aria-valuemax="100">${percentProgress}%</div>`
                    }
                })
            }
            cancelBtn.addEventListener('click', e=>{
                xhr.abort()
                progressBox.innerHTML=``
                progressBox.classList.add('visually-hidden')
                cancelBtn.classList.add('visually-hidden')
            })
            return xhr
        },

        success: function(response){
            alertBox.innerHTML=`<div class="alert alert-success" role="alert">El archivo se ha subido exitosamente</div>`
            setTimeout(() => {
                alertBox.innerHTML=""
            },4000)
            uploadForm.reset()
            progressBox.classList.add('visually-hidden')
            cancelBtn.classList.add('visually-hidden')
            
        },
        error: function(err){
            if(media_data.type != 'application/octet-stream'){
                alertBox.innerHTML=`<div class="alert alert-danger" role="alert">El archivo .${extension_data} no es permitido. Por favor ingresar solo archivos .bin</div>`
            }
            else{
                alertBox.innerHTML=`<div class="alert alert-danger" role="alert">Error: algo ha salido mal</div>`
            }
            setTimeout(() => {
                alertBox.innerHTML=""
                uploadForm.reset()
            },4000)
            
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

