- this project will require 2 csv file

  1. keywords-everywhere-exported.csv
  2. moz-exported.csv

- then it will generate third file `final-keywords.csv` where first column will have the `keywords`, second `Search Vol` and third `Difficulty`

- if `Search Vol` or `Difficulty` is missing for a keyword, so that cell for that keyword will empty

- make sure to remove the rows before `Keyword` column inside `moz-exported.csv` means `Keyword` and other headings should be in first row

- the required files should be in the root of the project with exact names
