<ul class="nav">
    <li class="nav-item">
        <a class="nav-link" href="{{ route('admin.dashboard') }}">
            <i class="nav-icon la la-lg la-dashboard"></i> Dashboard
        </a>
    </li>
    <li class="nav-title">Administrador</li>
    <li class="nav-item nav-dropdown">
        <a class="nav-link nav-dropdown-toggle" href="#">
            <i class="nav-icon la la-lg la-bank"></i> Categorías
        </a>
        <ul class="nav-dropdown-items">
            <li class="nav-item">
                <a class="nav-link" href="{{ route('admin.categories.index') }}">
                    <i class="nav-icon la la-lg la-puzzle"></i> Ver
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ route('admin.categories.create') }}">
                    <i class="nav-icon la la-lg la-puzzle"></i> Crear
                </a>
            </li>
        </ul>
    </li>
    <li class="nav-item nav-dropdown">
        <a class="nav-link nav-dropdown-toggle" href="#">
            <i class="nav-icon la la-lg la-bank"></i> Productos
        </a>
        <ul class="nav-dropdown-items">
            <li class="nav-item">
                <a class="nav-link" href="{{ route('admin.products.index') }}">
                    <i class="nav-icon la la-lg la-puzzle"></i> Ver
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{{ route('admin.products.create') }}">
                    <i class="nav-icon la la-lg la-puzzle"></i> Crear
                </a>
            </li>
        </ul>
    </li>
</ul>