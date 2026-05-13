import { useEffect, useState } from "react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend
} from "recharts";

function App() {
  const [equipos, setEquipos] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/equipos")
      .then((r) => r.json())
      .then((data) => setEquipos(data));
  }, []);

  const total = equipos.length;
  const criticos = equipos.filter(e => e.es_critico).length;
  const operativos = equipos.filter(e => e.estado === "Operativo").length;
  const fuera = equipos.filter(e => e.estado === "Fuera de servicio").length;

  const data = [
    { name: "Operativos", value: operativos },
    { name: "Fuera", value: fuera },
    { name: "Críticos", value: criticos },
  ];

  const COLORS = ["#22c55e", "#ef4444", "#3b82f6"];

  return (
    <div className="min-h-screen bg-slate-100 flex">

      {/* Sidebar */}
      <aside className="w-64 bg-slate-900 text-white p-6">
        <h1 className="text-2xl font-bold mb-8">
          CRM Biomédico
        </h1>

        <nav className="space-y-4 text-slate-300">
          <div className="hover:text-white cursor-pointer">Dashboard</div>
          <div className="hover:text-white cursor-pointer">Equipos</div>
          <div className="hover:text-white cursor-pointer">Historial</div>
          <div className="hover:text-white cursor-pointer">Reportes</div>
        </nav>
      </aside>

      {/* Main */}
      <main className="flex-1 p-8">

        <h2 className="text-3xl font-bold mb-6 text-slate-800">
          Panel General
        </h2>

        {/* KPI */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">

          <div className="bg-white rounded-2xl shadow p-5">
            <p className="text-gray-500">Total Equipos</p>
            <h3 className="text-3xl font-bold">{total}</h3>
          </div>

          <div className="bg-white rounded-2xl shadow p-5">
            <p className="text-gray-500">Críticos</p>
            <h3 className="text-3xl font-bold text-red-500">{criticos}</h3>
          </div>

          <div className="bg-white rounded-2xl shadow p-5">
            <p className="text-gray-500">Operativos</p>
            <h3 className="text-3xl font-bold text-green-500">{operativos}</h3>
          </div>

          <div className="bg-white rounded-2xl shadow p-5">
            <p className="text-gray-500">Fuera Servicio</p>
            <h3 className="text-3xl font-bold text-orange-500">{fuera}</h3>
          </div>

        </div>

        {/* Grid */}
        <div className="grid md:grid-cols-2 gap-6">

          {/* Chart */}
          <div className="bg-white rounded-2xl shadow p-6">
            <h3 className="text-xl font-semibold mb-4">
              Estado de Equipos
            </h3>

            <PieChart width={350} height={280}>
              <Pie
                data={data}
                dataKey="value"
                outerRadius={90}
                label
              >
                {data.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Pie>

              <Tooltip />
              <Legend />
            </PieChart>
          </div>

          {/* Equipos */}
          <div className="bg-white rounded-2xl shadow p-6">
            <h3 className="text-xl font-semibold mb-4">
              Últimos Equipos
            </h3>

            <div className="space-y-3">
              {equipos.slice(0, 5).map((equipo) => (
                <div
                  key={equipo.id}
                  className="border rounded-xl p-3"
                >
                  <p className="font-semibold">{equipo.nombre}</p>
                  <p className="text-sm text-gray-500">
                    {equipo.marca} - {equipo.modelo}
                  </p>
                  <p className="text-sm mt-1">
                    Estado: {equipo.estado}
                  </p>
                </div>
              ))}
            </div>

          </div>

        </div>

      </main>
    </div>
  );
}

export default App;