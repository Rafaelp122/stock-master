import { useEffect, useState } from "react";
import api from "./services/api"; // Importa o seu "mensageiro"
import { Button } from "@/components/ui/button";

function App() {
  // 1. O "Estado" (A memória do componente para guardar os produtos)
  const [products, setProducts] = useState([]);

  // 2. O "Efeito" (O que acontece quando a tela carrega)
  useEffect(() => {
    api
      .get("/products/items/")
      .then(response => {
        setProducts(response.data);
        console.log("Conectado ao Django!", response.data);
      })
      .catch(err => console.error("Erro na integração:", err));
  }, []);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-zinc-950 text-zinc-50 p-6">
      <div className="w-full max-w-2xl space-y-8 text-center">
        <div className="space-y-2">
          <h1 className="text-4xl font-bold tracking-tight">StockMaster</h1>
          <p className="text-zinc-400">
            {products.length > 0
              ? `Exibindo ${products.length} produtos do sistema.`
              : "Conectado à API. Nenhum produto encontrado."}
          </p>
        </div>

        {/* Lista de Produtos vinda do Backend */}
        <div className="grid gap-4 text-left">
          {products.length > 0 ? (
            // SE tiver produtos, faz o map
            products.map(product => (
              <div
                key={product.id}
                className="p-4 rounded-lg border border-zinc-800 bg-zinc-900/50 flex justify-between items-center"
              >
                <div>
                  <h3 className="font-medium text-zinc-100">{product.name}</h3>
                  <p className="text-sm text-zinc-500">{product.category_name}</p>
                </div>
                <span className="text-emerald-400 font-mono">
                  R$ {Number(product.price).toFixed(2)}
                </span>
              </div>
            ))
          ) : (
            <div className="p-8 rounded-lg border border-dashed border-zinc-800 text-center space-y-2">
              <p className="text-zinc-500">Nenhum produto cadastrado no estoque.</p>
              <p className="text-xs text-zinc-600">
                Cadastre algo via Django Admin para testar.
              </p>
            </div>
          )}
        </div>

        <div className="flex gap-4 justify-center">
          <Button onClick={() => window.location.reload()}>Atualizar Lista</Button>
          <Button variant="secondary">Configurações</Button>
          <Button variant="destructive">Apagar Tudo</Button>
        </div>
      </div>
    </div>
  );
}

export default App;
