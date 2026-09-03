@extends('layouts.main')

@section('title', 'Products show')

@section('content')
    <h1>PRODUCTO - {{ $product->nombre }}</h1>
@endsection