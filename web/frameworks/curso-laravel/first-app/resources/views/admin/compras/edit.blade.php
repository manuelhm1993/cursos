@extends('layouts.admin')

@section('content')
    <div class="card">
        <div class="card-header">
            <strong>Compra</strong>
        </div>
        <div class="card-body">

            @include('includes.errores')

            <form method="post" action="{{ route('admin.compras.update', $compra->id) }}">
                @csrf
                @method('PUT')
                <div class="row">
                    <div class="col-sm-12">
                        <div class="form-group">
                            <label for="name">Pagado</label>
                            <select class="form-control" name="pagado">
                                <option value="0" @if(!$compra->pagado) selected @endif>
                                    No
                                </option>
                                <option value="1" @if($compra->pagado) selected @endif>
                                    Si
                                </option>
                            </select>
                        </div>
                    </div>

                    <div class="col-sm-12">
                        <button class="btn btn-info" type="submit">Actualizar</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
@endsection