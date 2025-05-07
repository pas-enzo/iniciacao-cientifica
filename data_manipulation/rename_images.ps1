# Definir os caminhos dos diretórios
$dirSantaCasa2 = "C:\Users\Windows 10\Documents\IC\Imagens\Imagens Oficiais\Imagens saudaveis\Santa Casa 2"
$dirSantaCasa3 = "C:\Users\Windows 10\Documents\IC\Imagens\Imagens Oficiais\Imagens saudaveis\Santa Casa 3"

# Função para renomear arquivos
function Rename-Images {
    param (
        [string]$directory,
        [int]$startNumber
    )
    
    # Obter todos os arquivos .jpg no diretório
    $files = Get-ChildItem -Path $directory -Filter "img*.jpg" | Sort-Object { [int]($_.BaseName -replace 'img', '') }
    
    $currentNumber = $startNumber
    
    foreach ($file in $files) {
        # Gerar novo nome
        $newName = "img$currentNumber.jpg"
        # $newPath = Join-Path -Path $directory -ChildPath $newName
        
        # Renomear o arquivo
        Rename-Item -Path $file.FullName -NewName $newName -Force
        
        Write-Host "Renomeado: $($file.Name) -> $newName"
        
        $currentNumber++
    }
    
    return $currentNumber
}

# Renomear imagens em Santa Casa 2, começando de 210
$nextNumber = Rename-Images -directory $dirSantaCasa2 -startNumber 210

# Renomear imagens em Santa Casa 3, começando do último número de Santa Casa 2
Rename-Images -directory $dirSantaCasa3 -startNumber $nextNumber