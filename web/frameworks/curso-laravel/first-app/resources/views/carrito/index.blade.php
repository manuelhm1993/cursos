@extends('layouts.main')

@push('vite-scripts')
    @vite('resources/js/proceso_compra.js')
@endpush

@section('content')
    <div id="proceso_compra"></div>
@endsection