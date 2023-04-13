# Serverless Data Engineering Pipeline
In this project, we need to reproduce the architecture of the example serverless data engineering project or perform something similar using only serverless technologies. I used naïve Bayes classifier as the generative probabilistic model for sentiment analysis. For the dataset, I chose the IMDB dataset, which contains 50K movie reviews for binary sentiment classification. Azure Databricks is used to build the serveless data pipeline. I also used Azure Cognitive Service for Language to build sentiment analysis Azure funciton at the end.

## Steps
1. Build a Azure Databricks Service and create a cluster
   * Use Azure portal to build a Azure Databricks Service
   ![databrciks](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/databricks.png)
   * Then, click `Launch Workspace`, you would get the workspace
   * After entering the workspace, you need to create a cluster.
   ![cluster](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/cluster.png)
2. Prepare data
   * In this task, I use `IMDB Dataset`, you should first upload the dataset to `DBFS` and copy the path.
   ![dbfs](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/dbfs.png)
   * Then, read the csv file and store it Delta Lake.
   ![read](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/read.png)
   * You chould check the result by running the following code.
   ![delta](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/delta.png)
3. Sentiment analysis
   * I built a naïve Bayes model for sentiment analysis. The whole process includes loading data, building vocabulary, training model, evaluating model and generating new data. You could check it in `./code/sentiment analysis.ipynb`.
4. Create an Azure Databricks job to run the pipeline
   * Click `Create job` in `Workflows`
   * Clike `Add a new task to your job` to build a new task. Enter a `name` as Task name, choose `Notebook` as type, choose `Workspace` as Source and select `the desired notebook` as the path. 
   * You can continue to `Add task` to complete your workflow.
   * Here's my workflow:
     ![workflow](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/workflow.png)
   * Click `Run Now` to run the workflow. You can check the running details by clicking the `Start time`.
     ![run](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/run.png)
     ![details](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/details.png)
     You can check the results by clicking one of your `task`. Here are the classification accuracy, some prediction results, and the generated new data .
     ![acc](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/acc.png)
     ![samples](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/samples.png)
     ![gen](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/gen.png)
   * Schedule the data pipeline job
     ![trigger](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/trigger.png)
5. Azure Functions
   * I also use Azure Cognitive Service for Language to build sentiment analysis Azure funciton.
     ![cognitive](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/cognitive.png)
   * Open codespace and log in to the Azure account.
   * Create a Azure function (`./api/SA/__init__.py`) and enter `func start` to run it.
     ![function](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/function.png)
   * With the function running, right click the function and choose `Execute Function Now...`. Enter the request message `{"text": "you are so pretty"}` to send it to the function.
     ![run](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/running.png)
   * Then you will get the sentiment analysis of this request message.
   
     ![result](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj4/result.png)
     
   * Deploy the project to the Azure by clicking the `Deploy...` button.


## Reference
* [Create a function in Azure with Python using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration)
* [ sentiment analysis in Azure Cognitive Service for Language](https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/overview)
* [Work with Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cmacos%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools)
* [Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/)
