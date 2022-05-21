from calculate import calories
from utils import add_class, remove_class

# define the task template that will be use to render new templates to the page
calories_template = Element("calories-template").select(".calories", from_content=True)
calories_result_content = Element("list-tasks-container")

# Inputs
sex_content = Element("sex-content")
weight_content = Element("weight-content")
activity_content = Element("activity-content")


def get_and_presents_results(*ags, **kws):

    check_empty_values()

    # get values and calculate calories needed
    sex, weight, physical_activity = get_values_from_content()
    calories_needed = calories(sex, weight, physical_activity)

    # add the calories_html_content to the page
    calories_html_content = calories_template.select("p")
    calories_html_content.element.innerText = calories_needed
    calories_result_content.element.appendChild(calories_template.element)

    add_class(calories_html_content)


def get_values_from_content():
    sex = int(sex_content.element.value)
    weight = int(weight_content.element.value)
    physical_activity = int(activity_content.element.value)
    check_weight(weight)
    return sex, weight, physical_activity


def check_weight(weight):
    if not 1 <= weight <= 100:
        exit()


def check_empty_values():
    # ignore if there are empty values
    if not weight_content.element.value and \
            activity_content.element.value and \
            sex_content.element.value:
        exit()


def clean_input_and_result():
    weight_content.clear()
    calories_html_content = calories_template.select("p")
    calories_html_content.element.innerText = ""
