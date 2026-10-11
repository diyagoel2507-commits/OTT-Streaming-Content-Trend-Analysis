# Deployment Configuration and Rollback Evidence

## 1. Project Information

- **Project:** OTT Streaming Content Trend Analysis
- **Analysis Environment:** Google Colab
- **Programming Language:** Python
- **Libraries:** Pandas, Matplotlib, Seaborn
- **Query Language:** SQL
- **Version Control:** GitHub

## 2. Environment Setup

The analysis notebook was developed using Google Colab, a browser-based Python environment.

To reproduce the analysis:

1. Open the Jupyter notebook in Google Colab.
2. Ensure the Netflix dataset is available.
3. Install any missing libraries if required.
4. Run the notebook cells in order.
5. Review the data-cleaning outputs and six visualizations.

For local execution, Python and the required libraries must be installed.

## 3. Dataset Configuration

The project uses the public Netflix Movies and TV Shows dataset.

Dataset source: https://github.com/shivamb/netflix-shows

The CSV file is stored in the project's `data/` directory.

## 4. Deployment Status

This project is an exploratory data analysis project, not a deployed web application.

The notebook is intended to run in Google Colab. The GitHub repository stores the notebook, SQL queries, visualizations, and project documentation.

No live application deployment has been performed as part of this documented workflow.

## 5. Rollback Procedure

GitHub version history can be used to review and recover earlier project versions.

1. Open the repository on GitHub.
2. Navigate to the file or commit that needs review.
3. Open the commit history to identify the previous version.
4. Review the changes before reverting.
5. Use GitHub's revert functionality when available, or restore the previous file content in a new commit.
6. Verify the restored file and rerun the relevant notebook cells.

## 6. Rollback Evidence

**Evidence status:** Rollback testing has not yet been performed.

Before claiming rollback validation, test the procedure on a non-critical file or branch and record the test date, commit identifier, change made, restoration result, and verification outcome.

## 7. Limitations

- No live web application has been deployed.
- No automated deployment pipeline has been configured.
- Rollback recovery must be tested before it can be reported as verified.

## 8. Conclusion

This document records the project's execution environment, dataset source, repository-based recovery approach, and current deployment limitations. It distinguishes documented procedures from deployment or rollback tests that have not yet been completed.
