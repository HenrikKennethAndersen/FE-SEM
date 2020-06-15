# ----- Script hooks 

library( knitr)

# Script hook for printing only certain lines

hook_output <- knit_hooks$get("output")
knit_hooks$set(output = function(x, options) {
  lines <- options$output.lines
  if (is.null(lines)) {
    return(hook_output(x, options))  # pass to default hook
  }
  x <- unlist(strsplit(x, "\n"))
  more <- "..."
  if (length(lines)==1) {        # first n lines
    if (length(x) > lines) {
      # truncate the output, but add ....
      x <- c(head(x, lines), more)
    }
  } else {
    x <- c(if (abs(lines[1])>1) more else NULL, 
           x[lines], 
           if (length(x)>lines[abs(length(lines))]) more else NULL
    )
  }
  # paste these lines together
  x <- paste(c(x, ""), collapse = "\n")
  hook_output(x, options)
})

# From: https://community.rstudio.com/t/showing-only-the-first-few-lines-of-the-results-of-a-code-chunk/6963/2
# Retrieved on: 26.05.2020


# Script hook to increase space between text and chunk output 

hook_output_def = knitr::knit_hooks$get('output')
knitr::knit_hooks$set(output = function(x, options) {
  if (!is.null(options$vspaceout)) {
    end <- paste0("\\vspace{", options$vspaceout, "}")
    stringr::str_c(hook_output_def(x, options), end)
  } else {
    hook_output_def(x, options)
  }
})

hook_source_def = knitr::knit_hooks$get('source')
knitr::knit_hooks$set(source = function(x, options) {
  if (!is.null(options$vspaceecho)) {
    begin <- paste0("\\vspace{", options$vspaceecho, "}")
    stringr::str_c(begin, hook_source_def(x, options))
  } else {
    hook_source_def(x, options)
  }
})

# From: https://stackoverflow.com/questions/43379224/add-vertical-space-above-and-below-figures-code-chunks
# Retrieved on: 04.06.2020