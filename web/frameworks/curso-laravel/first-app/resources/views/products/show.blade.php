@extends('layouts.main')

@section('title', 'Products show')

@push('vite-scripts')
    @vite('resources/js/show_products.js')
@endpush

@section('content')
    <div id="ver_producto" data-id="{{ $product->id }}"></div>
@endsection