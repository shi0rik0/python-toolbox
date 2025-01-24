import subprocess
import shutil
import importlib.resources
from pathlib import Path


def copy_files(*files):
    for file in files:
        with importlib.resources.path('python_toolbox.create_electron.data',
                                      file) as path:
            Path(file).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(path, file)


DEPENDENCIES = ['vue', 'pinia', 'vue-router']
DEV_DEPENDENCIES = [
    'prettier',

    # ESLint rules
    'eslint-config-prettier',
    'eslint-plugin-vue',

    # Vite plugins
    '@vitejs/plugin-vue',

    # TypeScript definitions
    '@types/electron-squirrel-startup',

    # For eslint.config.js
    '@eslint/compat@1.1.1',  # Version >= 1.2.0 will cause peer dependency conflict
    'globals',
    '@eslint/js',
    '@eslint/eslintrc',
    'eslint-define-config',

    # Tailwind CSS
    'tailwindcss@3.4.17',  # TODO: upgrade to 4.x.
    'postcss',
    'autoprefixer',
]

# On Windows, use `npm.cmd` instead of `npm`
NPM = 'npm.cmd' if shutil.which('npm.cmd') else 'npm'
NPX = 'npx.cmd' if shutil.which('npx.cmd') else 'npx'


def main():
    subprocess.run(
        [NPX, 'create-electron-app@latest', '--template=vite-typescript'],
        check=True)
    subprocess.run([NPM, 'install', *DEPENDENCIES], check=True)
    subprocess.run([NPM, 'install', '-D', *DEV_DEPENDENCIES], check=True)

    # Init Tailwind CSS config
    subprocess.run([NPX, 'tailwindcss', 'init', '-p'], check=True)

    # Copy Tailwind CSS config
    copy_files('tailwind.config.js')

    # Copy Vite config to enable the Vue plugin
    copy_files('vite.renderer.config.ts')

    # Copy Prettier config
    copy_files('.prettierrc', '.prettierignore')

    # Copy ESLint config
    copy_files('eslint.config.js')

    # Copy VSCode settings
    copy_files('.vscode/settings.json', '.vscode/extensions.json')

    # Mount Vue
    copy_files('src/App.vue', 'index.html', 'src/index.css', 'src/renderer.ts')

    # Format the code
    subprocess.run([NPX, 'prettier', '--write', '.'], check=True)
