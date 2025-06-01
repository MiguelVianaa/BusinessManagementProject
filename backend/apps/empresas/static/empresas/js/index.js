document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('deleteModal');
    const closeModal = document.getElementById('closeModal');
    const cancelDelete = document.getElementById('cancelDelete');
    const deleteForm = document.getElementById('deleteForm');
    let empresaIdToDelete = null;
    let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    document.querySelectorAll('.btn-delete').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            empresaIdToDelete = this.getAttribute('data-id');
            modal.style.display = 'flex';
        });
    });

    closeModal.onclick = cancelDelete.onclick = function() {
        modal.style.display = 'none';
        empresaIdToDelete = null;
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
            empresaIdToDelete = null;
        }
    };

    deleteForm.onsubmit = function(e) {
        e.preventDefault();
        if(!empresaIdToDelete) return;

        fetch(`/empresas/destroy/${empresaIdToDelete}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({})
        })
        .then(response => {
            modal.style.display = 'none';
            if (response.redirected) {
                window.location.href = response.url;
            } else if (response.ok) {
                window.location.reload();
            } else {
                alert("Erro ao excluir empresa!");
            }
        })
        .catch(() => {
            modal.style.display = 'none';
            alert("Erro de conexão.");
        });
    };
});