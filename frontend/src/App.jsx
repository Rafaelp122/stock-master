import { Button } from "@/components/ui/button"

function App() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-zinc-950 text-zinc-50">
      <div className="space-y-4 text-center">
        <h1 className="text-4xl font-bold tracking-tight">StockMaster</h1>
        <p className="text-zinc-400">Ambiente Frontend configurado com sucesso.</p>
        
        <div className="flex gap-4 justify-center">
          <Button>Clique aqui</Button>
          <Button variant="secondary">Configurações</Button>
          <Button variant="destructive">Apagar Produto</Button>
        </div>
      </div>
    </div>
  )
}

export default App
