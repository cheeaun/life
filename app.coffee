fs = require 'fs'

# roots v2.1.2
# Files in this list will not be compiled - minimatch supported
ignore_files: ['_*', 'README*', '.gitignore', '.DS_Store', 'life.md']
ignore_folders: ['.git', 'css', 'js']

layouts:
  default: 'layout.jade'

locals:
  lifeConfig: JSON.stringify(
    customStylesheetURL: null
    yearLength: 120
    hideAge: false
    markdown: String(fs.readFileSync 'life.md')
  )
