<h1>Gracias por tu compra</h1>
<h2>Datos de la compra</h2>
<ul>
    <li><strong>Nombre:</strong> {{ $compra->nombre }}</li>
    <li><strong>Apellido:</strong> {{ $compra->apellido }}</li>
    <li><strong>Email:</strong> {{ $compra->email }}</li>
    <li><strong>Teléfono:</strong> {{ $compra->telefono }}</li>
    <li><strong>Método de entrega:</strong> {{ $compra->tipo_envio }}</li>

    @if ($compra->tipo_envio === \App\Utilities\Enums\TipoEnvio::DELIVERY)
        <li><strong>Dirección:</strong> {{ $compra->direccion }}</li>
        <li><strong>Código postal:</strong> {{ $compra->codigo_postal }}</li>
        <li><strong>Municipio:</strong> {{ $compra->municipio }}</li>
        <li><strong>Estado:</strong> {{ $compra->estado }}</li>
        <li><strong>País:</strong> {{ $compra->pais }}</li>
    @endif
</ul>

<h2>Productos</h2>
<table>
    <thead>
        <tr>
            <th>Nombre</th>
            <th>Cantidad</th>
            <th>Precio</th>
            <th>Subtotal</th>
        </tr>
    </thead>
    <tbody>
        @foreach ($compra->products as $product)
            <tr>
                <td>{{ $product->nombre }}</td>
                <td>{{ $product->pivot->cantidad }}</td>
                <td>${{ $product->pivot->precio }}</td>
                <td>${{ $product->pivot->precio * $product->pivot->cantidad }}</td>
            </tr>
        @endforeach
    </tbody>
</table>