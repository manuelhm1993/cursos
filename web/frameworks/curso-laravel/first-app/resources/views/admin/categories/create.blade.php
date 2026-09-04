@extends('layouts.admin')

@section('content')
<div class="row">
    <div class="col-md">
        <div class="card">
            <div class="card-header">
                <strong>Crear</strong> categoría
            </div>
            <div class="card-body">
                {{-- Mostrar los errores de validación --}}
                @include('includes.errores')

                <form action="{{ route('admin.categories.store') }}" method="post" id="edit-form">
                    @csrf
                    <div class="form-group">
                        <label for="nombre">Nombre</label>
                        <input class="form-control" id="nombre" type="text" name="nombre" placeholder="Verduras" value="{{ old('nombre') }}">
                    </div>
                </form>
            </div>
            <div class="card-footer">
                <button class="btn btn-sm btn-primary" type="submit" form="edit-form">Crear</button>
                <button class="btn btn-sm btn-danger" type="reset" form="edit-form">Limpiar</button>
            </div>
        </div>
    </div>
</div>
@endsection