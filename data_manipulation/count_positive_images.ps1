# Define os caminhos dos diretórios
$diretorios = @(
    "C:\Users\Windows 10\Documents\IC\Imagens\Imagens Oficiais\Imagens HNGR Geral\HNGR_1",
    "C:\Users\Windows 10\Documents\IC\Imagens\Imagens Oficiais\Imagens HNGR Geral\HNGR_2",
    "C:\Users\Windows 10\Documents\IC\Imagens\Imagens Oficiais\Imagens HNGR Geral\HNGR_3"
)

# Extensões de arquivos de imagem, incluindo .jfif
$extensoesImagem = @("*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.tiff", "*.jfif")

$totalImagens = 0

# Itera sobre cada diretório
foreach ($dir in $diretorios) {
    if (Test-Path $dir) {
        # Conta imagens no diretório
        $contagem = 0
        foreach ($ext in $extensoesImagem) {
            $contagem += (Get-ChildItem -Path $dir -Filter $ext -File -ErrorAction SilentlyContinue).Count
        }
        Write-Host "Diretório: $dir"
        Write-Host "Imagens encontradas: $contagem"
        $totalImagens += $contagem
    } else {
        Write-Host "Diretório não encontrado: $dir"
    }
}

Write-Host "`nTotal de imagens em todos os diretórios: $totalImagens"