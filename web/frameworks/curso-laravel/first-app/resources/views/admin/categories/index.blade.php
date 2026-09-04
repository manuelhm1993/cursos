@extends('layouts.admin')

@section('content')
    @include('includes.success')

    <div class="row">
        <div class="col-lg">
            <div class="card">
                <div class="card-header"><i class="fa fa-list"></i> Lista de categorías</div>
                <div class="card-body">
                    <table class="table table-responsive-sm">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nombre</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            @foreach ($categories as $category)
                            <tr>
                                <td>{{ $category->id }}</td>
                                <td>{{ $category->nombre }}</td>
                                <td>
                                    <a href="{{ route('admin.categories.edit', $category->id) }}" class="btn btn-info">
                                        Editar
                                    </a>
                                    <button type="submit" role="button" class="btn btn-danger" form="borrar-id-{{ $category->id }}" onclick="return confirm('¿Está seguro que desea eliminar este elemento?')">
                                        Borrar
                                    </button>
                                    <form id="borrar-id-{{ $category->id }}" action="{{ route('admin.categories.destroy', $category->id) }}" method="post">
                                        @csrf
                                        @method('DELETE')
                                    </form>
                                </td>
                            </tr>
                            @endforeach
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
@endsection