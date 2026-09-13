@extends('layouts.main')

@section('title', 'Products')

@push('js-scripts')
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const container = document.querySelector('#products-wrapper');

            if (!container) return;

            // Delegación de eventos para interceptar clics en los enlaces de la paginación
            container.addEventListener('click', (event) => {
                const link = event.target.closest('.pagination a');

                if (link) {
                    event.preventDefault();
                    const url = link.getAttribute('href');

                    if (url) {
                        fetchProducts(url);
                    }
                }
            });

            function fetchProducts(url) {
                // Opacidad temporal para feedback visual de carga
                container.style.opacity = '0.5';

                fetch(url, {
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => {
                    if (!response.ok) throw new Error('Error al cargar productos');
                    return response.text();
                })
                .then(html => {
                    // Reemplazo del HTML parcial
                    container.innerHTML = html;
                    container.style.opacity = '1';

                    // Desplazar suavemente al inicio del listado
                    container.scrollIntoView({ behavior: 'smooth' });
                })
                .catch(error => {
                    console.error(error);
                    container.style.opacity = '1';
                });
            }
        });
    </script>
@endpush

@section('content')
    <h1 class="text-center my-4">PRODUCTS</h1>

    @include('includes.products')
@endsection