const { fixupConfigRules } = require('@eslint/compat')
const globals = require('globals')
const tsParser = require('@typescript-eslint/parser')
const path = require('node:path')
const { fileURLToPath } = require('node:url')
const js = require('@eslint/js')
const { FlatCompat } = require('@eslint/eslintrc')
const { defineFlatConfig } = require('eslint-define-config')
const pluginVue = require('eslint-plugin-vue')
const eslintConfigPrettier = require('eslint-config-prettier')

const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all,
})

module.exports = defineFlatConfig([
  eslintConfigPrettier,
  ...pluginVue.configs['flat/recommended'],
  ...fixupConfigRules(
    compat.extends(
      'eslint:recommended',
      'plugin:@typescript-eslint/eslint-recommended',
      'plugin:@typescript-eslint/recommended',
      'plugin:import/recommended',
      'plugin:import/electron',
      'plugin:import/typescript'
    )
  ),
  {
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
      },
      parser: tsParser,
    },
  },
])
