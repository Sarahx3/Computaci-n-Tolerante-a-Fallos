const list = document.querySelector('ul');
const titleInput = document.querySelector('#title');
const bodyInput = document.querySelector('#body');
const form = document.querySelector('form');
const submitBtn = document.querySelector('form button');

let db;

window.onload = function() {
    // abre o crea DB
    let request = window.indexedDB.open('myNotes', 1);

    request.onerror = function() {
        console.log('No se pudo abrir la base de datos');
    };

    request.onsuccess = function() {
        console.log('Base de datos abierta');
        db = request.result;

        displayData();
    };

    //crear tablas de la db si no están hechas
    request.onupgradeneeded = function(e) {

        let db = e.target.result;

        // crear tabla vacia
        let objectStore = db.createObjectStore('notes_os', { keyPath: 'id', autoIncrement:true });

        objectStore.createIndex('title', 'title', { unique: false });
        objectStore.createIndex('body', 'body', { unique: false });

        console.log('configuracion completa');
    };

    //click a agregar nota
    form.onsubmit = addData;

    function addData(e) {
        e.preventDefault();

        //crear objeto con los datos de los input
        let newItem = { title: titleInput.value, body: bodyInput.value };

        //abrir modo lectura/escritura
        let transaction = db.transaction(['notes_os'], 'readwrite');

        let objectStore = transaction.objectStore('notes_os');

        var request = objectStore.add(newItem);
        request.onsuccess = function() {
            titleInput.value = '';
            bodyInput.value = '';
        };

        transaction.oncomplete = function() {
        console.log('Transacción completada');

        displayData();
        };

        transaction.onerror = function() {
        console.log('Error en transacción');
        };
    }

    function displayData() {
        while (list.firstChild) {
        list.removeChild(list.firstChild);
        }

        let objectStore = db.transaction('notes_os').objectStore('notes_os');
        objectStore.openCursor().onsuccess = function(e) {
            let cursor = e.target.result;

            if(cursor) {
                const listItem = document.createElement('li');
                const h3 = document.createElement('h3');
                const text = document.createElement('p');

                listItem.appendChild(h3);
                listItem.appendChild(text);
                list.appendChild(listItem);

                h3.textContent = cursor.value.title;
                text.textContent = cursor.value.body;

                listItem.setAttribute('data-note-id', cursor.value.id);

                //crear boton eliminar
                const deleteBtn = document.createElement('button');
                listItem.appendChild(deleteBtn);
                deleteBtn.textContent = 'Eliminar';

                deleteBtn.onclick = deleteItem;

                //Ir al siguiente objeto de la lista
                cursor.continue();
            } else {
                //Si está vacía
                if(!list.firstChild) {
                const listItem = document.createElement('li');
                listItem.textContent = 'No hay tareas.'
                list.appendChild(listItem);
                }
                console.log('Todas las notas se han mostrado');
            }
        };
    }

    function deleteItem(e) {
        // obtener ID
        let noteId = Number(e.target.parentNode.getAttribute('data-note-id'));

        let transaction = db.transaction(['notes_os'], 'readwrite');
        let objectStore = transaction.objectStore('notes_os');
        let request = objectStore.delete(noteId);

        transaction.oncomplete = function() {
            //elimina el li
            e.target.parentNode.parentNode.removeChild(e.target.parentNode);
            console.log('Nota ' + noteId + ' eliminada.');

            if(!list.firstChild) {
                const listItem = document.createElement('li');
                listItem.textContent = 'No hay tareas.';
                list.appendChild(listItem);
            }
        };
    }
}