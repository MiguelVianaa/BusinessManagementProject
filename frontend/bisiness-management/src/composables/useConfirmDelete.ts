import swal from 'sweetalert2';
import axios from 'axios';

interface DeleteConfig {
    route: (item: any) => string;
    title?: string;
    msg?: string;
    confirmButtonName?: string;
    cancelButtonName?: string;
    msgSuccess?: string;
    msgFailed?: string;
    getName?: (item: any) => string;
}

export function useConfirmDelete(item: any, config: DeleteConfig): Promise<void> {

    return new Promise((resolve, reject) => {

        let htmlContent = config.msg || 'Você não poderá reverter essa ação.';
        if (config.getName) {
            htmlContent += `<br><br><strong>${config.getName(item)}</strong>`;
        }

        swal.fire({
            icon: 'warning',
            title: config.title || 'Tem certeza que deseja excluir?',
            html: htmlContent,
            showCancelButton: true,
            confirmButtonColor: '#D32F2F',
            confirmButtonText: config.confirmButtonName || 'Sim, Excluir!',
            cancelButtonText: config.cancelButtonName || 'Cancelar',
            reverseButtons: true,
        }).then(async (result) => {

            if (result.isConfirmed) {
                try {

                    await axios.delete(config.route(item));

                    swal.fire({
                        icon: 'success',
                        title: 'Excluído!',
                        text: config.msgSuccess || 'O item foi excluído com sucesso.',
                        timer: 2000,
                        showConfirmButton: false,
                    });

                    resolve();
                } catch (e) {
                    swal.fire({
                        icon: 'error',
                        title: 'Erro!',
                        text: config.msgFailed || 'Não foi possível excluir o item.',
                    });

                    reject(e);
                }
            } else {

                reject('cancelled');
            }
        });
    });
}