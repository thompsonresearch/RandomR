
# Install necessary packages if not already installed
if (!requireNamespace("shiny", quietly = TRUE)) install.packages("shiny")
if (!requireNamespace("fs", quietly = TRUE)) install.packages("fs")

library(shiny)
library(fs)

# Define UI
ui <- fluidPage(
  titlePanel("Directory and Subdirectory Creator"),
  mainPanel(
    textOutput("selectedDir"),
    actionButton("choose_dir", "Choose Directory")
  )
)

# Define server logic
server <- function(input, output, session) {
  observeEvent(input$choose_dir, {
    dir <- choose.dir(getwd(), "Select a Folder")
    output$selectedDir <- renderText({ dir })
    
    if (dir != "") {
      # Define the file structure with subfolders, change to suit needs.
      folders_to_create <- list(
        "Data" = c("Raw", "Processed", "Complete"),
        "R-Scripts" = c("Analysis", "Preprocessing", "GIS"), 
        "Py-Scripts" = c("Analysis", "Preprocessing", "GIS"),
        "Results" = c("Figures", "Tables", "Statistics"),
        "Documentation" = c("Drafts", "Supervisor Feedback", "For Submission")
      )
      
      # Create the folders and subfolders
      for (folder in names(folders_to_create)) {
        main_folder_path <- file.path(dir, folder)
        dir_create(main_folder_path)
        
        subfolders <- folders_to_create[[folder]]
        for (subfolder in subfolders) {
          dir_create(file.path(main_folder_path, subfolder))
        }
      }
      
      showModal(modalDialog(
        title = "Success",
        paste("Folders and subfolders created in:", dir),
        easyClose = TRUE,
        footer = NULL
      ))
    }
  })
}

# Run the application
shinyApp(ui = ui, server = server)
