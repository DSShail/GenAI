from langchain_core.prompts import PromptTemplate

#template
template=PromptTemplate(
    template="""
    You are tasked with summarizing or analyzing the research paper titled: **{research_paper}**.

The summary/analysis should be written in the style of: **{style}**.

The output should be of the following length: **{length}**.

Please make sure to:

- Adhere to the selected style.
- Maintain accuracy and avoid generating false or misleading information.
- Structure the content logically based on the selected length.

Now proceed with the task.

    """,
    input_variables=['research_paper','style','length']
)

template.save('template.json')