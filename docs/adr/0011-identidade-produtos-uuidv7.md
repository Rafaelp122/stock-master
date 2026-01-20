# ADR-011: Identidade de Produtos via UUIDv7, SkuSequence e QR Code Dinâmico

**Data:** 19/01/2026  
**Status:** ✅ Implementado  

## Decisão
Adotar o UUIDv7 como identificador primário e fonte de dados para o QR Code, utilizando uma tabela de sequência dedicada (SkuSequence) para gerar SKUs numéricos sequenciais e imutáveis.

## Contexto
O sistema de gestão de estoque exige uma forma de identificar produtos tanto por humanos (visualmente) quanto por máquinas (leitores de QR Code). Utilizar o SKU (Stock Keeping Unit) como dado bruto do QR Code cria um acoplamento perigoso: se o SKU mudar, as etiquetas físicas tornam-se inúteis. Além disso, o uso de UUIDs aleatórios (v4) causa fragmentação de índices.

Durante o desenvolvimento, identificamos que calcular o próximo número do SKU via busca de texto (`Max("sku")`) é inseguro devido a erros lexicográficos (onde "10" pode ser lido como menor que "9" pelo banco) e riscos de concorrência (dois usuários gerando o mesmo número simultaneamente).

## Decisão Técnica

1. **Identificador Primário:** Migrar para o UUIDv7. Ele é ordenado pelo tempo, o que melhora a performance de inserção e indexação no PostgreSQL (B-tree friendly).

2. **QR Code (Abordagem Dinâmica):** O QR Code deve armazenar apenas o UUIDv7 do produto. O sistema de leitura fará um lookup no banco de dados para encontrar o item atual, permitindo que o SKU mude sem invalidar a etiqueta física.

3. **Geração de SKU (Sequencial):** Implementar um fallback automático caso o SKU não seja preenchido. O padrão será `[CAT]-[ANO]-[SEQUENCIAL]` (ex: `ELE-2026-0001`).

4. **Gerenciador de Sequência:** Utilizar uma tabela dedicada `SkuSequence` para rastrear o `last_number` por categoria e ano, garantindo integridade numérica.

5. **Controle de Concorrência:** Uso de `select_for_update()` em transações atômicas para bloquear a linha da sequência durante o incremento, impedindo duplicidade.

6. **Sanitização de Dados:** Todo SKU deve ser normalizado para remover acentos e caracteres especiais via `unicodedata`.

7. **Imutabilidade:** O SKU e o QR Code são gerados apenas na criação do registro (`is_new`), impedindo que edições posteriores alterem a identidade original.

8. **Gestão de Arquivos:** Utilizar Signals para garantir que a exclusão de um produto remova fisicamente seu arquivo de imagem do disco.

## Justificativa
- ✅ **UUIDv7:** Une unicidade global com performance de chave sequencial.
- ✅ **Desacoplamento:** O link entre objeto físico e digital torna-se eterno ao usar o ID no QR Code.
- ✅ **Confiabilidade Matemática:** A tabela de sequência garante que o próximo número será sempre +1, independente da formatação da string.
- ✅ **Segurança Multiusuário:** O bloqueio em nível de linha permite que o sistema escale sem conflitos de escrita.
- ✅ **Integridade de Storage:** A limpeza automática de arquivos evita o acúmulo de lixo eletrônico.

## Consequências

### Positivas
- ✅ Performance de banco de dados otimizada para grandes volumes.
- ✅ Risco zero de colisão de SKU em ambientes concorrentes.
- ✅ Etiquetas de QR Code imunes a mudanças de metadados.
- ✅ Ordenação numérica sempre correta (0001, 0002...).

### Negativas
- ⚠️ Exige a dependência adicional da biblioteca `uuid6`.
- ⚠️ Adiciona uma tabela extra (`SkuSequence`) ao esquema do banco.
- ⚠️ Requer reset ou migração cuidadosa do banco, pois o `id` é Primary Key.

## Implementação
- **Modelagem:** `Product.id` com `uuid6.uuid7` e `sku` com `db_index=True`.
- **Sequência:** Tabela `SkuSequence` com `unique_together` para categoria e ano.
- **Automação:** Método `save()` orquestrando `select_for_update()` e geração de imagem.
- **Infraestrutura:** Pasta `media/qrcodes/` gerenciada via Signal `post_delete`.

## Referência
- Requisito: RF04 (Geração automática de QR Code no Backend).
- Documento: `REQUIREMENTS.MD`.
- Issue: #5.
