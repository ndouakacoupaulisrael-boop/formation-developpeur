$ErrorActionPreference = 'Stop'
$repoUrl = 'https://github.com/ndouakacoupaulisrael-boop/formation-developpeur.git'

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host 'Git est introuvable. Installe Git for Windows puis relance ce script.' -ForegroundColor Red
    exit 1
}

if (-not (Test-Path '.git')) {
    git init
    git branch -M main
    git remote add origin $repoUrl
} else {
    $remote = git remote get-url origin 2>$null
    if (-not $remote) {
        git remote add origin $repoUrl
    } elseif ($remote -ne $repoUrl) {
        git remote set-url origin $repoUrl
    }
    git branch -M main
}

git add .
$hasChanges = (git diff --cached --name-only)
if ($hasChanges) {
    git commit -m 'feat: publier portfolio et projets académiques'
} else {
    Write-Host 'Aucun nouveau changement à committer.'
}

git push -u origin main
Write-Host ''
Write-Host 'Publication terminée. Vérifie le dépôt :' -ForegroundColor Green
Write-Host 'https://github.com/ndouakacoupaulisrael-boop/formation-developpeur'
