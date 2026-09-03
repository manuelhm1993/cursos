@extends('layouts.admin')

@section('content')
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